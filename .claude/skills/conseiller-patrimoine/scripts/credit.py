#!/usr/bin/env python3
"""Crédit immobilier à taux fixe et échéances constantes.

Taux en % annuel nominal (ex. 3.5). Mensualités hors assurance, sauf mention.

Exemples :
  python credit.py mensualite --capital 300000 --taux 3.5 --duree-mois 300
  python credit.py empruntable --mensualite 1800 --taux 3.5 --duree-mois 300
  python credit.py crd --capital 300000 --taux 3.5 --duree-mois 300 --apres 24
  python credit.py tableau --capital 300000 --taux 3.5 --duree-mois 300 --csv tableau.csv
  python credit.py ira --rembourse 50000 --crd-avant 200000 --taux 2.5
  python credit.py anticipation --crd 200000 --taux 2.5 --mois-restants 280 \
      --montant 50000 --rendement-net 2.0 --mode duree

Plafond des indemnités de remboursement anticipé (C. consom. art. R313-25) :
le plus faible de six mois d'intérêts sur le capital remboursé au taux moyen
du prêt et de 3 % du capital restant dû avant remboursement. Cas d'exclusion :
art. L313-48 (vente liée à une mobilité professionnelle, décès, cessation forcée
d'activité). L'offre de prêt peut prévoir mieux pour l'emprunteur.
"""

import argparse
import csv
import math
import sys


def _r(taux_annuel_pct):
    return taux_annuel_pct / 100.0 / 12.0


def mensualite(capital, taux_annuel_pct, n_mois):
    """Mensualité constante hors assurance."""
    if n_mois <= 0:
        raise ValueError("durée nulle")
    r = _r(taux_annuel_pct)
    if r == 0:
        return capital / n_mois
    return capital * r / (1 - (1 + r) ** (-n_mois))


def capital_empruntable(mens, taux_annuel_pct, n_mois):
    """Capital que rembourse une mensualité donnée (hors assurance)."""
    r = _r(taux_annuel_pct)
    if r == 0:
        return mens * n_mois
    return mens * (1 - (1 + r) ** (-n_mois)) / r


def crd_apres(capital, taux_annuel_pct, n_mois, k):
    """Capital restant dû après k échéances payées."""
    if k <= 0:
        return capital
    if k >= n_mois:
        return 0.0
    r = _r(taux_annuel_pct)
    m = mensualite(capital, taux_annuel_pct, n_mois)
    if r == 0:
        return capital - m * k
    return capital * (1 + r) ** k - m * ((1 + r) ** k - 1) / r


def tableau(capital, taux_annuel_pct, n_mois, assurance_mensuelle=0.0):
    """Liste de lignes (n, échéance, intérêts, capital amorti, assurance, CRD)."""
    r = _r(taux_annuel_pct)
    m = mensualite(capital, taux_annuel_pct, n_mois)
    crd = capital
    lignes = []
    for n in range(1, n_mois + 1):
        interets = crd * r
        amorti = m - interets
        if n == n_mois:
            amorti = crd
            m_eff = amorti + interets
        else:
            m_eff = m
        crd = crd - amorti
        lignes.append({
            "echeance": n,
            "mensualite": round(m_eff, 2),
            "interets": round(interets, 2),
            "capital_amorti": round(amorti, 2),
            "assurance": round(assurance_mensuelle, 2),
            "crd": round(max(crd, 0.0), 2),
        })
    return lignes


def ira_plafond(rembourse, crd_avant, taux_annuel_pct):
    """Plafond légal des IRA : min(6 mois d'intérêts sur le remboursé, 3 % du CRD avant)."""
    six_mois = rembourse * taux_annuel_pct / 100.0 / 2.0
    trois_pct = 0.03 * crd_avant
    return {"six_mois_interets": six_mois, "trois_pct_crd": trois_pct,
            "plafond": min(six_mois, trois_pct)}


def duree_pour_mensualite(crd, taux_annuel_pct, mens):
    """Nombre de mois (réel) pour amortir crd avec une mensualité donnée."""
    r = _r(taux_annuel_pct)
    if r == 0:
        return crd / mens
    if mens <= crd * r:
        return math.inf
    return -math.log(1 - crd * r / mens) / math.log(1 + r)


def anticipation(crd, taux_annuel_pct, mois_restants, montant, rendement_net_pct,
                 mode="duree", ira=0.0, assurance_economisee=0.0, assurance_mensuelle=0.0):
    """Compare, à la date de fin initiale du prêt, le patrimoine obtenu en
    (A) remboursant `montant` par anticipation, les mensualités libérées étant
        placées au rendement net, et
    (B) plaçant `montant` au rendement net en gardant le prêt.

    mode "duree" : mensualité inchangée, durée raccourcie.
    mode "mensualite" : durée inchangée, mensualité réduite.
    ira : indemnité payée en A (sortie de trésorerie le jour du remboursement).
    assurance_mensuelle : prime d'assurance emprunteur payée chaque mois en B.
        En mode "duree", elle s'arrête en A à la nouvelle fin du prêt : les
        primes ainsi évitées comptent dans l'avantage de A.
    assurance_economisee : baisse mensuelle de prime en A tant que le prêt court
        (0 si l'assurance est assise sur le capital initial).
    """
    if montant > crd:
        raise ValueError("montant supérieur au CRD")
    m0 = capital_empruntable(1.0, taux_annuel_pct, mois_restants)
    m_init = crd / m0  # mensualité actuelle sur la durée restante
    rp = (1 + rendement_net_pct / 100.0) ** (1 / 12.0) - 1
    crd_a = crd - montant

    # Option B : montant placé, prêt inchangé
    patrimoine_b = montant * (1 + rp) ** mois_restants

    # Option A : économies mensuelles placées
    economies = []
    if mode == "duree":
        n_a = duree_pour_mensualite(crd_a, taux_annuel_pct, m_init) if crd_a > 0 else 0
        n_a_entier = math.ceil(n_a - 1e-9)
        for mois in range(1, mois_restants + 1):
            if mois <= n_a_entier - 1:
                eco = assurance_economisee
            elif mois == n_a_entier:
                # dernière échéance partielle
                crd_av = crd_apres_mensualite(crd_a, taux_annuel_pct, m_init, mois - 1)
                derniere = crd_av * (1 + _r(taux_annuel_pct))
                eco = m_init - derniere + assurance_economisee
            else:
                eco = m_init + assurance_mensuelle
            economies.append(eco)
        detail = {"duree_restante_mois_A": n_a, "mensualite": m_init}
    elif mode == "mensualite":
        m_a = mensualite(crd_a, taux_annuel_pct, mois_restants) if crd_a > 0 else 0.0
        economies = [m_init - m_a + assurance_economisee] * mois_restants
        detail = {"mensualite_avant": m_init, "mensualite_apres": m_a}
    else:
        raise ValueError("mode inconnu")

    patrimoine_a = -ira * (1 + rp) ** mois_restants
    for i, eco in enumerate(economies, start=1):
        patrimoine_a += eco * (1 + rp) ** (mois_restants - i)

    interets_sans = m_init * mois_restants - crd
    if mode == "duree":
        interets_avec = sum(l["interets"] for l in _tableau_mensualite(crd_a, taux_annuel_pct, m_init))
    else:
        interets_avec = (m_a * mois_restants - crd_a) if crd_a > 0 else 0.0
    return {
        "patrimoine_A_remboursement": patrimoine_a,
        "patrimoine_B_placement": patrimoine_b,
        "avantage_A_moins_B": patrimoine_a - patrimoine_b,
        "interets_economises": interets_sans - interets_avec,
        **detail,
    }


def crd_apres_mensualite(crd, taux_annuel_pct, mens, k):
    r = _r(taux_annuel_pct)
    if r == 0:
        return max(crd - mens * k, 0.0)
    return crd * (1 + r) ** k - mens * ((1 + r) ** k - 1) / r


def _tableau_mensualite(crd, taux_annuel_pct, mens):
    r = _r(taux_annuel_pct)
    lignes = []
    while crd > 0.005 and len(lignes) < 1200:
        interets = crd * r
        amorti = min(mens - interets, crd)
        crd -= amorti
        lignes.append({"interets": interets, "amorti": amorti})
    return lignes


def _eur(x):
    return f"{x:,.2f} €".replace(",", " ").replace(".", ",")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    a = sp.add_parser("mensualite")
    a.add_argument("--capital", type=float, required=True)
    a.add_argument("--taux", type=float, required=True)
    a.add_argument("--duree-mois", type=int, required=True)
    a.add_argument("--assurance-mensuelle", type=float, default=0.0)

    a = sp.add_parser("empruntable")
    a.add_argument("--mensualite", type=float, required=True, help="hors assurance")
    a.add_argument("--taux", type=float, required=True)
    a.add_argument("--duree-mois", type=int, required=True)

    a = sp.add_parser("crd")
    a.add_argument("--capital", type=float, required=True)
    a.add_argument("--taux", type=float, required=True)
    a.add_argument("--duree-mois", type=int, required=True)
    a.add_argument("--apres", type=int, required=True, help="nombre d'échéances payées")

    a = sp.add_parser("tableau")
    a.add_argument("--capital", type=float, required=True)
    a.add_argument("--taux", type=float, required=True)
    a.add_argument("--duree-mois", type=int, required=True)
    a.add_argument("--assurance-mensuelle", type=float, default=0.0)
    a.add_argument("--csv", help="fichier de sortie (sinon résumé annuel à l'écran)")

    a = sp.add_parser("ira")
    a.add_argument("--rembourse", type=float, required=True)
    a.add_argument("--crd-avant", type=float, required=True)
    a.add_argument("--taux", type=float, required=True)

    a = sp.add_parser("anticipation")
    a.add_argument("--crd", type=float, required=True)
    a.add_argument("--taux", type=float, required=True)
    a.add_argument("--mois-restants", type=int, required=True)
    a.add_argument("--montant", type=float, required=True)
    a.add_argument("--rendement-net", type=float, required=True,
                   help="rendement annuel net d'impôt et de frais du placement alternatif, en %%")
    a.add_argument("--mode", choices=["duree", "mensualite"], default="duree")
    a.add_argument("--ira", type=float, default=0.0)
    a.add_argument("--assurance-mensuelle", type=float, default=0.0,
                   help="prime mensuelle actuelle ; en mode duree elle cesse plus tôt si l'on rembourse")
    a.add_argument("--assurance-economisee", type=float, default=0.0,
                   help="baisse mensuelle de prime pendant le prêt (0 si assise sur le capital initial)")

    args = p.parse_args(argv)

    if args.cmd == "mensualite":
        m = mensualite(args.capital, args.taux, args.duree_mois)
        cout = m * args.duree_mois - args.capital
        print(f"Hypothèses : capital {_eur(args.capital)}, taux {args.taux} %, {args.duree_mois} mois")
        print(f"Mensualité hors assurance : {_eur(m)}")
        if args.assurance_mensuelle:
            print(f"Mensualité assurance comprise : {_eur(m + args.assurance_mensuelle)}")
        print(f"Coût total des intérêts : {_eur(cout)}")
        if args.assurance_mensuelle:
            print(f"Coût total de l'assurance : {_eur(args.assurance_mensuelle * args.duree_mois)}")
    elif args.cmd == "empruntable":
        c = capital_empruntable(args.mensualite, args.taux, args.duree_mois)
        print(f"Hypothèses : mensualité {_eur(args.mensualite)} hors assurance, taux {args.taux} %, {args.duree_mois} mois")
        print(f"Capital empruntable : {_eur(c)}")
    elif args.cmd == "crd":
        print(f"Hypothèses : capital {_eur(args.capital)}, taux {args.taux} %, {args.duree_mois} mois")
        c = crd_apres(args.capital, args.taux, args.duree_mois, args.apres)
        print(f"CRD après {args.apres} échéances : {_eur(c)}")
    elif args.cmd == "tableau":
        lignes = tableau(args.capital, args.taux, args.duree_mois, args.assurance_mensuelle)
        if args.csv:
            with open(args.csv, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=list(lignes[0].keys()), delimiter=";")
                w.writeheader()
                w.writerows(lignes)
            print(f"{len(lignes)} lignes écrites dans {args.csv}")
        else:
            print("Année ; intérêts ; capital amorti ; CRD fin d'année")
            for an in range(0, (args.duree_mois + 11) // 12):
                bloc = lignes[an * 12:(an + 1) * 12]
                print(f"{an + 1} ; {_eur(sum(l['interets'] for l in bloc))} ; "
                      f"{_eur(sum(l['capital_amorti'] for l in bloc))} ; {_eur(bloc[-1]['crd'])}")
    elif args.cmd == "ira":
        d = ira_plafond(args.rembourse, args.crd_avant, args.taux)
        print(f"Six mois d'intérêts sur {_eur(args.rembourse)} : {_eur(d['six_mois_interets'])}")
        print(f"3 % du CRD avant remboursement : {_eur(d['trois_pct_crd'])}")
        print(f"Plafond légal des IRA : {_eur(d['plafond'])} (lire l'offre : elle peut prévoir moins ou une exonération)")
    elif args.cmd == "anticipation":
        d = anticipation(args.crd, args.taux, args.mois_restants, args.montant,
                         args.rendement_net, args.mode, args.ira, args.assurance_economisee,
                         args.assurance_mensuelle)
        print(f"Hypothèses : CRD {_eur(args.crd)}, taux {args.taux} %, {args.mois_restants} mois restants, "
              f"remboursement {_eur(args.montant)}, mode {args.mode}, placement alternatif {args.rendement_net} % net, "
              f"IRA {_eur(args.ira)}, assurance {_eur(args.assurance_mensuelle)}/mois")
        for k, v in d.items():
            print(f"{k} : {_eur(v) if 'mois' not in k else f'{v:.1f}'}")
        print("Lecture : avantage positif = rembourser enrichit davantage à la date de fin initiale, à liquidité perdue près.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

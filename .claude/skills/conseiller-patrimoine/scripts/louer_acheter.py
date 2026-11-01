#!/usr/bin/env python3
"""Louer ou acheter sa résidence principale : patrimoine net comparé à horizon.

Modèle mensuel, sans impôt (rendement du placement saisi net), plus-value de
résidence principale supposée exonérée. Celui des deux ménages dont la sortie
mensuelle est la plus faible place la différence au rendement du placement,
pour comparer deux budgets identiques.

Exemple :
  python3 louer_acheter.py --prix 450000 --frais-acquisition-pct 7.5 --apport 120000 \
      --taux 3.5 --duree-mois 300 --assurance-mensuelle 60 --taxe-fonciere 1500 \
      --entretien-pct 1.0 --charges-proprio 0 --valorisation-pct 1.5 --frais-revente-pct 5 \
      --loyer 1500 --hausse-loyer-pct 1.5 --rendement-placement-pct 4 --horizon 15

Toutes les hypothèses de marché (valorisation, hausse des loyers, rendement)
sont à sourcer et à tester en plusieurs valeurs.

Lecture : le placement du locataire est supposé net d'impôt chaque année, alors
que la plus-value de la résidence principale est exonérée. Saisir le rendement
brut d'un PEA ou d'un compte-titres favorise donc la location.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from credit import mensualite, crd_apres  # noqa: E402
from entrees import (duree_annees, entier_min, montant, montant_positif, pct_borne, pct_frais,  # noqa: E402
                     rendement, taux_pret)


def simuler(prix, frais_acquisition_pct, apport, taux, duree_mois, assurance_mensuelle,
            taxe_fonciere, entretien_pct, charges_proprio, valorisation_pct, frais_revente_pct,
            loyer, hausse_loyer_pct, rendement_placement_pct, horizon_annees):
    """Renvoie une liste annuelle (année, patrimoine acheteur, patrimoine locataire)."""
    frais = prix * frais_acquisition_pct / 100.0
    emprunt = max(prix + frais - apport, 0.0)
    m = mensualite(emprunt, taux, duree_mois) if emprunt > 0 else 0.0
    rp = (1 + rendement_placement_pct / 100.0) ** (1 / 12.0) - 1
    rv = (1 + valorisation_pct / 100.0) ** (1 / 12.0) - 1

    # Le locataire place l'apport dès le départ.
    placement_locataire = apport
    placement_acheteur = max(apport - prix - frais, 0.0)  # apport excédentaire placé
    valeur_bien = prix
    loyer_courant = loyer
    resultats = []
    for mois in range(1, int(horizon_annees * 12) + 1):
        an_index = (mois - 1) // 12
        valeur_bien *= 1 + rv
        cout_acheteur = ((m + assurance_mensuelle) if mois <= duree_mois else 0.0) \
            + (taxe_fonciere + charges_proprio) * (1 + valorisation_pct / 100.0) ** an_index / 12.0 \
            + valeur_bien * entretien_pct / 100.0 / 12.0
        cout_locataire = loyer_courant
        placement_locataire *= 1 + rp
        placement_acheteur *= 1 + rp
        diff = cout_acheteur - cout_locataire
        if diff > 0:
            placement_locataire += diff
        else:
            placement_acheteur += -diff
        if mois % 12 == 0:
            loyer_courant *= 1 + hausse_loyer_pct / 100.0
            annee = mois // 12
            crd = crd_apres(emprunt, taux, duree_mois, mois) if emprunt > 0 else 0.0
            net_acheteur = valeur_bien * (1 - frais_revente_pct / 100.0) - crd + placement_acheteur
            resultats.append((annee, net_acheteur, placement_locataire))
    return resultats, emprunt, m


def _eur(x):
    return f"{x:,.0f} €".replace(",", " ")


LIBELLES = {"achat": "l'achat", "location": "la location"}


def bascules(resultats):
    """Années où l'écart acheteur moins locataire change de signe (positif = l'achat passe devant)."""
    annees = []
    signe_prec = None
    for annee, acheteur, locataire in resultats:
        signe = acheteur > locataire
        if signe_prec is not None and signe != signe_prec:
            annees.append((annee, "achat" if signe else "location"))
        signe_prec = signe
    return annees


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for nom, typ, req in (("prix", montant_positif, True), ("frais-acquisition-pct", pct_frais, True),
                          ("apport", montant, True), ("taux", taux_pret, True),
                          ("duree-mois", entier_min(1), True), ("assurance-mensuelle", montant, False),
                          ("taxe-fonciere", montant, False), ("entretien-pct", pct_borne(0, 10, "entretien"), True),
                          ("charges-proprio", montant, False), ("valorisation-pct", rendement, True),
                          ("frais-revente-pct", pct_frais, True), ("loyer", montant_positif, True),
                          ("hausse-loyer-pct", rendement, True), ("rendement-placement-pct", rendement, True),
                          ("horizon", duree_annees(1, 60), True)):
        p.add_argument(f"--{nom}", type=typ, required=req, default=0.0)
    a = p.parse_args(argv)
    if a.horizon != int(a.horizon):
        print(f"Horizon ramené à {int(a.horizon)} ans : les résultats sont annuels.")
    a.horizon = int(a.horizon)
    if 0 < a.taux < 0.5:
        print(f"Attention : taux de {a.taux} % ; vérifier l'unité (3.5 pour 3,5 %).")
    res, emprunt, m = simuler(a.prix, a.frais_acquisition_pct, a.apport, a.taux, a.duree_mois,
                              a.assurance_mensuelle, a.taxe_fonciere, a.entretien_pct, a.charges_proprio,
                              a.valorisation_pct, a.frais_revente_pct, a.loyer, a.hausse_loyer_pct,
                              a.rendement_placement_pct, a.horizon)
    print(f"Hypothèses : prix {_eur(a.prix)}, frais {a.frais_acquisition_pct} %, apport {_eur(a.apport)}, "
          f"emprunt {_eur(emprunt)} à {a.taux} % sur {a.duree_mois} mois (mensualité {_eur(m)}), "
          f"valorisation {a.valorisation_pct} %/an, loyer {_eur(a.loyer)} +{a.hausse_loyer_pct} %/an, "
          f"placement {a.rendement_placement_pct} % net, entretien {a.entretien_pct} % de la valeur/an, "
          f"frais de revente {a.frais_revente_pct} %")
    print("Année ; patrimoine acheteur (revente nette, CRD déduit) ; patrimoine locataire ; écart")
    for annee, acheteur, locataire in res:
        print(f"{annee} ; {_eur(acheteur)} ; {_eur(locataire)} ; {_eur(acheteur - locataire)}")
    changements = bascules(res)
    if not changements:
        devant = "l'achat" if res[0][1] > res[0][2] else "la location"
        print(f"Aucune bascule sur l'horizon : {devant} reste devant chaque année.")
    elif len(changements) == 1:
        annee, sens = changements[0]
        print(f"Bascule en faveur de {LIBELLES[sens]} en année {annee}.")
    else:
        print("Plusieurs bascules : " + ", ".join(f"année {an} vers {LIBELLES[s]}" for an, s in changements)
              + ". Résultat sensible aux hypothèses : le tester avec d'autres valeurs.")
    print("Lecture : placement du locataire supposé net d'impôt chaque année ; la plus-value de résidence "
          "principale est exonérée. Un rendement brut saisi favorise la location.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Louer ou acheter sa résidence principale : patrimoine net comparé à horizon.

Modèle mensuel, sans impôt (rendement du placement saisi net), plus-value de
résidence principale supposée exonérée. Celui des deux ménages dont la sortie
mensuelle est la plus faible place la différence au rendement du placement,
pour comparer deux budgets identiques.

Exemple :
  python louer_acheter.py --prix 450000 --frais-acquisition-pct 7.5 --apport 120000 \
      --taux 3.5 --duree-mois 300 --assurance-mensuelle 60 --taxe-fonciere 1500 \
      --entretien-pct 1.0 --charges-proprio 0 --valorisation-pct 1.5 --frais-revente-pct 5 \
      --loyer 1500 --hausse-loyer-pct 1.5 --rendement-placement-pct 4 --horizon 15

Toutes les hypothèses de marché (valorisation, hausse des loyers, rendement)
sont à sourcer et à tester en plusieurs valeurs.
"""

import argparse
import sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
from credit import mensualite, crd_apres  # noqa: E402


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


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for nom, req in (("prix", True), ("frais-acquisition-pct", True), ("apport", True), ("taux", True),
                     ("duree-mois", True), ("assurance-mensuelle", False), ("taxe-fonciere", False),
                     ("entretien-pct", True), ("charges-proprio", False), ("valorisation-pct", True),
                     ("frais-revente-pct", True), ("loyer", True), ("hausse-loyer-pct", True),
                     ("rendement-placement-pct", True), ("horizon", True)):
        p.add_argument(f"--{nom}", type=float, required=req, default=0.0)
    a = p.parse_args(argv)
    res, emprunt, m = simuler(a.prix, a.frais_acquisition_pct, a.apport, a.taux, int(a.duree_mois),
                              a.assurance_mensuelle, a.taxe_fonciere, a.entretien_pct, a.charges_proprio,
                              a.valorisation_pct, a.frais_revente_pct, a.loyer, a.hausse_loyer_pct,
                              a.rendement_placement_pct, a.horizon)
    print(f"Hypothèses : prix {_eur(a.prix)}, frais {a.frais_acquisition_pct} %, apport {_eur(a.apport)}, "
          f"emprunt {_eur(emprunt)} à {a.taux} % sur {int(a.duree_mois)} mois (mensualité {_eur(m)}), "
          f"valorisation {a.valorisation_pct} %/an, loyer {_eur(a.loyer)} +{a.hausse_loyer_pct} %/an, "
          f"placement {a.rendement_placement_pct} % net, entretien {a.entretien_pct} % de la valeur/an, "
          f"frais de revente {a.frais_revente_pct} %")
    print("Année ; patrimoine acheteur (revente nette, CRD déduit) ; patrimoine locataire ; écart")
    bascule = None
    for annee, acheteur, locataire in res:
        if bascule is None and acheteur > locataire:
            bascule = annee
        print(f"{annee} ; {_eur(acheteur)} ; {_eur(locataire)} ; {_eur(acheteur - locataire)}")
    texte_bascule = str(bascule) if bascule else "aucune sur l'horizon"
    print(f"Année de bascule en faveur de l'achat : {texte_bascule}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

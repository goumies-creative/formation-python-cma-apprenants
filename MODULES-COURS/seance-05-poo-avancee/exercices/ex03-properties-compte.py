"""
Exercice 3 : CompteBancaire avec Properties et Validation
Objectif : Utiliser @property pour getters/setters avec validation
"""

print("=== EXERCICE 3 : COMPTE BANCAIRE AVEC PROPERTIES ===\n")

# TODO: Créer une classe CompteBancaire avec :
# - Attribut _solde (protégé, commence par _)
# - Attribut _taux_interet (protégé)
# - Méthode __init__(solde_initial, taux_interet)
#
# - @property solde (getter) qui retourne self._solde
# - @solde.setter qui :
#   * Valide que le solde >= 0
#   * Lève ValueError si négatif
#   * Sinon, modifie self._solde
#
# - @property taux_interet (getter)
# - @taux_interet.setter qui :
#   * Valide que le taux est entre 0 et 100
#   * Lève ValueError sinon
#
# - @property interets_annuels (getter LECTURE SEULE)
#   * Calcule et retourne solde * taux / 100
#   * Pas de setter !
#
# - Méthode deposer(montant) qui utilise le setter
# - Méthode retirer(montant) qui utilise le setter
# - Méthode __str__()

# Votre code ici :


# Tests
if __name__ == "__main__":
    print("--- Test Création ---")
    compte = CompteBancaire(1000, 2.5)
    print(f"Solde : {compte.solde}€")
    print(f"Taux : {compte.taux_interet}%")
    print(f"Intérêts annuels : {compte.interets_annuels}€")

    print("\n--- Test Dépôt ---")
    compte.deposer(500)
    print(f"Nouveau solde : {compte.solde}€")
    print(f"Nouveaux intérêts : {compte.interets_annuels}€")

    print("\n--- Test Retrait ---")
    compte.retirer(200)
    print(f"Solde après retrait : {compte.solde}€")

    print("\n--- Test Validation Solde ---")
    try:
        compte.solde = -100
    except ValueError as e:
        print(f"✅ Erreur attendue : {e}")

    print("\n--- Test Validation Taux ---")
    try:
        compte.taux_interet = 150
    except ValueError as e:
        print(f"✅ Erreur attendue : {e}")

    print("\n--- Test Property Lecture Seule ---")
    try:
        compte.interets_annuels = 100  # Ne devrait pas marcher
    except AttributeError as e:
        print(f"✅ Erreur attendue : Property en lecture seule")

    print("\n--- Affichage Final ---")
    print(compte)

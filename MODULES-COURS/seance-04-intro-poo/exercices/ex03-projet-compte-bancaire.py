"""
Exercice 3 : Projet Compte Bancaire
Objectif : Créer un système de gestion de compte bancaire complet
"""

print("=== EXERCICE 3 : PROJET COMPTE BANCAIRE ===\n")

# TODO: Créer une classe CompteBancaire avec :
# - Attributs : titulaire, numero_compte, solde
# - Attribut historique (liste des opérations)
#
# - Méthode __init__ : initialise le compte avec validation
#   * Le solde initial ne peut pas être négatif
#   * Le numéro de compte doit être une chaîne non vide
#
# - Méthode deposer(montant) :
#   * Ajoute le montant au solde
#   * Enregistre l'opération dans l'historique
#   * Le montant doit être positif
#
# - Méthode retirer(montant) :
#   * Retire le montant du solde
#   * Enregistre l'opération dans l'historique
#   * Vérifie que le solde est suffisant
#   * Le montant doit être positif
#
# - Méthode afficher_solde() : affiche le solde actuel
#
# - Méthode afficher_historique() : affiche toutes les opérations
#
# - Méthode __str__ : représentation lisible du compte

# Votre code ici :
class CompteBancaire:
    pass  # Remplacez pass par votre code


# Tests
if __name__ == "__main__":
    # Test 1 : Création de compte
    print("--- Création de compte ---")
    compte = CompteBancaire("Alice Dupont", "FR7612345678901234567890123", 1000)
    print(compte)

    # Test 2 : Dépôts
    print("\n--- Dépôts ---")
    compte.deposer(500)
    compte.deposer(250)
    compte.afficher_solde()

    # Test 3 : Retraits
    print("\n--- Retraits ---")
    compte.retirer(300)
    compte.retirer(100)
    compte.afficher_solde()

    # Test 4 : Retrait avec solde insuffisant
    print("\n--- Retrait avec solde insuffisant ---")
    compte.retirer(5000)  # Devrait échouer

    # Test 5 : Historique
    print("\n--- Historique des opérations ---")
    compte.afficher_historique()

    # BONUS : Test de validation
    print("\n--- Tests de validation ---")
    try:
        compte_invalide = CompteBancaire("Bob", "FR123", -100)
    except ValueError as e:
        print(f"Erreur attendue : {e}")

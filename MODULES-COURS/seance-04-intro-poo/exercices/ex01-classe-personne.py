"""
Exercice 1 : Classe Personne
Objectif : Créer une classe basique avec attributs et méthodes
"""

print("=== EXERCICE 1 : CLASSE PERSONNE ===\n")

# TODO: Créer une classe Personne avec :
# - Attributs : nom, prenom, age
# - Méthode __init__ pour initialiser ces attributs
# - Méthode se_presenter() qui affiche "Bonjour, je m'appelle [prenom] [nom] et j'ai [age] ans"
# - Méthode est_majeur() qui retourne True si age >= 18, False sinon
# - Méthode __str__ pour affichage lisible

# Votre code ici :
class Personne:
    pass  # Remplacez pass par votre code


# Tests
if __name__ == "__main__":
    # Test 1 : Création et présentation
    alice = Personne("Dupont", "Alice", 25)
    alice.se_presenter()

    # Test 2 : Vérification majorité
    bob = Personne("Martin", "Bob", 17)
    print(f"Alice est majeure : {alice.est_majeur()}")
    print(f"Bob est majeur : {bob.est_majeur()}")

    # Test 3 : Affichage avec __str__
    print(f"\nAffichage d'Alice : {alice}")
    print(f"Affichage de Bob : {bob}")

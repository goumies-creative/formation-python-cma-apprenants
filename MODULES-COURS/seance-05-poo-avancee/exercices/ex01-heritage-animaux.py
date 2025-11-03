"""
Exercice 1 : Hiérarchie d'Animaux
Objectif : Créer une hiérarchie Animal -> Chien/Chat avec héritage
"""

print("=== EXERCICE 1 : HIÉRARCHIE ANIMAUX ===\n")

# TODO: Créer une classe Animal avec :
# - Attributs : nom, age
# - Méthode __init__(nom, age)
# - Méthode manger() qui affiche "[nom] mange"
# - Méthode dormir() qui affiche "[nom] dort"
# - Méthode __str__() pour affichage

# TODO: Créer une classe Chien qui hérite d'Animal :
# - Méthode aboyer() qui affiche "[nom] fait: Ouaf!"

# TODO: Créer une classe Chat qui hérite d'Animal :
# - Méthode miauler() qui affiche "[nom] fait: Miaou!"

# Votre code ici :


# Tests
if __name__ == "__main__":
    print("--- Test Chien ---")
    rex = Chien("Rex", 3)
    rex.manger()   # Hérité d'Animal
    rex.dormir()   # Hérité d'Animal
    rex.aboyer()   # Propre à Chien
    print(rex)

    print("\n--- Test Chat ---")
    felix = Chat("Felix", 2)
    felix.manger()  # Hérité d'Animal
    felix.miauler() # Propre à Chat
    print(felix)

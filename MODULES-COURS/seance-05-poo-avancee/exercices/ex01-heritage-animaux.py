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

# TODO: consignes :
# Spécifications :

# Classe Animal avec attribut nom et méthodes
# Classe Chien hérite d'Animal + attribut race
# Classe Chat hérite d'Animal + attribut couleur
# Override de faire_son() dans chaque enfant
# Utiliser super().__init__() correctement

# Votre code ici :
class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def manger(self):
        print(f"{self.nom} mange")

    def dormir(self):
        print(f"{self.nom} dort")

    def faire_son(self):
        print("Son générique")

    def __str__(self):
        return f"Animal(nom={self.nom}, age={self.age})"
    
class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age, race)

    def faire_son(self):
        print("Ouaf!")

    def aboyer(self):
        print(f"{self.nom} fait: Ouaf!")

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age, couleur)

    def faire_son(self):
        print("Miaou!")

    def miauler(self):
        print(f"{self.nom} fait: Miaou!")


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

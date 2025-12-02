"""
Exercice 2 : Classe Voiture
Objectif : Créer une classe avec méthodes d'action et attributs dynamiques
"""

print("=== EXERCICE 2 : CLASSE VOITURE ===\n")

# TODO: Créer une classe Voiture avec :
# - Attributs : marque, modele, annee
# - Attribut km initialisé à 0
# - Attribut en_marche initialisé à False
#
# - Méthode demarrer() : met en_marche à True
# - Méthode arreter() : met en_marche à False
# - Méthode rouler(distance) : ajoute distance à km (seulement si en_marche est True)
# - Méthode afficher_info() : affiche toutes les infos de la voiture
# - Méthode __str__ pour affichage

# Votre code ici :
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = 0
        self.en_marche = False

    def demarrer(self):
        self.en_marche = True
        print(f"La voiture {self.marque} {self.modele} a démarré.")

    def arreter(self):
        self.en_marche = False
        print(f"La voiture {self.marque} {self.modele} est arrêtée.")

    def rouler(self, distance):
        if self.en_marche:
            self.km += distance
            print(f"La voiture {self.marque} {self.modele} a roulé {distance} km.")
        else:
            print(f"La voiture {self.marque} {self.modele} ne peut pas rouler car elle est arrêtée.")

    def afficher_info(self):
        print(f"Voiture : {self}")

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - {self.km} km - En marche: {self.en_marche}"


# Tests
if __name__ == "__main__":
    # Test 1 : Création de voiture
    ma_voiture = Voiture("Renault", "Clio", 2020)
    ma_voiture.afficher_info()

    # Test 2 : Tentative de rouler sans démarrer
    print("\n--- Tentative de rouler sans démarrer ---")
    ma_voiture.rouler(50)

    # Test 3 : Démarrage et trajet
    print("\n--- Démarrage et trajet ---")
    ma_voiture.demarrer()
    ma_voiture.rouler(50)
    ma_voiture.rouler(100)
    ma_voiture.afficher_info()

    # Test 4 : Arrêt
    print("\n--- Arrêt ---")
    ma_voiture.arreter()
    ma_voiture.rouler(30)  # Ne devrait pas fonctionner

"""
Exercice 2 : Système de Véhicules avec Héritage
Objectif : Créer une hiérarchie Vehicule -> Voiture/Moto avec super() et override
"""

print("=== EXERCICE 2 : SYSTÈME DE VÉHICULES ===\n")

# TODO: Créer une classe Vehicule avec :
# - Attributs : marque, annee, km
# - Méthode __init__(marque, annee, km=0)
# - Méthode rouler(distance) qui ajoute à km
# - Méthode afficher_info() qui affiche toutes les infos
# - Méthode __str__()

# TODO: Créer une classe Voiture qui hérite de Vehicule :
# - Ajouter attribut nb_portes
# - Utiliser super().__init__() pour initialiser les attributs du parent
# - OVERRIDE afficher_info() pour inclure nb_portes
#   (appeler super().afficher_info() puis ajouter les portes)

# TODO: Créer une classe Moto qui hérite de Vehicule :
# - Ajouter attribut type_moto (ex: "sportive", "cross")
# - Utiliser super().__init__()
# - OVERRIDE afficher_info() pour inclure type_moto

# Votre code ici :


# Tests
if __name__ == "__main__":
    print("--- Test Voiture ---")
    voiture = Voiture("Renault", 2020, nb_portes=5, km=15000)
    voiture.afficher_info()
    voiture.rouler(100)
    voiture.afficher_info()
    print(voiture)

    print("\n--- Test Moto ---")
    moto = Moto("Yamaha", 2021, type_moto="sportive", km=5000)
    moto.afficher_info()
    moto.rouler(50)
    moto.afficher_info()
    print(moto)

    print("\n--- Test Polymorphisme ---")
    vehicules = [voiture, moto]
    for v in vehicules:
        print(f"\n{v.__class__.__name__} :")
        v.afficher_info()

"""
Exercice 2 : Jeu de Dés avec Statistiques
Objectif : Créer un simulateur de dés qui garde les statistiques
"""

print("=== EXERCICE 2 : SIMULATEUR DE DÉS ===\n")

# TODO: Importer random et datetime
import random
from datetime import datetime  

# TODO: Créer une liste vide pour stocker l'historique des lancers
historique = []

# TODO: Créer une fonction lancer_des(nb_des=2) qui :
#   - Lance nb_des dés (nombre aléatoire 1-6 pour chaque dé)
#   - Calcule le total
#   - Enregistre le résultat dans l'historique avec l'heure
#   - Affiche les résultats
#   - Retourne le total

def lancer_des(nb_des=2):
    """Lance plusieurs dés et retourne le total"""
    # TODO: Créer une fonction lancer_des(nb_des=2) qui :
#   - Lance nb_des dés (nombre aléatoire 1-6 pour chaque dé)
#   - Calcule le total
#   - Enregistre le résultat dans l'historique avec l'heure
#   - Affiche les résultats
#   - Retourne le total
    des = [random.randint(1, 6) for _ in range(nb_des)]
    total = sum(des)
    heure = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historique.append((heure, des, total))
    print(f"Lancé des : {des} | Total : {total} | Heure : {heure}")
    return total
    


# TODO: Créer une fonction afficher_statistiques() qui :
#   - Affiche le nombre total de lancers
#   - Affiche le total minimum
#   - Affiche le total maximum
#   - Affiche la moyenne des totaux
#   - Affiche tous les lancers avec leur heure


def afficher_statistiques():
    """Affiche les statistiques des lancers"""
    # TODO: Créer une fonction afficher_statistiques() qui :
    #   - Affiche le nombre total de lancers
    #   - Affiche le total minimum
    #   - Affiche le total maximum
    #   - Affiche la moyenne des totaux
    #   - Affiche tous les lancers avec leur heure  
    if not historique:
        print("Aucun lancer effectué.")
        return
    total_lancers = len(historique)
    totaux = [entry[2] for entry in historique]
    total_min = min(totaux)
    total_max = max(totaux)
    moyenne = sum(totaux) / total_lancers 
    print(f"Nombre total de lancers : {total_lancers}")
    print(f"Total minimum : {total_min}")
    print(f"Total maximum : {total_max}")
    print(f"Moyenne des totaux : {moyenne:.2f}")
    print("Historique des lancers :")
    for entry in historique:
        print(f"Heure : {entry[0]} | Dés : {entry[1]} | Total : {entry[2]}")


# TODO: Créer une fonction jeu_principal() qui :
#   - Affiche un menu
#   - Propose : 1) Lancer les dés, 2) Voir statistiques, 3) Quitter
#   - Boucle tant que l'utilisateur ne choisit pas "Quitter"


def jeu_principal():
    """Boucle principale du jeu"""
    print("🎲 BIENVENUE DANS LE SIMULATEUR DE DÉS 🎲")
    print("=" * 50)

    # TODO: Créer une fonction jeu_principal() qui :
    #   - Affiche un menu
    #   - Propose : 1) Lancer les dés, 2) Voir statistiques, 3) Quitter
    #   - Boucle tant que l'utilisateur ne choisit pas "Quitter"

    while True:
        print("\nMenu :")
        print("1. Lancer les dés")
        print("2. Voir statistiques")
        print("3. Quitter")
        choix = input("Choisissez une option (1-3) : ")
        if choix == "1":
            nb_des = input("Combien de dés lancer ? (par défaut 2) : ")
            nb_des = int(nb_des) if nb_des.isdigit() else 2
            lancer_des(nb_des)
        elif choix == "2":
            afficher_statistiques()
        elif choix == "3":
            print("Merci d'avoir joué ! Au revoir.")
            break
        else:
            print("Option invalide. Veuillez réessayer.")  

# Tests
if __name__ == "__main__":
    # Lancer le jeu
    jeu_principal()

    # Ou tests unitaires :
    # print("Tests unitaires...")
    # lancer_des(2)
    # lancer_des(3)
    # afficher_statistiques()

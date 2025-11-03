"""
Exercice 2 : Jeu de Dés avec Statistiques
Objectif : Créer un simulateur de dés qui garde les statistiques
"""

print("=== EXERCICE 2 : SIMULATEUR DE DÉS ===\n")

# TODO: Importer random et datetime


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
    # Votre code ici
    pass


# TODO: Créer une fonction afficher_statistiques() qui :
#   - Affiche le nombre total de lancers
#   - Affiche le total minimum
#   - Affiche le total maximum
#   - Affiche la moyenne des totaux
#   - Affiche tous les lancers avec leur heure


def afficher_statistiques():
    """Affiche les statistiques des lancers"""
    # Votre code ici
    pass


# TODO: Créer une fonction jeu_principal() qui :
#   - Affiche un menu
#   - Propose : 1) Lancer les dés, 2) Voir statistiques, 3) Quitter
#   - Boucle tant que l'utilisateur ne choisit pas "Quitter"


def jeu_principal():
    """Boucle principale du jeu"""
    print("🎲 BIENVENUE DANS LE SIMULATEUR DE DÉS 🎲")
    print("=" * 50)

    # Votre code ici
    pass


# Tests
if __name__ == "__main__":
    # Lancer le jeu
    jeu_principal()

    # Ou tests unitaires :
    # print("Tests unitaires...")
    # lancer_des(2)
    # lancer_des(3)
    # afficher_statistiques()

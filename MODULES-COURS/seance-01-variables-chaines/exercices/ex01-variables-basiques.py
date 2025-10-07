"""
Exercice 1 : Variables Basiques
Objectif : Pratiquer la création et l'utilisation de variables
"""

print("=== EXERCICE 1 : VARIABLES BASIQUES ===")

# TODO: Créez des variables pour vous décrire
# - Votre prénom (string)
# - Votre âge (integer)
# - Votre taille en mètres (float)
# - Si vous aimez Python (booléen)

prenom = "Marie"
age = 25
taille = 1.65
aime_python = True

# TODO: Affichez ces variables avec des messages personnalisés
print(f"Je m'appelle {prenom}")
print(f"J'ai {age} ans")
print(f"Je mesure {taille} mètres")
print(f"J'aime Python : {aime_python}")

# TODO: Créez une variable pour l'année de naissance et calculez-la
annee_actuelle = 2025
annee_naissance = annee_actuelle - age
print(f"Je suis né(e) en {annee_naissance}")

# TODO: Créez une liste de vos 3 hobbies préférés
hobbies = ["lecture", "randonnée", "cuisine"]
print(f"Mes hobbies : {hobbies}")

# TODO: Créez un dictionnaire avec vos informations de contact
contact = {
    "email": "marie@email.com",
    "telephone": "01 23 45 67 89",
    "ville": "Paris"
}
print(f"Mes contacts : {contact}")

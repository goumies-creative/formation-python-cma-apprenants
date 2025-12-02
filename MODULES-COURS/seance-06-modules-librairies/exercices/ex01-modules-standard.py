"""
Exercice 1 : Exploration des Modules Standard
Objectif : Utiliser random et datetime pour créer des programmes simples
"""

print("=== EXERCICE 1 : MODULES STANDARD ===\n")

# PARTIE A : Module random
print("PARTIE A : Générateur de Nombres Aléatoires")
print("-" * 40)

# TODO: Importer le module random
import random

# TODO: 1. Générer et afficher un nombre aléatoire entre 1 et 100
random_number = random.randint(1, 100)
print(f"Nombre aléatoire entre 1 et 100 : {random_number}")

# TODO: 2. Simuler un lancer de dé (1 à 6)
dice_roll = random.randint(1, 6)
print(f"Lancer de dé : {dice_roll}")    

# TODO: 3. Choisir aléatoirement une couleur parmi ['rouge', 'vert', 'bleu', 'jaune']
colors = ['rouge', 'vert', 'bleu', 'jaune']
chosen_color = random.choice(colors)
print(f"Couleur choisie : {chosen_color}")

# TODO: 4. Créer une liste de 5 nombres aléatoires entre 1 et 20
random_numbers_list = [random.randint(1, 20) for _ in range(5)]
print(f"Liste de 5 nombres aléatoires entre 1 et 20 : {random_numbers_list}")

# TODO: 5. Mélanger la liste ['As', 'Roi', 'Dame', 'Valet', '10'] et l'afficher
cards = ['As', 'Roi', 'Dame', 'Valet', '10']
random.shuffle(cards)
print(f"Liste de cartes mélangée : {cards}")


print("\n" + "=" * 40)
print("PARTIE B : Module datetime")
print("-" * 40)

# TODO: Importer datetime, date, et timedelta
from datetime import datetime, date, timedelta

# TODO: 1. Afficher la date et l'heure actuelles
now = datetime.now()
print(f"Date et heure actuelles : {now}")

# TODO: 2. Afficher uniquement la date du jour au format JJ/MM/AAAA
today = date.today()
print(f"Date du jour (JJ/MM/AAAA) : {today.strftime('%d/%m/%Y')}")

# TODO: 3. Calculer votre âge à partir de votre date de naissance
#         (Utilisez date(année, mois, jour) pour créer votre date de naissance)
birth_date = date(1990, 1, 1)  # Remplacez par votre date de naissance
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print(f"Âge : {age} ans")

# TODO: 4. Calculer et afficher la date dans 30 jours
date_in_30_days = today + timedelta(days=30)
print(f"Date dans 30 jours : {date_in_30_days.strftime('%d/%m/%Y')}")

# TODO: 5. Calculer combien de jours il reste jusqu'à Noël 2025 (25 décembre)
christmas_2025 = date(2025, 12, 25)
days_until_christmas = (christmas_2025 - today).days
print(f"Jours jusqu'à Noël 2025 : {days_until_christmas} jours")


# Bonus : Créer un message personnalisé avec la date et une couleur aléatoire
print("\n" + "=" * 40)
print("BONUS : Message du jour")
print("-" * 40)

# TODO: Créer une liste de messages motivants
messages = [
    "Aujourd'hui est une nouvelle opportunité !",
    "Croyez en vous et tout est possible.",
    "Chaque jour est un cadeau, profitez-en !",
    "Le succès vient à ceux qui persévèrent.",
    "Faites de votre mieux et laissez le reste suivre."
]
# TODO: Choisir un message aléatoirement
chosen_message = random.choice(messages)    

# TODO: Afficher "Message du [date] : [message]"
print(f"Message du {today.strftime('%d/%m/%Y')} : {chosen_message}")
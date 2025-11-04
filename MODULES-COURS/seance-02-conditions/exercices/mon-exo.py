age = int(input("Quel âge avez-vous ? "))

if age >= 18:
    print("Vous êtes majeur !")
else:
    annees_restantes = 18 - age
    print(f"Vous serez majeur dans {annees_restantes} an(s)")
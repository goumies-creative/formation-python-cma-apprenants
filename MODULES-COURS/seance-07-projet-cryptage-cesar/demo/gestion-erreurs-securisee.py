# Avec gestion d'erreur : SÉCURITÉ
try:
    age = int("abc")
except ValueError:
    print("Erreur : pas un nombre")
    age = 0
# Programme continue
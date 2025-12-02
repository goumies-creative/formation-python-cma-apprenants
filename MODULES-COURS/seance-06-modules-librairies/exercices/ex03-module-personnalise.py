"""
Exercice 3 : Créer et Utiliser un Module Personnalisé
Objectif : Créer un module utils.py avec des fonctions réutilisables
"""

print("=== EXERCICE 3 : MODULE PERSONNALISÉ ===\n")

# PARTIE 1 : Créer le module utils.py
print("PARTIE 1 : Création du module utils.py")
print("-" * 40)

# TODO: Créer un fichier utils.py dans le même dossier avec les fonctions suivantes :
#
# 1. est_pair(nombre) -> bool
#    Retourne True si le nombre est pair
#
# 2. est_palindrome(texte) -> bool
#    Retourne True si le texte est un palindrome (ignore les espaces et la casse)
#    Exemples : "radar", "Kayak", "La mariée ira mal"
#
# 3. compter_voyelles(texte) -> int
#    Compte le nombre de voyelles dans le texte
#
# 4. inverser_chaine(texte) -> str
#    Retourne le texte inversé
#
# 5. liste_to_string(liste, separateur=", ") -> str
#    Convertit une liste en chaîne avec séparateur
#    Exemple : [1, 2, 3] -> "1, 2, 3"
#
# N'oubliez pas d'ajouter :
#   - Des docstrings pour chaque fonction
#   - Un bloc if __name__ == "__main__": avec des tests
#   - Des commentaires explicatifs

print("⚠️  Créez d'abord le fichier utils.py avec les fonctions demandées")
print("   Puis décommentez le code ci-dessous pour tester.\n")

# PARTIE 2 : Utiliser le module
print("PARTIE 2 : Utilisation du module utils.py")
print("-" * 40)

# TODO: Une fois utils.py créé, décommentez les lignes suivantes :

from utils import est_pair, est_palindrome, compter_voyelles, inverser_chaine, liste_to_string

# Test 1 : est_pair
nombres = [10, 15, 22, 7, 100]
print("Test est_pair:")
for nb in nombres:
    if est_pair(nb):
        print(f"  {nb} est pair")
    else:
        print(f"  {nb} est impair")

# # Test 2 : est_palindrome
mots = ["radar", "Python", "Kayak", "ressasser"]
print("\nTest est_palindrome:")
for mot in mots:
    if est_palindrome(mot):
        print(f"  '{mot}' est un palindrome ✓")
    else:
        print(f"  '{mot}' n'est pas un palindrome ✗")

# Test 3 : compter_voyelles
phrases = ["Hello World", "Python est génial", "AEIOU"]
print("\nTest compter_voyelles:")
for phrase in phrases:
    nb = compter_voyelles(phrase)
    print(f"  '{phrase}' contient {nb} voyelle(s)")

# Test 4 : inverser_chaine
textes = ["Python", "Bonjour", "12345"]
print("\nTest inverser_chaine:")
for texte in textes:
    inverse = inverser_chaine(texte)
    print(f"  '{texte}' inversé = '{inverse}'")

# Test 5 : liste_to_string
listes = [
    ([1, 2, 3, 4, 5], ", "),
    (["a", "b", "c"], " - "),
    (["Alice", "Bob", "Charlie"], " et ")
]
print("\nTest liste_to_string:")
for liste, sep in listes:
    resultat = liste_to_string(liste, sep)
    print(f"  {liste} avec '{sep}' = '{resultat}'")


# PARTIE 3 : Mini-projet avec le module
print("\n" + "=" * 40)
print("PARTIE 3 : Mini-projet")
print("-" * 40)

# TODO: Créer un petit programme qui :
#   1. Demande à l'utilisateur de saisir une phrase
#   2. Affiche si c'est un palindrome
#   3. Affiche le nombre de voyelles
#   4. Affiche la phrase inversée
#   5. Affiche les mots de la phrase séparés par " | "
phrase = input("Entrez une phrase : ")
print("\nAnalyse de votre phrase :")
# Palindrome
if est_palindrome(phrase):
    print("- Palindrome : Oui ✓")
else:
    print("- Palindrome : Non ✗")
# Nombre de voyelles
nb_voyelles = compter_voyelles(phrase)
print(f"- Nombre de voyelles : {nb_voyelles}")
# Phrase inversée  
phrase_inversee = inverser_chaine(phrase)
print(f"- Inversé : {phrase_inversee}")
# Mots séparés par " | "
mots = phrase.split()
mots_separes = liste_to_string(mots, " | ")
print(f"- Mots : {mots_separes}")   

# Exemple d'exécution :
# Entrez une phrase : Python est cool
phraseP = "Python est cool"
print("\nAnalyse de votre phrase :")
# Palindrome
if est_palindrome(phraseP):
    print("- Palindrome : Oui ✓")
else:
    print("- Palindrome : Non ✗")
# Nombre de voyelles
nb_voyelles = compter_voyelles(phraseP)
print(f"- Nombre de voyelles : {nb_voyelles}")
# Phrase inversée  
phrase_inversee = inverser_chaine(phraseP)
print(f"- Inversé : {phrase_inversee}")
# Mots séparés par " | "
mots = phraseP.split()
mots_separes = liste_to_string(mots, " | ")
print(f"- Mots : {mots_separes}")

# Analyse de votre phrase :
# - Palindrome : Non
# - Nombre de voyelles : 4
# - Inversé : looc tse nohtyP
# - Mots : Python | est | cool

print("📝 À vous de jouer ! Décommentez et complétez le code ci-dessous :\n")

def analyser_phrase():
    """Analyse une phrase avec les fonctions du module utils"""
    from utils import est_palindrome, compter_voyelles, inverser_chaine, liste_to_string
#
    # TODO: Demander une phrase à l'utilisateur
    phrase = input("Entrez une phrase : ")
    # TODO: Analyser et afficher les résultats
    print("\nAnalyse de votre phrase :")
    # Palindrome
    if est_palindrome(phrase):
        print("- Palindrome : Oui ✓")
    else:
        print("- Palindrome : Non ✗")
    # Nombre de voyelles
    nb_voyelles = compter_voyelles(phrase)
    print(f"- Nombre de voyelles : {nb_voyelles}")
    # Phrase inversée  
    phrase_inversee = inverser_chaine(phrase)
    print(f"- Inversé : {phrase_inversee}")
    # Mots séparés par " | "
    mots = phrase.split()
    mots_separes = liste_to_string(mots, " | ")
    print(f"- Mots : {mots_separes}")  

if __name__ == "__main__":
    analyser_phrase()

# TODO: Créer un fichier utils.py dans le même dossier avec les fonctions suivantes :
#
# 1. est_pair(nombre) -> bool
#    Retourne True si le nombre est pair
def est_pair(nombre):
    """Retourne True si le nombre est pair"""
    return nombre % 2 == 0 

# 2. est_palindrome(texte) -> bool
#    Retourne True si le texte est un palindrome (ignore les espaces et la casse)
#    Exemples : "radar", "Kayak", "La mariée ira mal"
def est_palindrome(texte):
    """Retourne True si le texte est un palindrome (ignore les espaces et la casse)"""
    texte_nettoye = ''.join(texte.split()).lower()
    return texte_nettoye == texte_nettoye[::-1]

# 3. compter_voyelles(texte) -> int
#    Compte le nombre de voyelles dans le texte
def compter_voyelles(texte):
    """Compte le nombre de voyelles dans le texte"""
    voyelles = "aeiouyAEIOUY"
    return sum(1 for char in texte if char in voyelles)

# 4. inverser_chaine(texte) -> str
#    Retourne le texte inversé
def inverser_chaine(texte):
    """Retourne le texte inversé"""
    return texte[::-1]

# 5. liste_to_string(liste, separateur=", ") -> str
#    Convertit une liste en chaîne avec séparateur
#    Exemple : [1, 2, 3] -> "1, 2, 3"
def liste_to_string(liste, separateur=", "):
    """Convertit une liste en chaîne avec séparateur"""
    return separateur.join(str(item) for item in liste)

# N'oubliez pas d'ajouter :
#   - Des docstrings pour chaque fonction
#   - Un bloc if __name__ == "__main__": avec des tests
#   - Des commentaires explicatifs
if __name__ == "__main__":
    # Tests des fonctions
    print("Tests du module utils.py\n")

    # Test est_pair
    print("Test est_pair:")
    for nb in [10, 15, 22, 7, 100]:
        print(f"  {nb} est pair: {est_pair(nb)}")

    # Test est_palindrome
    print("\nTest est_palindrome:")
    for mot in ["radar", "Python", "Kayak", "La mariée ira mal"]:
        print(f"  '{mot}' est un palindrome: {est_palindrome(mot)}")

    # Test compter_voyelles
    print("\nTest compter_voyelles:")
    textes = ["Bonjour le monde", "Python", "Formation CMA"]
    for texte in textes:
        print(f"  '{texte}' contient {compter_voyelles(texte)} voyelles")

    # Test inverser_chaine
    print("\nTest inverser_chaine:")
    for texte in ["Bonjour", "Python", "Formation"]:
        print(f"  '{texte}' inversé est '{inverser_chaine(texte)}'")

    # Test liste_to_string
    print("\nTest liste_to_string:")
    listes = [[1, 2, 3], ['a', 'b', 'c'], [True, False, True]]
    for lst in listes:
        print(f"  Liste {lst} convertie en chaîne: '{liste_to_string(lst)}'")
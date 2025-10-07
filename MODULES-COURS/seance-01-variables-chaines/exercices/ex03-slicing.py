"""
Exercice 3 : Slicing et Indexation
Objectif : Maîtriser l'accès et le découpage des chaînes
"""

print("=== EXERCICE 3 : SLICING ET INDEXATION ===")

# Chaîne de travail
texte = "PythonProgramming"

# TODO: Accédez au premier caractère
premier = texte[0]
print(f"1. Premier caractère : '{premier}'")

# TODO: Accédez au dernier caractère
dernier = texte[-1]
print(f"2. Dernier caractère : '{dernier}'")

# TODO: Accédez au 5ème caractère
cinquieme = texte[4]
print(f"3. Cinquième caractère : '{cinquieme}'")

# TODO: Extrayez "Python" (6 premiers caractères)
python_part = texte[:6]
print(f"4. 'Python' : '{python_part}'")

# TODO: Extrayez "Programming" (à partir du 7ème caractère)
programming_part = texte[6:]
print(f"5. 'Programming' : '{programming_part}'")

# TODO: Extrayez "Program" (caractères 7 à 13)
program_part = texte[6:13]
print(f"6. 'Program' : '{program_part}'")

# TODO: Extrayez tous les 2 caractères
un_sur_deux = texte[::2]
print(f"7. Un caractère sur deux : '{un_sur_deux}'")

# TODO: Inversez la chaîne
inverse = texte[::-1]
print(f"8. Chaîne inversée : '{inverse}'")

# TODO: Extrayez les 3 derniers caractères
trois_derniers = texte[-3:]
print(f"9. Trois derniers caractères : '{trois_derniers}'")

# TODO: Exercice pratique - Formatez un numéro de téléphone
telephone = "0123456789"
telephone_formate = f"+33 {telephone[1:3]} {telephone[3:5]} {telephone[5:7]} {telephone[7:9]} {telephone[9:]}"
print(f"10. Téléphone formaté : {telephone_formate}")

# TODO: Défi - Extrayez le mot du milieu d'une phrase
phrase = "Python est un langage formidable"
mots = phrase.split()
mot_du_milieu = mots[len(mots)//2]
print(f"11. Mot du milieu : '{mot_du_milieu}'")

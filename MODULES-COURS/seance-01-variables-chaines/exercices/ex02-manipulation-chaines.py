"""
Exercice 2 : Manipulation de Chaînes
Objectif : Maîtriser les méthodes de manipulation de texte
"""

print("=== EXERCICE 2 : MANIPULATION DE CHAÎNES ===")

# Chaîne de travail
texte = "  Python est un langage de programmation incroyable!  "

# TODO: Enlevez les espaces au début et à la fin
texte_propre = texte.strip()
print(f"1. Texte nettoyé : '{texte_propre}'")

# TODO: Mettez tout en majuscules
texte_majuscules = texte_propre.upper()
print(f"2. En majuscules : {texte_majuscules}")

# TODO: Mettez tout en minuscules
texte_minuscules = texte_propre.lower()
print(f"3. En minuscules : {texte_minuscules}")

# TODO: Capitalisez (première lettre en majuscule)
texte_capitalise = texte_propre.capitalize()
print(f"4. Capitalisé : {texte_capitalise}")

# TODO: Comptez combien de fois 'a' apparaît
nombre_a = texte_propre.count('a')
print(f"5. Nombre de 'a' : {nombre_a}")

# TODO: Trouvez la position du mot 'langage'
position_langage = texte_propre.find('langage')
print(f"6. Position de 'langage' : {position_langage}")

# TODO: Remplacez 'incroyable' par 'fantastique'
texte_remplace = texte_propre.replace('incroyable', 'fantastique')
print(f"7. Après remplacement : {texte_remplace}")

# TODO: Séparez la phrase en mots
mots = texte_propre.split()
print(f"8. Mots séparés : {mots}")

# TODO: Recréez la phrase avec des tirets entre les mots
phrase_tirets = "-".join(mots)
print(f"9. Avec tirets : {phrase_tirets}")

# TODO: Vérifiez si la phrase contient 'programmation'
contient_programmation = 'programmation' in texte_propre
print(f"10. Contient 'programmation' : {contient_programmation}")

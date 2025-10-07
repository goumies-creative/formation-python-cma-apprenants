# Variables Avancées et Types de Données

## Objectifs

- Comprendre les différents types de variables en Python
- Savoir quand utiliser chaque type
- Maîtriser les conversions entre types
- Utiliser les listes et dictionnaires pour organiser les données

## Les Variables en Python

### Qu'est-ce qu'une variable ?
Une variable est comme une **boîte étiquetée** qui contient une valeur.

```python
# Assignation simple
nom = "Marie"
age = 25
taille = 1.65
est_etudiant = True
```

### Règles de nommage
```python
#  Bonnes pratiques 
nom_complet = "Marie Dupont"  # snake_case
age_utilisateur = 25
est_actif = True

# À éviter
NomComplet = "Marie Dupont"   # PascalCase pour les classes
AGEUTILISATEUR = 25           # MAJUSCULES pour les constantes
x = "Marie"                   # Trop vague
```

## Types de Données de Base
### Nombres
```python
# Entiers (int)
age = 25
annee = 2025
quantite = -10

# Nombres à virgule (float)
prix = 19.99
temperature = -5.5
pourcentage = 0.75

# Opérations
somme = 10 + 5           # 15
division = 10 / 3        # 3.333...
division_entiere = 10 // 3  # 3
reste = 10 % 3           # 1
puissance = 2 ** 3       # 8
```

### Texte
```python
# Chaînes de caractères
nom = "Marie"
prenom = 'Jean'
message = "Hello World!"

# Chaînes multilignes
description = """
Ceci est une description
sur plusieurs lignes
"""
```

### Booléens
```python
# Valeurs booléennes
est_vrai = True
est_faux = False

# Expressions booléennes
est_majeur = age >= 18
est_egal = (10 == 10)      # True
est_different = (10 != 5)  # True
```

## Collections de Données
### Listes
```python
# Création de liste
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = [1, "texte", True, 3.14]

# Accès aux éléments
premier_fruit = fruits[0]     # "pomme"
dernier_fruit = fruits[-1]    # "orange"

# Modification
fruits[1] = "kiwi"           # Remplace "banane" par "kiwi"
fruits.append("fraise")       # Ajoute à la fin
```

### Dictionnaires
```python
# Création de dictionnaire
personne = {
    "nom": "Dupont",
    "prenom": "Marie",
    "age": 25,
    "ville": "Paris"
}

# Accès aux valeurs
nom_personne = personne["nom"]        # "Dupont"
age_personne = personne.get("age")    # 25

# Modification
personne["age"] = 26
personne["metier"] = "Développeuse"   # Ajoute une nouvelle clé
```

## Conversion entre Types
### Conversions courantes
```python
# str vers int
texte_nombre = "25"
nombre = int(texte_nombre)    # 25

# int vers str
age = 25
texte_age = str(age)          # "25"

# float vers int
prix = 19.99
prix_entier = int(prix)       # 19 (troncature)

# bool vers int
vrai = int(True)              # 1
faux = int(False)             # 0
```

### Vérification des types
```python
age = 25
nom = "Marie"

print(type(age))    # <class 'int'>
print(type(nom))    # <class 'str'>

# Vérifications
print(isinstance(age, int))    # True
print(isinstance(nom, str))    # True
```

## Bonnes Pratiques
### Noms significatifs
```python
# ✅ Clair et explicite
nombre_utilisateurs = 150
liste_emails = ["a@b.com", "c@d.com"]
est_connecte = True

# ❌ Confus ou vague
n = 150
l = ["a@b.com", "c@d.com"]
flag = True
```

### Constantes
```python
# En MAJUSCULES pour les constantes
TAUX_TVA = 0.20
PI = 3.14159
NOM_APPLICATION = "MonApp"
```


### Initialisation multiple
```python
# Assignation multiple
x, y, z = 1, 2, 3

# Même valeur à plusieurs variables
a = b = c = 0

# Échange de valeurs
x, y = y, x
```

## Exercices Pratiques
### Exercice 1 : Création de Variables
```python
# Créez des variables pour décrire un livre
titre = "Python pour les débutants"
auteur = "Marie Curie"
annee_publication = 2024
prix = 29.99
est_disponible = True
nombre_pages = 350
```

### Exercice 2 : Liste d'étudiants
```python
# Créez une liste d'étudiants
etudiants = ["Alice", "Bob", "Charlie", "Diana"]

# Ajoutez un étudiant
etudiants.append("Émilie")

# Modifiez le deuxième étudiant
etudiants[1] = "Benjamin"

# Affichez la liste
print("Liste des étudiants:", etudiants)
```

Exercice 3 : Dictionnaire produit
```python
# Créez un dictionnaire pour un produit
produit = {
    "nom": "Ordinateur portable",
    "marque": "TechCorp",
    "prix": 999.99,
    "en_stock": True
}

# Affichez les informations
print(f"Produit: {produit['nom']}")
print(f"Prix: {produit['prix']}€")
print(f"En stock: {produit['en_stock']}")
```

## Pièges Courants
### Erreurs de type
```python
# Mauvais
age = "25"
age_plus_un = age + 1  # Erreur!

# Correct
age = int("25")
age_plus_un = age + 1  # 26
```

### Noms réservés
```python
# Ne pas utiliser les mots réservés
class = "MaClasse"     # Erreur!
def = "ma_fonction"    # Erreur!

# Utiliser des alternatives
classe = "MaClasse"
definition = "ma_fonction"
```

## Checklist de Maîtrise
- Je sais créer des variables avec des noms significatifs
- Je connais les différences entre int, float, str, bool
- Je peux utiliser les listes pour stocker plusieurs valeurs
- Je sais utiliser les dictionnaires pour des données structurées
- Je maîtrise les conversions entre types
- J'évite les pièges courants avec les types

**Les variables sont les briques de base de tous vos programmes !**
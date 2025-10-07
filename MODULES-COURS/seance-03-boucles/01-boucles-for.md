# Boucles For - Itération sur Séquences

## Objectifs

- Comprendre le concept d'itération
- Maîtriser la boucle for avec différentes séquences
- Utiliser range() pour générer des séquences numériques
- Parcourir efficacement listes, strings et dictionnaires

## Concept d'Itération

### Qu'est-ce qu'une itération ?
L'itération consiste à **parcourir un à un** les éléments d'une séquence.

```python
# Sans boucle (fastidieux)
fruits = ["pomme", "banane", "orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

# Avec boucle (efficace)
for fruit in fruits:
    print(fruit)
```

## Syntaxe de Base
### Structure for
```python
for element in sequence:
    # Code exécuté pour chaque élément
    print(element)
```

### Exemples avec différents types
```python
# Liste
nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
    print(nombre * 2)

# String
mot = "Python"
for lettre in mot:
    print(lettre.upper())

# Tuple
coordonnees = (10, 20, 30)
for coord in coordonnees:
    print(coord)
```

## La Fonction range()
### Générer des séquences numériques
```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Compte à rebours
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

## Parcours Avancé
### Avec enumerate() - index et valeur
```python
fruits = ["pomme", "banane", "orange"]

for index, fruit in enumerate(fruits):
    print(f"Index {index} : {fruit}")
# Index 0 : pomme
# Index 1 : banane  
# Index 2 : orange
```

### Parcours de dictionnaires
```python
personne = {"nom": "Dupont", "age": 25, "ville": "Paris"}

# Clés seulement
for cle in personne:
    print(cle)

# Valeurs seulement
for valeur in personne.values():
    print(valeur)

# Clés et valeurs
for cle, valeur in personne.items():
    print(f"{cle} : {valeur}")
```


## Patterns Courants
### Accumulation
```python
# Somme des éléments
nombres = [1, 2, 3, 4, 5]
somme = 0

for nombre in nombres:
    somme += nombre

print(f"Somme : {somme}")  # 15
```

### Recherche
```python
# Trouver un élément
fruits = ["pomme", "banane", "orange"]
fruit_cherche = "banane"
trouve = False

for fruit in fruits:
    if fruit == fruit_cherche:
        trouve = True
        break

print(f"{fruit_cherche} trouvé : {trouve}")
```

### Filtrage
```python
# Nombres pairs seulement
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = []

for nombre in nombres:
    if nombre % 2 == 0:
        nombres_pairs.append(nombre)

print(f"Nombres pairs : {nombres_pairs}")  # [2, 4, 6, 8, 10]
```

##  Exercices Pratiques
### Exercice 1 : Table de multiplication
```python
nombre = int(input("Entrez un nombre : "))

print(f"Table de multiplication de {nombre}:")
for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")
```

### Exercice 2 : Compteur de voyelles
```python
texte = input("Entrez un texte : ")
voyelles = "aeiouyAEIOUY"
compteur = 0

for lettre in texte:
    if lettre in voyelles:
        compteur += 1

print(f"Nombre de voyelles : {compteur}")
```

### Exercice 2 : Compteur de voyelles
```python
texte = input("Entrez un texte : ")
voyelles = "aeiouyAEIOUY"
compteur = 0

for lettre in texte:
    if lettre in voyelles:
        compteur += 1

print(f"Nombre de voyelles : {compteur}")
```

### Exercice 3 : Liste d'étudiants avec notes
```python
etudiants = ["Alice", "Bob", "Charlie"]
notes = [15, 12, 18]

print("Bulletin de notes :")
for i, (etudiant, note) in enumerate(zip(etudiants, notes), 1):
    mention = "Excellent" if note >= 16 else "Très bien" if note >= 14 else "Bien" if note >= 12 else "Passable"
    print(f"{i}. {etudiant} : {note}/20 - {mention}")
```

## Pièges Courants
### Modification pendant l'itération
```python
# Dangereux
nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
    if nombre % 2 == 0:
        nombres.remove(nombre)  # Comportement imprévisible

# Sécurisé
nombres = [1, 2, 3, 4, 5]
nombres_filtres = []
for nombre in nombres:
    if nombre % 2 != 0:
        nombres_filtres.append(nombre)
```

### Oubli de l'indentation
```python
# ❌ Erreur d'indentation
for i in range(5):
print(i)  # IndentationError

# ✅ Correct
for i in range(5):
    print(i)
```

## Checklist de Maîtrise
- Je maîtrise la syntaxe de base de for
- Je sais utiliser range() pour générer des séquences
- Je peux parcourir listes, strings et dictionnaires
- J'utilise enumerate() pour avoir index et valeur
- Je connais les patterns courants (accumulation, recherche, filtrage)
- J'évite les pièges des modifications pendant l'itération

**Les boucles for transforment la répétition fastidieuse en élégance algorithmique !**
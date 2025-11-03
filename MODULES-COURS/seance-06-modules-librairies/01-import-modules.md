# Import et Modules Python

## Objectifs

- Comprendre le système d'import de Python
- Maîtriser les différentes syntaxes d'import
- Explorer la bibliothèque standard
- Utiliser des modules essentiels (random, datetime, os, sys)

## Introduction / Métaphore

### La Bibliothèque de Code

Imaginez une immense bibliothèque avec des milliers de livres (modules). Chaque livre contient des recettes de code (fonctions et classes) déjà écrites et testées par d'autres développeurs.

**Sans modules :** Vous devez réécrire chaque recette à chaque fois.
**Avec modules :** Vous empruntez le livre et utilisez directement les recettes.

```python
# Sans module : réinventer la roue
def generer_nombre_aleatoire(min, max):
    # Code complexe avec timestamp, algorithmes...
    pass

# Avec module : simple et efficace
import random
nombre = random.randint(1, 100)
```

## Concept Fondamental : Qu'est-ce qu'un Module ?

### Définition

Un **module** est simplement un fichier Python (.py) contenant du code réutilisable : fonctions, classes, variables.

### Types de Modules

1. **Bibliothèque standard** : Fournis avec Python (random, datetime, os...)
2. **Packages externes** : Installables via pip (requests, pandas, flask...)
3. **Modules personnalisés** : Créés par vous

## Syntaxe d'Import

### 1. Import Simple

```python
# Importer un module complet
import random

# Utilisation avec préfixe
nombre = random.randint(1, 100)
choix = random.choice(['rouge', 'vert', 'bleu'])
```

### 2. Import Spécifique

```python
# Importer uniquement certaines fonctions
from random import randint, choice

# Utilisation directe (sans préfixe)
nombre = randint(1, 100)
couleur = choice(['rouge', 'vert', 'bleu'])
```

### 3. Import avec Alias

```python
# Créer un raccourci (alias)
import datetime as dt

# Utilisation avec alias court
maintenant = dt.datetime.now()
```

### 4. Import Multiple

```python
# Importer plusieurs éléments
from random import randint, choice, shuffle

# Importer tout (⚠️ à éviter en général)
from random import *
```

## Exemples Progressifs

### Exemple 1 : Module random

```python
import random

# 1. Nombre aléatoire entier
de = random.randint(1, 6)
print(f"Lancer de dé : {de}")

# 2. Nombre aléatoire décimal
temperature = random.uniform(15.0, 30.0)
print(f"Température : {temperature:.1f}°C")

# 3. Choix aléatoire dans une liste
couleurs = ['rouge', 'vert', 'bleu', 'jaune']
couleur = random.choice(couleurs)
print(f"Couleur choisie : {couleur}")

# 4. Mélanger une liste
cartes = ['As', 'Roi', 'Dame', 'Valet', '10']
random.shuffle(cartes)
print(f"Cartes mélangées : {cartes}")

# 5. Échantillon aléatoire
participants = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
gagnants = random.sample(participants, 2)
print(f"Gagnants du tirage : {gagnants}")
```

### Exemple 2 : Module datetime

```python
from datetime import datetime, date, timedelta

# 1. Date et heure actuelles
maintenant = datetime.now()
print(f"Maintenant : {maintenant}")
print(f"Date : {maintenant.date()}")
print(f"Heure : {maintenant.time()}")

# 2. Formatage de dates
date_str = maintenant.strftime("%d/%m/%Y à %H:%M")
print(f"Formaté : {date_str}")

# 3. Date spécifique
noel = datetime(2025, 12, 25)
jours_restants = (noel - maintenant).days
print(f"Jours avant Noël : {jours_restants}")

# 4. Opérations sur dates
hier = datetime.now() - timedelta(days=1)
dans_une_semaine = datetime.now() + timedelta(weeks=1)
print(f"Hier : {hier.strftime('%d/%m/%Y')}")
print(f"Dans une semaine : {dans_une_semaine.strftime('%d/%m/%Y')}")

# 5. Âge à partir d'une date de naissance
naissance = date(1990, 5, 15)
aujourd_hui = date.today()
age = aujourd_hui.year - naissance.year
print(f"Âge : {age} ans")
```

### Exemple 3 : Module os (système)

```python
import os

# 1. Répertoire courant
print(f"Répertoire actuel : {os.getcwd()}")

# 2. Lister les fichiers
fichiers = os.listdir('.')
print(f"Fichiers : {fichiers[:5]}")  # 5 premiers

# 3. Vérifier l'existence
if os.path.exists('mon_fichier.txt'):
    print("Le fichier existe")
else:
    print("Le fichier n'existe pas")

# 4. Informations système
print(f"Système : {os.name}")  # 'nt' pour Windows, 'posix' pour Linux/Mac

# 5. Chemins
chemin = os.path.join('dossier', 'sous_dossier', 'fichier.txt')
print(f"Chemin : {chemin}")
```

## Patterns Courants

### Pattern 1 : Jeu de Dés

```python
import random

def lancer_des(nombre_des=2):
    """Lance plusieurs dés et retourne résultats et total"""
    resultats = [random.randint(1, 6) for _ in range(nombre_des)]
    total = sum(resultats)
    return resultats, total

# Utilisation
des, total = lancer_des(3)
print(f"Résultats : {des}")
print(f"Total : {total}")
```

### Pattern 2 : Calcul d'Âge Précis

```python
from datetime import date

def calculer_age(date_naissance):
    """Calcule l'âge précis à partir d'une date de naissance"""
    aujourd_hui = date.today()
    age = aujourd_hui.year - date_naissance.year

    # Vérifier si anniversaire pas encore passé cette année
    anniversaire_passe = (aujourd_hui.month, aujourd_hui.day) >= \
                         (date_naissance.month, date_naissance.day)

    if not anniversaire_passe:
        age -= 1

    return age

# Utilisation
naissance = date(1995, 8, 20)
age = calculer_age(naissance)
print(f"Âge : {age} ans")
```

### Pattern 3 : Timer / Chronomètre

```python
import time
from datetime import datetime

def chronometrer(fonction):
    """Mesure le temps d'exécution d'une fonction"""
    debut = time.time()
    resultat = fonction()
    fin = time.time()
    duree = fin - debut
    print(f"Temps d'exécution : {duree:.3f} secondes")
    return resultat

# Exemple d'utilisation
def tache_longue():
    total = 0
    for i in range(1000000):
        total += i
    return total

chronometrer(tache_longue)
```

## La Bibliothèque Standard : Modules Essentiels

### random - Nombres aléatoires
```python
import random

random.randint(1, 10)           # Entier aléatoire
random.random()                 # Décimal entre 0 et 1
random.choice(liste)            # Élément aléatoire
random.shuffle(liste)           # Mélanger
random.sample(liste, k)         # k éléments aléatoires uniques
```

### datetime - Dates et heures
```python
from datetime import datetime, date, timedelta

datetime.now()                  # Date et heure actuelles
date.today()                    # Date du jour
timedelta(days=7)              # Durée de 7 jours
datetime.strftime('%d/%m/%Y')  # Formater
```

### math - Mathématiques
```python
import math

math.sqrt(16)      # Racine carrée : 4.0
math.pi            # Constante π : 3.14159...
math.ceil(4.3)     # Arrondi supérieur : 5
math.floor(4.8)    # Arrondi inférieur : 4
math.pow(2, 3)     # Puissance : 8.0
```

### os - Système d'exploitation
```python
import os

os.getcwd()                    # Répertoire courant
os.listdir('.')               # Liste des fichiers
os.path.exists('fichier.txt')  # Vérifier existence
os.path.join('a', 'b')        # Construire chemin
```

### sys - Paramètres système
```python
import sys

sys.version        # Version de Python
sys.platform       # Plateforme (win32, linux, darwin)
sys.argv           # Arguments ligne de commande
sys.exit()         # Quitter le programme
```

## Exercice Pratique : Simulateur de Dés

```python
import random
from datetime import datetime

def simulateur_des():
    """Simulateur de jeu de dés avec statistiques"""
    print("🎲 SIMULATEUR DE DÉS 🎲")
    print("=" * 40)

    resultats = []

    while True:
        input("\nAppuyez sur Entrée pour lancer les dés (ou 'q' pour quitter)...")

        # Lancer 2 dés
        de1 = random.randint(1, 6)
        de2 = random.randint(1, 6)
        total = de1 + de2

        # Enregistrer et afficher
        resultats.append(total)
        heure = datetime.now().strftime("%H:%M:%S")

        print(f"[{heure}] Dé 1: {de1} | Dé 2: {de2} | Total: {total}")

        # Statistiques
        if len(resultats) >= 3:
            moyenne = sum(resultats) / len(resultats)
            maximum = max(resultats)
            minimum = min(resultats)
            print(f"\n📊 Stats: Moyenne={moyenne:.1f} | Max={maximum} | Min={minimum}")

# Lancer le simulateur
simulateur_des()
```

## Pièges Courants

### Erreur 1 : Nom de fichier conflictuel
```python
# ❌ Ne jamais nommer votre fichier "random.py"
# Cela cache le module random de Python !

# Si votre fichier s'appelle random.py :
import random  # Import VOTRE fichier au lieu du module Python !

# ✅ Utilisez des noms descriptifs
# mon_jeu.py, calculateur.py, etc.
```

### Erreur 2 : Import circulaire
```python
# ❌ fichier_a.py
from fichier_b import fonction_b

def fonction_a():
    return "A"

# ❌ fichier_b.py
from fichier_a import fonction_a

def fonction_b():
    return "B"

# ✅ Restructurer pour éviter les imports circulaires
```

### Erreur 3 : Oublier d'importer
```python
# ❌ Erreur
nombre = randint(1, 10)  # NameError: name 'randint' is not defined

# ✅ Correct
from random import randint
nombre = randint(1, 10)
```

### Erreur 4 : Import * (wildcard)
```python
# ⚠️ Éviter (pollue l'espace de noms)
from random import *
from datetime import *

# ✅ Préférer les imports explicites
from random import randint, choice
from datetime import datetime, date
```

## Checklist de Maîtrise

- [ ] Je comprends ce qu'est un module
- [ ] Je sais utiliser import, from...import, et as
- [ ] Je peux utiliser random pour générer des nombres aléatoires
- [ ] Je peux manipuler des dates avec datetime
- [ ] Je connais les modules essentiels de la bibliothèque standard
- [ ] Je sais éviter les conflits de noms de fichiers
- [ ] Je comprends quand utiliser chaque syntaxe d'import

**Les modules sont votre superpouvoir ! Ne codez jamais quelque chose qui existe déjà dans la bibliothèque standard.**

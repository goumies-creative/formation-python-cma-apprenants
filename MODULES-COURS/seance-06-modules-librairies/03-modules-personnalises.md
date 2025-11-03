# Créer ses Propres Modules

## Objectifs

- Créer des modules Python personnalisés
- Structurer un projet multi-fichiers
- Comprendre `__name__` et `__main__`
- Organiser son code de façon professionnelle
- Créer des packages Python

## Introduction / Métaphore

### La Boîte à Outils Personnalisée

Imaginez un menuisier qui fabrique souvent les mêmes types de meubles. Au lieu de chercher ses outils à chaque fois, il crée une **boîte à outils personnalisée** avec tout ce dont il a besoin.

**Modules personnalisés** = Votre boîte à outils de fonctions réutilisables

```python
# Sans module : copier-coller le code partout
# fichier1.py
def valider_email(email):
    return '@' in email

# fichier2.py
def valider_email(email):  # Code dupliqué !
    return '@' in email

# ===================================

# Avec module : une seule source de vérité
# utils.py
def valider_email(email):
    return '@' in email

# fichier1.py
from utils import valider_email

# fichier2.py
from utils import valider_email
```

## Concept Fondamental : Qu'est-ce qu'un Module Personnalisé ?

### Définition Simple

**Un module** = Un fichier Python (.py) que vous créez et que vous importez dans d'autres fichiers.

### Anatomie d'un Module

```python
# mon_module.py
"""
Documentation du module : Fonctions utilitaires
"""

# Variables du module
VERSION = "1.0.0"

# Fonctions du module
def ma_fonction():
    """Fait quelque chose"""
    return "Hello"

# Classes du module
class MaClasse:
    """Représente quelque chose"""
    pass

# Code exécuté à l'import
print(f"Module chargé (version {VERSION})")
```

## Créer un Premier Module

### Étape 1 : Créer le fichier module

```python
# calculatrice.py
"""
Module de calculs mathématiques simples
"""

def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

def soustraire(a, b):
    """Soustrait b de a"""
    return a - b

def multiplier(a, b):
    """Multiplie deux nombres"""
    return a * b

def diviser(a, b):
    """Divise a par b"""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

# Constante
PI = 3.14159
```

### Étape 2 : Utiliser le module

```python
# main.py (dans le même dossier que calculatrice.py)
import calculatrice

# Utilisation des fonctions
resultat = calculatrice.additionner(5, 3)
print(f"5 + 3 = {resultat}")

print(f"10 * 2 = {calculatrice.multiplier(10, 2)}")
print(f"Valeur de PI : {calculatrice.PI}")
```

### Étape 3 : Import sélectif

```python
# main.py
from calculatrice import additionner, multiplier, PI

# Utilisation directe (sans préfixe)
print(additionner(5, 3))
print(multiplier(10, 2))
print(PI)
```

## Le Mystère de `__name__` et `__main__`

### Le Problème

```python
# utils.py
def dire_bonjour():
    print("Bonjour !")

# Test lors du développement
dire_bonjour()  # Problème : s'exécute aussi quand on importe !
```

```python
# main.py
import utils  # Affiche "Bonjour !" alors qu'on ne voulait pas !
```

### La Solution : `if __name__ == "__main__"`

```python
# utils.py
def dire_bonjour():
    print("Bonjour !")

# Ce code NE s'exécute QUE si on lance directement utils.py
if __name__ == "__main__":
    print("Test du module utils.py")
    dire_bonjour()
```

**Explication :**
- Si vous lancez `python utils.py` → `__name__` vaut `"__main__"` → le code s'exécute
- Si vous faites `import utils` → `__name__` vaut `"utils"` → le code ne s'exécute pas

### Pattern Standard

```python
# mon_module.py
"""Documentation du module"""

def fonction1():
    """Fonction exportée"""
    pass

def fonction2():
    """Autre fonction exportée"""
    pass

def _fonction_privee():
    """Fonction privée (convention _)"""
    pass

# Tests et exemples (uniquement si lancé directement)
if __name__ == "__main__":
    print("🧪 Tests du module...")
    fonction1()
    fonction2()
    print("✅ Tests terminés")
```

## Exemples Progressifs

### Exemple 1 : Module utils.py Simple

```python
# utils.py
"""Fonctions utilitaires diverses"""

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0

def est_palindrome(texte):
    """Vérifie si un texte est un palindrome"""
    texte_nettoye = texte.lower().replace(' ', '')
    return texte_nettoye == texte_nettoye[::-1]

def compter_voyelles(texte):
    """Compte le nombre de voyelles dans un texte"""
    voyelles = 'aeiouyAEIOUY'
    return sum(1 for char in texte if char in voyelles)

# Tests
if __name__ == "__main__":
    print(est_pair(10))  # True
    print(est_palindrome("Radar"))  # True
    print(compter_voyelles("Hello World"))  # 3
```

```python
# main.py
from utils import est_pair, est_palindrome, compter_voyelles

nombre = 15
if est_pair(nombre):
    print(f"{nombre} est pair")
else:
    print(f"{nombre} est impair")

mot = "kayak"
if est_palindrome(mot):
    print(f"'{mot}' est un palindrome !")
```

### Exemple 2 : Module validation.py

```python
# validation.py
"""Module de validation de données"""

import re

def valider_email(email):
    """Valide le format d'un email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def valider_telephone(tel):
    """Valide un numéro de téléphone français"""
    # Format : 06 12 34 56 78 ou 0612345678
    tel_nettoye = tel.replace(' ', '').replace('.', '')
    return len(tel_nettoye) == 10 and tel_nettoye.startswith('0')

def valider_code_postal(code):
    """Valide un code postal français"""
    return len(code) == 5 and code.isdigit()

def valider_age(age):
    """Valide un âge (entre 0 et 120)"""
    try:
        age_int = int(age)
        return 0 <= age_int <= 120
    except ValueError:
        return False

# Tests
if __name__ == "__main__":
    print("Tests de validation...")

    emails = ["test@example.com", "invalid.email", "user@domain.co"]
    for email in emails:
        print(f"{email}: {valider_email(email)}")

    tels = ["06 12 34 56 78", "0612345678", "123"]
    for tel in tels:
        print(f"{tel}: {valider_telephone(tel)}")
```

### Exemple 3 : Module stats.py avec Classe

```python
# stats.py
"""Module de statistiques simples"""

class Statistiques:
    """Calculateur de statistiques sur une liste de nombres"""

    def __init__(self, donnees):
        """Initialise avec une liste de nombres"""
        self.donnees = donnees

    def moyenne(self):
        """Calcule la moyenne"""
        if not self.donnees:
            return 0
        return sum(self.donnees) / len(self.donnees)

    def minimum(self):
        """Retourne le minimum"""
        return min(self.donnees) if self.donnees else None

    def maximum(self):
        """Retourne le maximum"""
        return max(self.donnees) if self.donnees else None

    def etendue(self):
        """Calcule l'étendue (max - min)"""
        if not self.donnees:
            return 0
        return self.maximum() - self.minimum()

    def resume(self):
        """Affiche un résumé des statistiques"""
        print(f"📊 Statistiques sur {len(self.donnees)} valeurs")
        print(f"   Moyenne : {self.moyenne():.2f}")
        print(f"   Min     : {self.minimum()}")
        print(f"   Max     : {self.maximum()}")
        print(f"   Étendue : {self.etendue()}")

# Tests
if __name__ == "__main__":
    notes = [12, 15, 8, 18, 14, 11, 16]
    stats = Statistiques(notes)
    stats.resume()
```

```python
# main.py
from stats import Statistiques

notes_eleves = [12, 15, 8, 18, 14, 11, 16, 13, 17, 9]
stats = Statistiques(notes_eleves)

print(f"Moyenne de la classe : {stats.moyenne():.2f}/20")
print(f"Meilleure note : {stats.maximum()}/20")
print(f"Note la plus basse : {stats.minimum()}/20")
```

## Structurer un Projet Multi-Fichiers

### Structure Simple

```
mon_projet/
├── main.py              # Point d'entrée principal
├── utils.py             # Fonctions utilitaires
├── validation.py        # Fonctions de validation
└── stats.py             # Module de statistiques
```

### Structure Professionnelle

```
mon_projet/
├── main.py              # Point d'entrée
├── src/                 # Code source
│   ├── __init__.py      # Marque src comme package
│   ├── utils.py
│   ├── validation.py
│   └── stats.py
├── tests/               # Tests unitaires
│   ├── test_utils.py
│   └── test_validation.py
├── requirements.txt     # Dépendances
└── README.md           # Documentation
```

### Créer un Package Python

```python
# src/__init__.py
"""
Package principal de mon_projet
"""

__version__ = "1.0.0"
__author__ = "Votre Nom"

# Importer les modules principaux pour faciliter l'import
from .utils import est_pair, est_palindrome
from .validation import valider_email
from .stats import Statistiques

# __all__ définit ce qui est exporté avec "from src import *"
__all__ = [
    'est_pair',
    'est_palindrome',
    'valider_email',
    'Statistiques'
]
```

```python
# main.py
# Au lieu de :
# from src.utils import est_pair
# from src.stats import Statistiques

# On peut faire :
from src import est_pair, Statistiques

notes = [15, 12, 18]
stats = Statistiques(notes)
print(stats.moyenne())
```

## Bonnes Pratiques

### 1. Nommer les Modules

```python
# ✅ Bon : noms descriptifs, snake_case
utils.py
validation_donnees.py
calcul_statistiques.py

# ❌ Éviter : noms génériques ou conflictuels
test.py          # Conflit avec module test de Python
random.py        # Conflit avec module random !
MaClasse.py      # Pas de CamelCase pour les modules
```

### 2. Documenter les Modules

```python
# mon_module.py
"""
Module de traitement de données.

Ce module fournit des fonctions pour :
- Nettoyer les données
- Valider les entrées
- Calculer des statistiques

Exemple d'utilisation :
    from mon_module import nettoyer_donnees

    donnees = nettoyer_donnees(raw_data)
"""

def ma_fonction(param):
    """
    Description courte de la fonction.

    Args:
        param (type): Description du paramètre

    Returns:
        type: Description de ce qui est retourné

    Raises:
        ValueError: Si param est invalide
    """
    pass
```

### 3. Séparer Logique Métier et Tests

```python
# ✅ Bon
# utils.py
def calculer(x):
    return x * 2

if __name__ == "__main__":
    # Tests uniquement
    assert calculer(5) == 10
    print("✅ Tests OK")

# ❌ Mauvais : mélanger logique et tests
def calculer(x):
    result = x * 2
    print(f"Test: {result}")  # Pollution !
    return result
```

## Pièges Courants

### Erreur 1 : Import circulaire

```python
# ❌ fichier_a.py
from fichier_b import fonction_b

def fonction_a():
    return fonction_b()

# ❌ fichier_b.py
from fichier_a import fonction_a  # Erreur circulaire !

def fonction_b():
    return fonction_a()

# ✅ Solution : Restructurer ou importer dans la fonction
def fonction_b():
    from fichier_a import fonction_a  # Import local
    return fonction_a()
```

### Erreur 2 : Module non trouvé

```python
# Structure :
# projet/
#   ├── main.py
#   └── dossier/
#       └── utils.py

# ❌ main.py
import utils  # ModuleNotFoundError

# ✅ main.py
from dossier import utils
# ou
import dossier.utils
```

### Erreur 3 : Écraser les modules intégrés

```python
# ❌ Ne jamais faire :
# random.py  ← Votre fichier
# datetime.py  ← Votre fichier
# os.py  ← Votre fichier

# Cela écrase les modules Python !

# ✅ Utilisez des noms spécifiques :
# mon_random_utils.py
# mes_dates.py
# mes_outils_systeme.py
```

## Checklist de Maîtrise

- [ ] Je sais créer un module Python (.py)
- [ ] Je peux importer mes modules dans d'autres fichiers
- [ ] Je comprends `__name__` et `__main__`
- [ ] Je sais structurer un projet multi-fichiers
- [ ] Je documente mes modules avec docstrings
- [ ] J'évite les imports circulaires
- [ ] Je connais les bonnes pratiques de nommage
- [ ] Je sais créer un package avec `__init__.py`

**Organisez votre code comme vous organiseriez votre maison : chaque chose à sa place, facile à trouver, facile à maintenir !**

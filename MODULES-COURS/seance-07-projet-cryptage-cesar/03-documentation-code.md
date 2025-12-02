# Documentation de Code en Python

## Objectifs

- Comprendre l'importance de la documentation
- Maîtriser les docstrings (PEP 257)
- Écrire des commentaires utiles et pertinents
- Documenter fonctions, classes et modules
- Créer un fichier README efficace
- Utiliser les conventions de documentation Python

## Introduction / Métaphore

### La Documentation = Mode d'Emploi

Imaginez acheter un meuble IKEA sans notice de montage. Juste des pièces et des vis. Frustrant, non ?

**Code sans documentation :**
```python
def f(t, d):
    r = []
    for c in t:
        if c.isalpha():
            b = ord('A') if c.isupper() else ord('a')
            r.append(chr((ord(c) - b + d) % 26 + b))
        else:
            r.append(c)
    return ''.join(r)
```
*"Qu'est-ce que ça fait ? Qu'est-ce que t et d ? Comment l'utiliser ?"* 😵

**Code avec documentation :**
```python
def crypter_cesar(texte, decalage):
    """
    Crypte un texte avec le chiffre de César.

    Le chiffre de César décale chaque lettre de l'alphabet
    d'un nombre fixe de positions.

    Args:
        texte (str): Le texte à crypter
        decalage (int): Le nombre de positions de décalage (0-25)

    Returns:
        str: Le texte crypté

    Example:
        >>> crypter_cesar("ABC", 3)
        'DEF'
    """
    resultat = []
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultat.append(chr((ord(char) - base + decalage) % 26 + base))
        else:
            resultat.append(char)
    return ''.join(resultat)
```
*"Ah ! Ça crypte un texte. Je passe le texte et le décalage. Exemple clair !"* 😊

## Concept Fondamental : Pourquoi Documenter ?

### Les 5 Raisons Essentielles

| Raison | Explication |
|--------|-------------|
| **Pour les autres** | Vos collègues doivent comprendre votre code |
| **Pour vous (futur)** | Dans 6 mois, vous aurez oublié |
| **Pour l'utilisation** | Comment appeler vos fonctions ? |
| **Pour la maintenance** | Modifier sans tout casser |
| **Pour la professionnalité** | Code pro = code documenté |

### La Règle d'Or

> **"Si vous devez réfléchir pour comprendre ce que fait le code, il faut le documenter."**

## Les Docstrings : Documentation Officielle

### Qu'est-ce qu'une Docstring ?

Une **docstring** est une chaîne de caractères qui documente un module, une classe, une fonction ou une méthode.

**Syntaxe :** Entre triple guillemets `"""` juste après la déclaration.

```python
def ma_fonction():
    """Ceci est une docstring"""
    pass
```

### Accéder à une Docstring

```python
def saluer(nom):
    """Affiche un message de salutation"""
    print(f"Bonjour {nom} !")

# Accéder à la docstring
print(saluer.__doc__)
# Affiche: Affiche un message de salutation

# Ou avec help()
help(saluer)
```

### PEP 257 : Convention de Style

La **PEP 257** définit les conventions pour les docstrings en Python.

#### Docstring Une Ligne (Simple)

```python
def est_pair(nombre):
    """Retourne True si le nombre est pair, False sinon."""
    return nombre % 2 == 0
```

**Règles :**
- Une seule ligne
- Point final
- Décrit ce que fait la fonction (pas comment)

#### Docstring Multi-Lignes (Complexe)

```python
def calculer_moyenne(notes, coefficients=None):
    """
    Calcule la moyenne pondérée d'une liste de notes.

    Si aucun coefficient n'est fourni, calcule la moyenne simple.
    Tous les coefficients doivent être positifs.

    Args:
        notes (list): Liste des notes (nombres)
        coefficients (list, optional): Liste des coefficients. Defaults to None.

    Returns:
        float: La moyenne calculée

    Raises:
        ValueError: Si notes est vide ou si len(notes) != len(coefficients)
        TypeError: Si notes ou coefficients contiennent des non-nombres

    Example:
        >>> calculer_moyenne([15, 18, 12])
        15.0
        >>> calculer_moyenne([15, 18, 12], [1, 2, 1])
        16.0
    """
    if not notes:
        raise ValueError("La liste de notes ne peut pas être vide")

    if coefficients is None:
        return sum(notes) / len(notes)

    if len(notes) != len(coefficients):
        raise ValueError("Le nombre de notes doit égaler le nombre de coefficients")

    total = sum(n * c for n, c in zip(notes, coefficients))
    return total / sum(coefficients)
```

### Structure d'une Docstring Complète

```python
def nom_fonction(param1, param2):
    """
    [Ligne 1 : Résumé court en une phrase]

    [Paragraphe(s) de description détaillée si nécessaire]

    Args:
        param1 (type): Description du paramètre 1
        param2 (type): Description du paramètre 2

    Returns:
        type: Description de ce qui est retourné

    Raises:
        ExceptionType: Quand cette exception est levée

    Example:
        >>> nom_fonction(val1, val2)
        résultat_attendu
    """
    pass
```

## Documenter Différents Éléments

### 1. Documenter une Fonction

```python
def crypter_cesar(texte, decalage):
    """
    Crypte un texte avec le chiffre de César.

    Le chiffre de César remplace chaque lettre par une lettre située
    à un nombre fixe de positions dans l'alphabet.

    Args:
        texte (str): Texte à crypter (lettres, espaces, ponctuation)
        decalage (int): Nombre de positions de décalage (peut être négatif)

    Returns:
        str: Texte crypté (même longueur que l'original)

    Example:
        >>> crypter_cesar("Hello", 3)
        'Khoor'
        >>> crypter_cesar("ABC", -1)
        'ZAB'

    Note:
        Les caractères non-alphabétiques restent inchangés.
    """
    resultat = []
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nouveau_char = chr((ord(char) - base + decalage) % 26 + base)
            resultat.append(nouveau_char)
        else:
            resultat.append(char)
    return ''.join(resultat)
```

### 2. Documenter une Classe

```python
class CompteBancaire:
    """
    Représente un compte bancaire avec solde et opérations.

    Cette classe permet de gérer un compte bancaire simple avec
    des opérations de dépôt, retrait et consultation du solde.

    Attributes:
        titulaire (str): Nom du titulaire du compte
        solde (float): Solde actuel du compte
        operations (list): Historique des opérations

    Example:
        >>> compte = CompteBancaire("Alice", 1000)
        >>> compte.deposer(500)
        >>> compte.solde
        1500
    """

    def __init__(self, titulaire, solde_initial=0):
        """
        Initialise un nouveau compte bancaire.

        Args:
            titulaire (str): Nom du titulaire
            solde_initial (float, optional): Solde de départ. Defaults to 0.

        Raises:
            ValueError: Si le solde initial est négatif
        """
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")

        self.titulaire = titulaire
        self.solde = solde_initial
        self.operations = []

    def deposer(self, montant):
        """
        Dépose de l'argent sur le compte.

        Args:
            montant (float): Montant à déposer (doit être positif)

        Raises:
            ValueError: Si le montant est négatif ou nul

        Example:
            >>> compte.deposer(500)
            >>> compte.solde
            1500
        """
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        self.solde += montant
        self.operations.append(f"Dépôt: +{montant}€")

    def retirer(self, montant):
        """
        Retire de l'argent du compte.

        Args:
            montant (float): Montant à retirer (doit être positif)

        Returns:
            bool: True si le retrait a réussi, False si solde insuffisant

        Example:
            >>> compte.retirer(200)
            True
            >>> compte.solde
            800
        """
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        if montant > self.solde:
            return False

        self.solde -= montant
        self.operations.append(f"Retrait: -{montant}€")
        return True
```

### 3. Documenter un Module

```python
"""
Module de cryptographie - Chiffre de César.

Ce module fournit des fonctions pour crypter et décrypter des textes
en utilisant le chiffre de César, une technique de cryptographie simple
par substitution.

Functions:
    crypter_cesar(texte, decalage): Crypte un texte
    decrypter_cesar(texte, decalage): Décrypte un texte
    bruteforce_cesar(texte_crypte): Essaie tous les décalages possibles

Example:
    import cryptage_cesar

    texte = "Message secret"
    crypte = cryptage_cesar.crypter_cesar(texte, 5)
    decrypte = cryptage_cesar.decrypter_cesar(crypte, 5)

Author: Votre Nom
Date: 2025-11-02
Version: 1.0
"""

def crypter_cesar(texte, decalage):
    """Crypte un texte avec le chiffre de César."""
    pass

def decrypter_cesar(texte, decalage):
    """Décrypte un texte crypté avec César."""
    pass
```

## Les Commentaires : Compléments Essentiels

### Différence Docstring vs Commentaire

| Aspect | Docstring | Commentaire |
|--------|-----------|-------------|
| **Position** | Après déclaration | N'importe où |
| **Syntaxe** | `"""..."""` | `# ...` |
| **Usage** | Documente l'API publique | Explique le "pourquoi" |
| **Accessible** | Via `help()`, `__doc__` | Non accessible |

### Commentaires Utiles

```python
def crypter_cesar(texte, decalage):
    """Crypte un texte avec le chiffre de César."""

    resultat = []

    for char in texte:
        if char.isalpha():
            # Déterminer la base ASCII (A pour majuscules, a pour minuscules)
            base = ord('A') if char.isupper() else ord('a')

            # Appliquer le décalage avec modulo pour boucler sur l'alphabet
            position = ord(char) - base
            nouvelle_position = (position + decalage) % 26
            nouveau_char = chr(nouvelle_position + base)

            resultat.append(nouveau_char)
        else:
            # Garder les caractères non-alphabétiques intacts
            resultat.append(char)

    return ''.join(resultat)
```

### Commentaires à Éviter

```python
# ❌ Commentaire évident (redondant)
i = i + 1  # Incrémenter i

# ❌ Commentaire qui répète le code
total = prix * quantite  # Multiplier prix par quantité

# ❌ Commentaire obsolète
# Cette fonction utilise l'algorithme A (FAUX, elle utilise B maintenant)
def calculer():
    pass

# ✅ Bon commentaire (explique le POURQUOI)
# On utilise l'algorithme B car il est 3x plus rapide pour n > 1000
def calculer():
    pass
```

### Commentaires TODO et FIXME

```python
def traiter_donnees(donnees):
    """Traite et valide des données."""

    # TODO: Ajouter validation des emails
    # FIXME: Bug avec les dates au format US
    # HACK: Solution temporaire, à refactoriser
    # NOTE: Cette fonction sera dépréciée en v2.0

    pass
```

## Le Fichier README.md

### Structure d'un README Complet

```markdown
# Projet Cryptage César

## Description

Programme Python pour crypter et décrypter des messages avec le chiffre de César.

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/username/cryptage-cesar.git

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

```python
from cryptage_cesar import crypter_cesar, decrypter_cesar

# Crypter un message
message = "Hello World"
crypte = crypter_cesar(message, 5)
print(crypte)  # "Mjqqt Btwqi"

# Décrypter
decrypte = decrypter_cesar(crypte, 5)
print(decrypte)  # "Hello World"
```

## Fonctionnalités

- ✅ Cryptage avec décalage personnalisable
- ✅ Décryptage
- ✅ Brute force (essai de tous les décalages)
- ✅ Support majuscules/minuscules
- ✅ Préserve ponctuation et espaces

## Tests

```bash
python -m pytest tests/
```

## Structure du Projet

```
cryptage-cesar/
├── cryptage_cesar.py      # Code principal
├── test_cryptage.py       # Tests unitaires
├── README.md              # Ce fichier
└── requirements.txt       # Dépendances
```

## Contribution

Les contributions sont bienvenues ! Voir CONTRIBUTING.md

## Licence

MIT License - Voir LICENSE

## Auteur

Votre Nom - [@username](https://github.com/username)

## Changelog

### v1.0.0 (2025-11-02)
- Version initiale
- Cryptage et décryptage de base
```

### Éléments Essentiels d'un README

| Section | Description |
|---------|-------------|
| **Titre** | Nom du projet |
| **Description** | En 1-2 phrases, que fait le projet |
| **Installation** | Comment installer/lancer |
| **Utilisation** | Exemples concrets de code |
| **Fonctionnalités** | Liste des features |
| **Tests** | Comment lancer les tests |
| **Licence** | Type de licence |
| **Auteur** | Qui a créé le projet |

## Bonnes Pratiques

### ✅ À FAIRE

```python
# 1. Docstring pour toutes les fonctions publiques
def fonction_publique():
    """Cette fonction est documentée."""
    pass

# 2. Exemples dans les docstrings
def additionner(a, b):
    """
    Additionne deux nombres.

    Example:
        >>> additionner(2, 3)
        5
    """
    return a + b

# 3. Expliquer le POURQUOI, pas le QUOI
# On trie avant de chercher car la recherche binaire nécessite un tri
liste_triee = sorted(liste)

# 4. Tenir la documentation à jour
def nouvelle_fonction():
    """
    [À JOUR avec la dernière version du code]
    """
    pass
```

### ❌ À ÉVITER

```python
# 1. Docstring vague
def f(x):
    """Fait un truc."""  # ❌ Trop vague
    pass

# 2. Commentaire évident
x = x + 1  # Ajoute 1 à x  # ❌ Redondant

# 3. Documentation obsolète
# Cette fonction retourne une liste  # ❌ FAUX, retourne un dict
def obtenir_donnees():
    return {"cle": "valeur"}

# 4. Trop de commentaires inutiles
# Initialiser i à 0
i = 0
# Boucler de 0 à 9
for i in range(10):
    # Afficher i
    print(i)  # ❌ Surcharge inutile
```

## Template : Projet Complet Documenté

```python
"""
Module de cryptographie - Chiffre de César.

Ce module implémente le chiffre de César, une des techniques
de cryptographie les plus simples et les plus connues.

Example:
    >>> from cryptage_cesar import crypter_cesar
    >>> crypter_cesar("Hello", 3)
    'Khoor'
"""

def crypter_cesar(texte, decalage):
    """
    Crypte un texte avec le chiffre de César.

    Args:
        texte (str): Texte à crypter
        decalage (int): Nombre de positions de décalage

    Returns:
        str: Texte crypté

    Example:
        >>> crypter_cesar("ABC", 3)
        'DEF'
    """
    if not isinstance(texte, str):
        raise TypeError("Le texte doit être une chaîne de caractères")

    resultat = []
    for char in texte:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            nouveau_char = chr((ord(char) - base + decalage) % 26 + base)
            resultat.append(nouveau_char)
        else:
            resultat.append(char)

    return ''.join(resultat)


def decrypter_cesar(texte, decalage):
    """
    Décrypte un texte crypté avec le chiffre de César.

    Args:
        texte (str): Texte crypté
        decalage (int): Nombre de positions de décalage utilisé

    Returns:
        str: Texte décrypté

    Example:
        >>> decrypter_cesar("DEF", 3)
        'ABC'
    """
    return crypter_cesar(texte, -decalage)


# Tests (si lancé directement)
if __name__ == "__main__":
    print("🧪 Tests du module cryptage_cesar")

    # Test 1
    assert crypter_cesar("Hello", 3) == "Khoor", "Test cryptage simple"
    print("✅ Test 1 OK")

    # Test 2
    crypte = crypter_cesar("Python", 5)
    decrypte = decrypter_cesar(crypte, 5)
    assert decrypte == "Python", "Test symétrie"
    print("✅ Test 2 OK")

    print("\n✅ Tous les tests réussis !")
```

## Checklist de Maîtrise

- [ ] Je documente toutes mes fonctions avec des docstrings
- [ ] J'utilise la structure PEP 257 (résumé, Args, Returns, Example)
- [ ] J'écris des commentaires pour expliquer le "pourquoi"
- [ ] J'évite les commentaires évidents ou redondants
- [ ] Je documente les classes avec attributs et méthodes
- [ ] Je crée un README.md pour mes projets
- [ ] Je garde ma documentation à jour avec le code
- [ ] J'utilise des exemples concrets dans les docstrings
- [ ] Je documente les exceptions possibles (Raises)

**Un code bien documenté est un code professionnel. La documentation n'est pas optionnelle !**

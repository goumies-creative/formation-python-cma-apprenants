# Tests Unitaires en Python

## Objectifs

- Comprendre l'importance des tests dans le développement
- Maîtriser les assertions avec assert
- Écrire des fonctions de test efficaces
- Tester différents cas : normaux, limites, erreurs
- Adopter une approche TDD (Test-Driven Development)
- Structurer les tests de manière professionnelle

## Introduction / Métaphore

### Les Tests = Filet de Sécurité

Imaginez un acrobate sur un trapèze. En dessous : un filet de sécurité.

**Sans tests (sans filet) :**
- Une erreur = catastrophe
- Peur de modifier le code
- Bugs découverts en production (devant les utilisateurs)

**Avec tests (avec filet) :**
- Une erreur est détectée immédiatement
- Confiance pour modifier le code
- Bugs découverts AVANT la mise en production

```python
# Sans tests : stress et incertitude
def crypter_cesar(texte, decalage):
    # Est-ce que ça marche vraiment ?
    # Ai-je pensé à tous les cas ?
    # Et si je modifie le code, ça va casser ?
    pass

# Avec tests : sérénité et confiance
def crypter_cesar(texte, decalage):
    # ✅ 15 tests passent
    # ✅ Tous les cas couverts
    # ✅ Je peux modifier en toute sécurité
    pass
```

## Concept Fondamental : Qu'est-ce qu'un Test ?

### Définition

Un **test** est un bout de code qui vérifie qu'un autre bout de code fonctionne correctement.

### Anatomie d'un Test

```python
# Fonction à tester
def additionner(a, b):
    return a + b

# Test de la fonction
def test_additionner():
    # 1. ARRANGE : Préparer les données
    a = 5
    b = 3

    # 2. ACT : Exécuter la fonction
    resultat = additionner(a, b)

    # 3. ASSERT : Vérifier le résultat
    assert resultat == 8, "5 + 3 devrait faire 8"

    print("✅ Test additionner réussi")

# Lancer le test
test_additionner()
```

### Les 3 A du Testing

| Étape | Nom | Description |
|-------|-----|-------------|
| **Arrange** | Préparer | Définir les données de test |
| **Act** | Agir | Exécuter la fonction testée |
| **Assert** | Affirmer | Vérifier que le résultat est correct |

## Les Assertions : assert

### Syntaxe de base

```python
assert condition, "Message si l'assertion échoue"

# Exemples
assert 5 > 3, "5 devrait être supérieur à 3"
assert "a" in "chat", "'a' devrait être dans 'chat'"
assert len([1, 2, 3]) == 3, "La liste devrait avoir 3 éléments"
```

### Assertions Courantes

```python
# Égalité
assert resultat == valeur_attendue

# Inégalité
assert resultat != valeur_non_souhaitee

# Comparaisons
assert age >= 18
assert score < 100

# Appartenance
assert "e" in texte
assert element in liste

# Type
assert isinstance(valeur, int)
assert isinstance(texte, str)

# Booléens
assert est_valide
assert not est_vide

# None
assert resultat is not None
assert valeur is None
```

## Tester une Fonction Simple

### Exemple : Fonction est_pair

```python
def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0

# Tests
def test_est_pair():
    """Tests de la fonction est_pair"""
    print("🧪 Tests de est_pair...")

    # Test 1 : Nombre pair
    assert est_pair(4) == True, "4 est pair"

    # Test 2 : Nombre impair
    assert est_pair(5) == False, "5 est impair"

    # Test 3 : Zéro (cas limite)
    assert est_pair(0) == True, "0 est pair"

    # Test 4 : Nombre négatif pair
    assert est_pair(-6) == True, "-6 est pair"

    # Test 5 : Nombre négatif impair
    assert est_pair(-7) == False, "-7 est impair"

    print("✅ Tous les tests réussis !")

# Lancer les tests
test_est_pair()
```

## Les Différents Types de Cas de Test

### 1. Cas Normaux (Happy Path)

```python
def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    return sum(notes) / len(notes)

def test_moyenne_cas_normal():
    """Test avec des valeurs normales"""
    notes = [15, 18, 12, 14]
    resultat = calculer_moyenne(notes)
    assert resultat == 14.75, "Moyenne de [15, 18, 12, 14] = 14.75"
    print("✅ Test cas normal OK")
```

### 2. Cas Limites (Edge Cases)

```python
def test_moyenne_cas_limites():
    """Test avec des cas limites"""
    # Une seule note
    assert calculer_moyenne([20]) == 20, "Moyenne d'une seule note"

    # Toutes les notes identiques
    assert calculer_moyenne([15, 15, 15]) == 15, "Notes identiques"

    # Notes = 0
    assert calculer_moyenne([0, 0, 0]) == 0, "Notes nulles"

    print("✅ Test cas limites OK")
```

### 3. Cas d'Erreur (Error Cases)

```python
def test_moyenne_cas_erreur():
    """Test avec des cas d'erreur"""
    try:
        # Liste vide devrait lever une erreur
        calculer_moyenne([])
        assert False, "Une liste vide devrait lever une erreur"
    except ZeroDivisionError:
        # C'est le comportement attendu
        print("✅ Erreur bien levée pour liste vide")
```

## Pattern : Suite de Tests Complète

```python
def crypter_cesar(texte, decalage):
    """
    Crypte un texte avec le chiffre de César

    Args:
        texte (str): Texte à crypter
        decalage (int): Décalage de l'alphabet

    Returns:
        str: Texte crypté
    """
    if not texte:
        return ""

    resultat = []
    for char in texte:
        if char.isalpha():
            # Déterminer si majuscule ou minuscule
            base = ord('A') if char.isupper() else ord('a')
            # Appliquer le décalage
            nouveau_char = chr((ord(char) - base + decalage) % 26 + base)
            resultat.append(nouveau_char)
        else:
            # Garder les caractères non-alphabétiques
            resultat.append(char)

    return ''.join(resultat)


def test_crypter_cesar():
    """Suite complète de tests pour crypter_cesar"""
    print("🧪 Tests de crypter_cesar...")

    # ===== CAS NORMAUX =====
    print("\n📋 Cas normaux...")

    # Test 1 : Minuscules, décalage 3
    assert crypter_cesar("abc", 3) == "def", "abc + 3 = def"

    # Test 2 : Majuscules, décalage 3
    assert crypter_cesar("ABC", 3) == "DEF", "ABC + 3 = DEF"

    # Test 3 : Texte mixte
    assert crypter_cesar("Hello", 3) == "Khoor", "Hello + 3 = Khoor"

    # Test 4 : Avec espaces
    assert crypter_cesar("Hello World", 3) == "Khoor Zruog", "Espaces préservés"

    print("✅ Cas normaux OK")

    # ===== CAS LIMITES =====
    print("\n🔎 Cas limites...")

    # Test 5 : Décalage 0 (pas de changement)
    assert crypter_cesar("Test", 0) == "Test", "Décalage 0"

    # Test 6 : Décalage 26 (retour au début)
    assert crypter_cesar("abc", 26) == "abc", "Décalage 26 = pas de changement"

    # Test 7 : Débordement alphabet (z -> c avec décalage 3)
    assert crypter_cesar("xyz", 3) == "abc", "Débordement alphabet"

    # Test 8 : Texte vide
    assert crypter_cesar("", 3) == "", "Texte vide"

    # Test 9 : Caractères spéciaux
    assert crypter_cesar("Hello, World!", 3) == "Khoor, Zruog!", "Ponctuation préservée"

    # Test 10 : Chiffres
    assert crypter_cesar("Test123", 3) == "Whvw123", "Chiffres préservés"

    print("✅ Cas limites OK")

    # ===== CAS NÉGATIFS =====
    print("\n⬅️ Décalage négatif...")

    # Test 11 : Décalage négatif (décryptage)
    assert crypter_cesar("def", -3) == "abc", "Décalage négatif"

    print("✅ Décalage négatif OK")

    print("\n🎉 TOUS LES TESTS RÉUSSIS !")


# Lancer les tests
if __name__ == "__main__":
    test_crypter_cesar()
```

## Test-Driven Development (TDD)

### Le Cycle Rouge-Vert-Refactor

**Philosophie :** Écrire les tests AVANT le code.

```python
# ÉTAPE 1 : Écrire le test AVANT la fonction (Rouge)
def test_calculer_factorielle():
    assert calculer_factorielle(5) == 120
    assert calculer_factorielle(0) == 1
    assert calculer_factorielle(1) == 1
    # ❌ Test échoue : fonction n'existe pas encore

# ÉTAPE 2 : Écrire le minimum de code pour passer (Vert)
def calculer_factorielle(n):
    if n == 0 or n == 1:
        return 1
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat
    # ✅ Tests passent

# ÉTAPE 3 : Refactoriser (si nécessaire)
def calculer_factorielle(n):
    # Version récursive plus élégante
    return 1 if n <= 1 else n * calculer_factorielle(n - 1)
    # ✅ Tests passent toujours
```

### Avantages du TDD

| Avantage | Explication |
|----------|-------------|
| **Design amélioré** | Penser à l'utilisation avant l'implémentation |
| **Code testable** | Fonctions petites et modulaires |
| **Documentation** | Les tests montrent comment utiliser le code |
| **Confiance** | Modifications sans peur de casser |

## Structurer les Tests

### Pattern : Fichier de Tests Séparé

```
projet/
├── cryptage.py          # Code principal
└── test_cryptage.py     # Tests
```

```python
# cryptage.py
def crypter_cesar(texte, decalage):
    """Crypte un texte avec le chiffre de César"""
    # ... implémentation ...
    pass

def decrypter_cesar(texte, decalage):
    """Décrypte un texte crypté avec César"""
    return crypter_cesar(texte, -decalage)
```

```python
# test_cryptage.py
from cryptage import crypter_cesar, decrypter_cesar

def test_crypter_cesar():
    """Tests du cryptage"""
    assert crypter_cesar("abc", 3) == "def"
    assert crypter_cesar("xyz", 3) == "abc"
    print("✅ Tests cryptage OK")

def test_decrypter_cesar():
    """Tests du décryptage"""
    # Crypter puis décrypter = texte original
    texte = "Hello World"
    crypte = crypter_cesar(texte, 5)
    decrypte = decrypter_cesar(crypte, 5)
    assert decrypte == texte, "Décryptage inverse du cryptage"
    print("✅ Tests décryptage OK")

def test_symetrie():
    """Test de symétrie cryptage/décryptage"""
    textes = ["Python", "Test123", "Hello, World!"]
    for texte in textes:
        for decalage in range(26):
            crypte = crypter_cesar(texte, decalage)
            decrypte = decrypter_cesar(crypte, decalage)
            assert decrypte == texte, f"Symétrie pour '{texte}' avec décalage {decalage}"
    print("✅ Tests symétrie OK")

# Lancer tous les tests
if __name__ == "__main__":
    test_crypter_cesar()
    test_decrypter_cesar()
    test_symetrie()
    print("\n🎉 TOUS LES TESTS RÉUSSIS !")
```

## Bonnes Pratiques

### ✅ À FAIRE

```python
# 1. Noms de tests descriptifs
def test_crypter_avec_decalage_negatif():  # ✅ Clair
    pass

# 2. Un concept par test
def test_majuscules():
    assert crypter_cesar("ABC", 3) == "DEF"

def test_minuscules():
    assert crypter_cesar("abc", 3) == "def"

# 3. Messages d'erreur clairs
assert resultat == attendu, f"Attendu {attendu}, obtenu {resultat}"

# 4. Tester les cas limites
def test_cas_limites():
    assert fonction([]) == valeur_pour_liste_vide
    assert fonction([1]) == valeur_pour_un_element
    assert fonction(None) == valeur_pour_none
```

### ❌ À ÉVITER

```python
# 1. Tests trop généraux
def test_tout():  # ❌ Trop vague
    assert fonction1() and fonction2() and fonction3()

# 2. Pas de message d'erreur
assert resultat == 42  # ❌ Pas de message

# 3. Tests dépendants
def test_1():
    global variable
    variable = calcul()

def test_2():
    # ❌ Dépend de test_1
    assert variable > 0
```

## Exercice Pratique : Tests pour Validateur

```python
def valider_mot_de_passe(mdp):
    """
    Valide un mot de passe

    Règles :
    - Au moins 8 caractères
    - Au moins une majuscule
    - Au moins une minuscule
    - Au moins un chiffre

    Returns:
        bool: True si valide, False sinon
    """
    if len(mdp) < 8:
        return False

    if not any(c.isupper() for c in mdp):
        return False

    if not any(c.islower() for c in mdp):
        return False

    if not any(c.isdigit() for c in mdp):
        return False

    return True


def test_valider_mot_de_passe():
    """Tests complets du validateur de mot de passe"""
    print("🧪 Tests du validateur de mot de passe...")

    # CAS VALIDES
    assert valider_mot_de_passe("Azerty123") == True, "Mot de passe valide"
    assert valider_mot_de_passe("MonMotDePasse1") == True, "Mot de passe long valide"

    # CAS INVALIDES
    # Trop court
    assert valider_mot_de_passe("Abc1") == False, "Trop court"

    # Pas de majuscule
    assert valider_mot_de_passe("azerty123") == False, "Pas de majuscule"

    # Pas de minuscule
    assert valider_mot_de_passe("AZERTY123") == False, "Pas de minuscule"

    # Pas de chiffre
    assert valider_mot_de_passe("AzertyUiop") == False, "Pas de chiffre"

    # Vide
    assert valider_mot_de_passe("") == False, "Mot de passe vide"

    print("✅ Tous les tests réussis !")


# Lancer les tests
test_valider_mot_de_passe()
```

## Introduction à unittest (Bonus)

Python fournit un module `unittest` pour des tests plus professionnels :

```python
import unittest
from cryptage import crypter_cesar

class TestCryptageCesar(unittest.TestCase):
    """Tests du cryptage César avec unittest"""

    def test_cas_normal(self):
        """Test cas normal"""
        self.assertEqual(crypter_cesar("abc", 3), "def")

    def test_majuscules(self):
        """Test majuscules"""
        self.assertEqual(crypter_cesar("ABC", 3), "DEF")

    def test_debordement(self):
        """Test débordement alphabet"""
        self.assertEqual(crypter_cesar("xyz", 3), "abc")

    def test_texte_vide(self):
        """Test texte vide"""
        self.assertEqual(crypter_cesar("", 3), "")

# Lancer les tests
if __name__ == "__main__":
    unittest.main()
```

## Checklist de Maîtrise

- [ ] Je comprends pourquoi les tests sont importants
- [ ] Je sais utiliser assert pour vérifier des conditions
- [ ] Je peux écrire des tests pour une fonction simple
- [ ] Je teste les cas normaux, limites et d'erreur
- [ ] Je structure mes tests de façon claire (AAA)
- [ ] Je donne des noms descriptifs à mes tests
- [ ] J'ajoute des messages d'erreur clairs aux assertions
- [ ] Je comprends le concept de TDD
- [ ] Je sais organiser les tests dans un fichier séparé

**Les tests ne sont pas une perte de temps - ils sont un investissement qui vous fait gagner du temps !**

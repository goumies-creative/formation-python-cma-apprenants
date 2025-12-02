# -*- coding: utf-8 -*-
"""
Solution de l'Exercice 3 : Projet Complet - Chiffre de César

Projet professionnel complet avec :
- Gestion d'erreurs
- Tests unitaires
- Documentation complète
- Interface utilisateur
"""

print("=== SOLUTION EXERCICE 3 : PROJET COMPLET CHIFFRE DE CÉSAR ===\n")

# ============================================================================
# PARTIE 1 : FONCTIONS DE BASE
# ============================================================================

def crypter_cesar(texte, decalage):
    """
    Crypte un texte avec le chiffre de César.

    Le chiffre de César décale chaque lettre de l'alphabet d'un nombre
    fixe de positions. Les caractères non-alphabétiques restent inchangés.

    Args:
        texte (str): Le texte à crypter
        decalage (int): Le nombre de positions de décalage (peut être négatif)

    Returns:
        str: Le texte crypté

    Raises:
        TypeError: Si texte n'est pas une chaîne ou decalage n'est pas un entier
        ValueError: Si le texte est vide

    Example:
        >>> crypter_cesar("Hello", 3)
        'Khoor'
        >>> crypter_cesar("ABC", -1)
        'ZAB'
    """
    # Validation des types
    if not isinstance(texte, str):
        raise TypeError(f"Le texte doit être une chaîne, pas {type(texte).__name__}")

    if not isinstance(decalage, int):
        raise TypeError(f"Le décalage doit être un entier, pas {type(decalage).__name__}")

    # Validation de la valeur
    if not texte:
        raise ValueError("Le texte ne peut pas être vide")

    # Cryptage caractère par caractère
    resultat = []
    for char in texte:
        if char.isalpha():
            # Déterminer la base ASCII (A pour majuscules, a pour minuscules)
            base = ord('A') if char.isupper() else ord('a')

            # Calculer la nouvelle position avec modulo pour boucler
            position = ord(char) - base
            nouvelle_position = (position + decalage) % 26
            nouveau_char = chr(nouvelle_position + base)

            resultat.append(nouveau_char)
        else:
            # Garder les caractères non-alphabétiques tels quels
            resultat.append(char)

    return ''.join(resultat)


def decrypter_cesar(texte, decalage):
    """
    Décrypte un texte crypté avec le chiffre de César.

    Args:
        texte (str): Le texte crypté
        decalage (int): Le décalage utilisé pour le cryptage

    Returns:
        str: Le texte décrypté

    Example:
        >>> decrypter_cesar("Khoor", 3)
        'Hello'
    """
    return crypter_cesar(texte, -decalage)


def bruteforce_cesar(texte_crypte):
    """
    Essaie tous les décalages possibles (0-25) pour décrypter un texte.

    Utile quand on ne connaît pas le décalage utilisé pour le cryptage.

    Args:
        texte_crypte (str): Le texte crypté à décrypter

    Returns:
        list: Liste de tuples (decalage, texte_decrypte)

    Example:
        >>> resultats = bruteforce_cesar("Khoor")
        >>> len(resultats)
        26
    """
    resultats = []
    for decalage in range(26):
        texte_decrypte = decrypter_cesar(texte_crypte, decalage)
        resultats.append((decalage, texte_decrypte))
    return resultats


# ============================================================================
# PARTIE 2 : FONCTIONS DE VALIDATION
# ============================================================================

def valider_texte(texte):
    """
    Valide un texte pour le cryptage.

    Args:
        texte (str): Texte à valider

    Returns:
        bool: True si valide

    Raises:
        TypeError: Si texte n'est pas une chaîne
        ValueError: Si texte est vide
    """
    if not isinstance(texte, str):
        raise TypeError("Le texte doit être une chaîne de caractères")

    if not texte:
        raise ValueError("Le texte ne peut pas être vide")

    return True


def valider_decalage(decalage):
    """
    Valide un décalage pour le cryptage.

    Args:
        decalage (int): Décalage à valider

    Returns:
        bool: True si valide

    Raises:
        TypeError: Si decalage n'est pas un entier
        ValueError: Si decalage est hors limites (-25 à 25)
    """
    if not isinstance(decalage, int):
        raise TypeError("Le décalage doit être un entier")

    # Note : on accepte -25 à 25, mais techniquement tous les entiers fonctionnent
    # grâce au modulo, c'est juste une recommandation
    if decalage < -25 or decalage > 25:
        print(f"⚠️  Avertissement : Décalage {decalage} sera normalisé par modulo 26")

    return True


def demander_texte(message="Entrez le texte : "):
    """
    Demande un texte à l'utilisateur avec validation.

    Args:
        message (str): Message à afficher

    Returns:
        str: Texte valide saisi par l'utilisateur
    """
    while True:
        try:
            texte = input(message).strip()

            # Validation
            valider_texte(texte)

            return texte

        except ValueError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")


def demander_decalage(message="Entrez le décalage (0-25) : "):
    """
    Demande un décalage à l'utilisateur avec validation.

    Args:
        message (str): Message à afficher

    Returns:
        int: Décalage valide saisi par l'utilisateur
    """
    while True:
        try:
            decalage = int(input(message))

            # Validation
            valider_decalage(decalage)

            return decalage

        except ValueError:
            print("❌ Veuillez entrer un nombre entier valide")
        except TypeError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")


# ============================================================================
# PARTIE 3 : TESTS UNITAIRES
# ============================================================================

def test_crypter_cesar():
    """Tests de la fonction crypter_cesar"""
    print("🧪 Tests crypter_cesar...")

    # Cas normaux
    assert crypter_cesar("abc", 3) == "def"
    assert crypter_cesar("ABC", 3) == "DEF"
    assert crypter_cesar("Hello", 5) == "Mjqqt"

    # Débordement
    assert crypter_cesar("xyz", 3) == "abc"
    assert crypter_cesar("XYZ", 3) == "ABC"

    # Décalage 0 et 26
    assert crypter_cesar("Test", 0) == "Test"
    assert crypter_cesar("Test", 26) == "Test"

    # Caractères spéciaux
    assert crypter_cesar("Hello World!", 3) == "Khoor Zruog!"
    assert crypter_cesar("Test123", 5) == "Yjxy123"

    # Décalages négatifs
    assert crypter_cesar("bcd", -1) == "abc"

    print("✅ Tests crypter_cesar OK")


def test_decrypter_cesar():
    """Tests de la fonction decrypter_cesar"""
    print("🧪 Tests decrypter_cesar...")

    # Décryptage simple
    assert decrypter_cesar("def", 3) == "abc"
    assert decrypter_cesar("Khoor", 3) == "Hello"

    # Symétrie
    texte = "Python est génial"
    for decalage in [1, 5, 13, 20]:
        crypte = crypter_cesar(texte, decalage)
        decrypte = decrypter_cesar(crypte, decalage)
        assert decrypte == texte

    print("✅ Tests decrypter_cesar OK")


def test_bruteforce_cesar():
    """Tests de la fonction bruteforce_cesar"""
    print("🧪 Tests bruteforce_cesar...")

    # Nombre de résultats
    resultats = bruteforce_cesar("Test")
    assert len(resultats) == 26

    # Format des résultats
    assert all(isinstance(item, tuple) for item in resultats)
    assert all(len(item) == 2 for item in resultats)

    # Texte original présent
    texte = "Secret"
    crypte = crypter_cesar(texte, 7)
    resultats = bruteforce_cesar(crypte)
    textes = [t for _, t in resultats]
    assert texte in textes

    print("✅ Tests bruteforce_cesar OK")


def test_validation():
    """Tests des fonctions de validation"""
    print("🧪 Tests validation...")

    # valider_texte
    try:
        valider_texte("Hello")  # Valide
        valider_texte("")  # Devrait lever ValueError
        assert False, "Texte vide devrait être invalide"
    except ValueError:
        pass  # Comportement attendu

    # valider_decalage
    try:
        valider_decalage(5)  # Valide
        valider_decalage("abc")  # Devrait lever TypeError
        assert False, "Décalage non-entier devrait être invalide"
    except TypeError:
        pass  # Comportement attendu

    print("✅ Tests validation OK")


def executer_tous_les_tests():
    """Exécute tous les tests du projet"""
    print("\n" + "=" * 60)
    print("EXÉCUTION DE TOUS LES TESTS")
    print("=" * 60)
    print()

    try:
        test_crypter_cesar()
        test_decrypter_cesar()
        test_bruteforce_cesar()
        test_validation()

        print("\n" + "=" * 60)
        print("🎉 TOUS LES TESTS RÉUSSIS !")
        print("=" * 60)

    except AssertionError as e:
        print(f"\n❌ ÉCHEC : {e}")
        import traceback
        traceback.print_exc()
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")
        import traceback
        traceback.print_exc()


# ============================================================================
# PARTIE 4 : INTERFACE UTILISATEUR
# ============================================================================

def afficher_menu():
    """Affiche le menu principal"""
    print("\n" + "=" * 60)
    print("🔐 CHIFFRE DE CÉSAR")
    print("=" * 60)
    print("1. Crypter un message")
    print("2. Décrypter un message")
    print("3. Brute force (essayer tous les décalages)")
    print("4. Exécuter les tests")
    print("5. Quitter")
    print("=" * 60)


def option_crypter():
    """Gère l'option de cryptage"""
    print("\n--- CRYPTAGE ---")

    try:
        # Demander le texte
        texte = demander_texte("Entrez le texte à crypter : ")

        # Demander le décalage
        decalage = demander_decalage("Entrez le décalage (0-25) : ")

        # Crypter
        texte_crypte = crypter_cesar(texte, decalage)

        # Afficher le résultat
        print(f"\n✅ Texte crypté : {texte_crypte}")
        print(f"   Décalage utilisé : {decalage}")

    except Exception as e:
        print(f"❌ Erreur lors du cryptage : {e}")


def option_decrypter():
    """Gère l'option de décryptage"""
    print("\n--- DÉCRYPTAGE ---")

    try:
        # Demander le texte crypté
        texte = demander_texte("Entrez le texte à décrypter : ")

        # Demander le décalage
        decalage = demander_decalage("Entrez le décalage utilisé : ")

        # Décrypter
        texte_decrypte = decrypter_cesar(texte, decalage)

        # Afficher le résultat
        print(f"\n✅ Texte décrypté : {texte_decrypte}")

    except Exception as e:
        print(f"❌ Erreur lors du décryptage : {e}")


def option_bruteforce():
    """Gère l'option brute force"""
    print("\n--- BRUTE FORCE ---")

    try:
        # Demander le texte crypté
        texte = demander_texte("Entrez le texte crypté : ")

        # Essayer tous les décalages
        resultats = bruteforce_cesar(texte)

        # Afficher tous les résultats
        print("\n📋 Tous les décalages possibles :")
        print("-" * 60)

        for decalage, texte_decrypte in resultats:
            print(f"Décalage {decalage:2d} : {texte_decrypte}")

        print("-" * 60)
        print("\n💡 Trouvez le texte qui a du sens et notez son décalage !")

        # Permettre à l'utilisateur de choisir
        choix = input("\nConnaissez-vous le bon décalage ? (o/n) : ").lower()

        if choix == 'o':
            bon_decalage = demander_decalage("Quel est le bon décalage ? ")
            print(f"\n✅ Message décrypté : {resultats[bon_decalage][1]}")

    except Exception as e:
        print(f"❌ Erreur lors du brute force : {e}")


def application_principale():
    """Application principale avec menu interactif"""
    print("Bienvenue dans l'application Chiffre de César !")
    print("Application complète avec gestion d'erreurs, tests et interface intuitive.")

    while True:
        try:
            afficher_menu()
            choix = input("\nVotre choix (1-5) : ").strip()

            if choix == '1':
                option_crypter()
            elif choix == '2':
                option_decrypter()
            elif choix == '3':
                option_bruteforce()
            elif choix == '4':
                executer_tous_les_tests()
            elif choix == '5':
                print("\n👋 Merci d'avoir utilisé Chiffre de César. Au revoir !")
                break
            else:
                print("❌ Choix invalide. Veuillez choisir entre 1 et 5.")

        except KeyboardInterrupt:
            print("\n\n👋 Interruption détectée. Au revoir !")
            break
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")


# ============================================================================
# PARTIE 5 : FONCTIONNALITÉS BONUS
# ============================================================================

def sauvegarder_message(texte, nom_fichier="message.txt"):
    """
    Sauvegarde un message crypté dans un fichier.

    Args:
        texte (str): Texte à sauvegarder
        nom_fichier (str): Nom du fichier

    Returns:
        bool: True si succès, False sinon
    """
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write(texte)
        print(f"✅ Message sauvegardé dans '{nom_fichier}'")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
        return False


def charger_message(nom_fichier="message.txt"):
    """
    Charge un message depuis un fichier.

    Args:
        nom_fichier (str): Nom du fichier

    Returns:
        str: Contenu du fichier

    Raises:
        FileNotFoundError: Si le fichier n'existe pas
    """
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
        print(f"✅ Message chargé depuis '{nom_fichier}'")
        return contenu
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier '{nom_fichier}' n'existe pas")
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")
        return None


def analyser_frequences(texte):
    """
    Analyse les fréquences des lettres dans un texte.

    Utile pour la cryptanalyse (aide au brute force).

    Args:
        texte (str): Texte à analyser

    Returns:
        dict: Dictionnaire {lettre: fréquence}
    """
    frequences = {}

    # Compter chaque lettre (ignorer la casse)
    texte_minuscule = texte.lower()
    total_lettres = sum(1 for c in texte_minuscule if c.isalpha())

    if total_lettres == 0:
        return {}

    for char in texte_minuscule:
        if char.isalpha():
            frequences[char] = frequences.get(char, 0) + 1

    # Convertir en pourcentages
    for lettre in frequences:
        frequences[lettre] = round((frequences[lettre] / total_lettres) * 100, 2)

    return frequences


# ============================================================================
# DOCUMENTATION (README)
# ============================================================================

__doc__ = """
# PROJET CHIFFRE DE CÉSAR

## Description

Application complète de cryptage/décryptage utilisant le chiffre de César.
Le chiffre de César est une technique de cryptographie par substitution
où chaque lettre est remplacée par une lettre située à une position fixe
dans l'alphabet.

## Fonctionnalités

- ✅ Cryptage de texte avec décalage personnalisable
- ✅ Décryptage de texte
- ✅ Brute force (essai de tous les décalages)
- ✅ Validation des entrées utilisateur
- ✅ Gestion complète des erreurs
- ✅ Tests unitaires complets
- ✅ Interface utilisateur interactive
- ✅ Documentation complète (docstrings PEP 257)
- ✅ Sauvegarde/chargement de fichiers (bonus)
- ✅ Analyse de fréquences (bonus)

## Utilisation

### Cryptage
```python
texte = "Hello World"
decalage = 5
texte_crypte = crypter_cesar(texte, decalage)
# Résultat : "Mjqqt Btwqi"
```

### Décryptage
```python
texte_crypte = "Mjqqt Btwqi"
decalage = 5
texte_original = decrypter_cesar(texte_crypte, decalage)
# Résultat : "Hello World"
```

### Brute Force
```python
texte_crypte = "Mjqqt"
resultats = bruteforce_cesar(texte_crypte)
# Retourne 26 possibilités avec tous les décalages
```

## Structure du Code

1. **Fonctions de base** : crypter_cesar, decrypter_cesar, bruteforce_cesar
2. **Validation** : valider_texte, valider_decalage, demander_*
3. **Tests** : test_* pour toutes les fonctionnalités
4. **Interface** : Menu interactif avec options
5. **Bonus** : Sauvegarde, chargement, analyse de fréquences
6. **Documentation** : Docstrings complètes pour toutes les fonctions

## Tests

Exécuter tous les tests :
```python
executer_tous_les_tests()
```

## Exemple d'Exécution

```
🔐 CHIFFRE DE CÉSAR
1. Crypter un message
2. Décrypter un message
3. Brute force
4. Exécuter les tests
5. Quitter

Votre choix : 1
Entrez le texte : Secret
Entrez le décalage : 7
✅ Texte crypté : Zljyla
```

## Auteur

Formation Python CMA
Date : 2025-11-02
Version : 1.0

## Notes Techniques

- Gestion des majuscules et minuscules
- Préservation des caractères spéciaux (espaces, ponctuation, chiffres)
- Décalage peut être négatif (décryptage)
- Modulo 26 pour boucler sur l'alphabet
- Validation robuste des entrées
- Messages d'erreur clairs
- Code professionnel et maintenable
"""

# ============================================================================
# EXÉCUTION
# ============================================================================

if __name__ == "__main__":
    # Afficher le README
    print(__doc__)

    # Choix du mode
    print("\n" + "=" * 60)
    print("MODE DE LANCEMENT")
    print("=" * 60)
    print("1. Lancer l'application")
    print("2. Exécuter les tests")
    print("3. Démonstration")
    print("=" * 60)

    choix = input("\nVotre choix (1-3) : ").strip()

    if choix == '1':
        # Mode application
        application_principale()

    elif choix == '2':
        # Mode tests
        executer_tous_les_tests()

    elif choix == '3':
        # Mode démonstration
        print("\n" + "=" * 60)
        print("DÉMONSTRATION")
        print("=" * 60)

        message = "Python est un langage génial"
        decalage = 13

        print(f"\n1. Message original : '{message}'")
        print(f"2. Décalage choisi : {decalage}")

        crypte = crypter_cesar(message, decalage)
        print(f"3. Message crypté : '{crypte}'")

        decrypte = decrypter_cesar(crypte, decalage)
        print(f"4. Message décrypté : '{decrypte}'")

        print(f"\n5. Vérification : {decrypte == message}")

        print("\n6. Brute force (premiers 5 résultats) :")
        resultats = bruteforce_cesar(crypte)
        for dec, texte in resultats[:5]:
            print(f"   Décalage {dec:2d} : {texte}")

        print("\n7. Analyse de fréquences du texte crypté :")
        freq = analyser_frequences(crypte)
        top_5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for lettre, pourcentage in top_5:
            print(f"   {lettre} : {pourcentage}%")

        print("\n✨ Démonstration terminée !")

    else:
        print("Choix invalide. Lancement de l'application par défaut.")
        application_principale()


# ============================================================================
# POINTS CLÉS DU PROJET
# ============================================================================
"""
📚 CE QUE CE PROJET DÉMONTRE :

1. GESTION D'ERREURS PROFESSIONNELLE
   ✅ try/except pour toutes les entrées utilisateur
   ✅ Validation des types (isinstance)
   ✅ Validation des valeurs (raise ValueError)
   ✅ Messages d'erreur clairs et spécifiques
   ✅ Boucles de redemande jusqu'à valeur valide

2. TESTS UNITAIRES COMPLETS
   ✅ Tests des cas normaux
   ✅ Tests des cas limites (vide, 0, 26, débordement)
   ✅ Tests des caractères spéciaux
   ✅ Tests de symétrie (crypter/décrypter)
   ✅ Tests d'erreurs (exceptions levées)

3. DOCUMENTATION PROFESSIONNELLE
   ✅ Docstrings PEP 257 pour toutes les fonctions
   ✅ Args, Returns, Raises, Example
   ✅ Commentaires pour expliquer le POURQUOI
   ✅ README complet en docstring de module

4. INTERFACE UTILISATEUR
   ✅ Menu clair et intuitif
   ✅ Options numérotées
   ✅ Feedback visuel (✅, ❌, 🔐, etc.)
   ✅ Gestion de Ctrl+C (KeyboardInterrupt)
   ✅ Messages guidés

5. CODE PROPRE ET MAINTENABLE
   ✅ Fonctions petites et focalisées
   ✅ Noms de variables descriptifs
   ✅ Séparation des responsabilités
   ✅ DRY (Don't Repeat Yourself)
   ✅ Facile à étendre (bonus functions)

6. ALGORITHME MATHÉMATIQUE
   ✅ Modulo pour boucler sur l'alphabet
   ✅ Gestion majuscules/minuscules
   ✅ Préservation des non-lettres
   ✅ Décalages négatifs (décryptage)

7. BONNES PRATIQUES PYTHON
   ✅ with open() pour les fichiers
   ✅ List comprehensions
   ✅ String formatting (f-strings)
   ✅ Encoding UTF-8
   ✅ if __name__ == "__main__"

PROFESSIONNALISME
Ce projet montre toutes les compétences d'un développeur professionnel :
- Robustesse (gestion d'erreurs)
- Fiabilité (tests)
- Clarté (documentation)
- Maintenabilité (code propre)
- Expérience utilisateur (interface)

C'EST UN PROJET PORTFOLIO-READY ! 🎉
"""

# -*- coding: utf-8 -*-
"""
Exercice 3 : Projet Complet - Chiffre de César
Objectif : Créer une application complète avec gestion d'erreurs, tests et documentation
"""

print("=== EXERCICE 3 : PROJET COMPLET CHIFFRE DE CÉSAR ===\n")

# ============================================================================
# INSTRUCTIONS
# ============================================================================
"""
Vous allez créer une application complète de cryptage César avec :

1. FONCTIONS DE BASE (cryptage/décryptage)
   - crypter_cesar(texte, decalage)
   - decrypter_cesar(texte, decalage)
   - bruteforce_cesar(texte_crypte)

2. GESTION DES ERREURS
   - Validation des entrées utilisateur
   - Gestion des exceptions
   - Messages d'erreur clairs

3. TESTS UNITAIRES
   - Tests pour chaque fonction
   - Cas normaux, limites, erreurs

4. DOCUMENTATION
   - Docstrings complètes (PEP 257)
   - Commentaires utiles
   - README (en commentaire)

5. INTERFACE UTILISATEUR
   - Menu interactif
   - Options : crypter, décrypter, brute force, quitter
"""

# ============================================================================
# PARTIE 1 : FONCTIONS DE BASE
# ============================================================================

# TODO: Implémentez crypter_cesar avec docstring complète

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
    # TODO: Votre code ici
    pass


# TODO: Implémentez decrypter_cesar avec docstring complète

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
    # TODO: Votre code ici
    pass


# TODO: Implémentez bruteforce_cesar avec docstring complète

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
    # TODO: Votre code ici
    pass


# ============================================================================
# PARTIE 2 : FONCTIONS DE VALIDATION
# ============================================================================

# TODO: Implémentez valider_texte avec gestion d'erreurs

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
    # TODO: Votre code ici
    pass


# TODO: Implémentez valider_decalage avec gestion d'erreurs

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
    # TODO: Votre code ici
    pass


# TODO: Implémentez demander_texte avec boucle de validation

def demander_texte(message="Entrez le texte : "):
    """
    Demande un texte à l'utilisateur avec validation.

    Args:
        message (str): Message à afficher

    Returns:
        str: Texte valide saisi par l'utilisateur
    """
    # TODO: Votre code ici
    # Utilisez une boucle while True
    # Gérez les exceptions
    pass


# TODO: Implémentez demander_decalage avec boucle de validation

def demander_decalage(message="Entrez le décalage (0-25) : "):
    """
    Demande un décalage à l'utilisateur avec validation.

    Args:
        message (str): Message à afficher

    Returns:
        int: Décalage valide saisi par l'utilisateur
    """
    # TODO: Votre code ici
    pass


# ============================================================================
# PARTIE 3 : TESTS UNITAIRES
# ============================================================================

def test_crypter_cesar():
    """Tests de la fonction crypter_cesar"""
    print("🧪 Tests crypter_cesar...")

    # TODO: Ajoutez au moins 5 tests
    # - Cas normal
    # - Débordement alphabet
    # - Décalage 0
    # - Caractères spéciaux
    # - Majuscules/minuscules

    # Exemple :
    # assert crypter_cesar("abc", 3) == "def", "Test basique"

    print("✅ Tests crypter_cesar OK")


def test_decrypter_cesar():
    """Tests de la fonction decrypter_cesar"""
    print("🧪 Tests decrypter_cesar...")

    # TODO: Ajoutez au moins 3 tests
    # - Décryptage simple
    # - Symétrie (crypter puis décrypter)
    # - Cas limites

    print("✅ Tests decrypter_cesar OK")


def test_bruteforce_cesar():
    """Tests de la fonction bruteforce_cesar"""
    print("🧪 Tests bruteforce_cesar...")

    # TODO: Ajoutez au moins 2 tests
    # - Nombre de résultats = 26
    # - Texte original présent dans les résultats

    print("✅ Tests bruteforce_cesar OK")


def test_validation():
    """Tests des fonctions de validation"""
    print("🧪 Tests validation...")

    # TODO: Testez valider_texte et valider_decalage
    # - Cas valides
    # - Cas invalides (doivent lever des exceptions)

    print("✅ Tests validation OK")


def executer_tous_les_tests():
    """Exécute tous les tests du projet"""
    print("\n" + "=" * 60)
    print("EXÉCUTION DE TOUS LES TESTS")
    print("=" * 60)
    print()

    try:
        # test_crypter_cesar()
        # test_decrypter_cesar()
        # test_bruteforce_cesar()
        # test_validation()

        print("\n" + "=" * 60)
        print("🎉 TOUS LES TESTS RÉUSSIS !")
        print("=" * 60)

    except AssertionError as e:
        print(f"\n❌ ÉCHEC : {e}")
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")


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

    # TODO: Implémentez cette fonction
    # 1. Demander le texte (avec validation)
    # 2. Demander le décalage (avec validation)
    # 3. Crypter et afficher le résultat
    # 4. Gérer les erreurs

    pass


def option_decrypter():
    """Gère l'option de décryptage"""
    print("\n--- DÉCRYPTAGE ---")

    # TODO: Implémentez cette fonction
    # Similaire à option_crypter mais pour le décryptage

    pass


def option_bruteforce():
    """Gère l'option brute force"""
    print("\n--- BRUTE FORCE ---")

    # TODO: Implémentez cette fonction
    # 1. Demander le texte crypté
    # 2. Essayer tous les décalages
    # 3. Afficher tous les résultats
    # 4. Permettre à l'utilisateur de choisir le bon

    pass


def application_principale():
    """Application principale avec menu interactif"""
    print("Bienvenue dans l'application Chiffre de César !")

    while True:
        try:
            afficher_menu()
            choix = input("\nVotre choix (1-5) : ").strip()

            if choix == '1':
                # option_crypter()
                pass
            elif choix == '2':
                # option_decrypter()
                pass
            elif choix == '3':
                # option_bruteforce()
                pass
            elif choix == '4':
                # executer_tous_les_tests()
                pass
            elif choix == '5':
                print("\n👋 Au revoir !")
                break
            else:
                print("❌ Choix invalide. Choisissez entre 1 et 5.")

        except KeyboardInterrupt:
            print("\n\n👋 Interruption détectée. Au revoir !")
            break
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")


# ============================================================================
# PARTIE 5 : DOCUMENTATION (README en commentaire)
# ============================================================================

"""
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
5. **Documentation** : Docstrings complètes pour toutes les fonctions

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

[Votre nom]
Date : 2025-11-02
Version : 1.0

## Notes Techniques

- Gestion des majuscules et minuscules
- Préservation des caractères spéciaux (espaces, ponctuation, chiffres)
- Décalage peut être négatif (décryptage)
- Modulo 26 pour boucler sur l'alphabet
- Validation robuste des entrées
- Messages d'erreur clairs
"""

# ============================================================================
# PARTIE 6 : FONCTIONNALITÉS BONUS (OPTIONNEL)
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
    # TODO: BONUS - Implémentez cette fonction
    pass


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
    # TODO: BONUS - Implémentez cette fonction
    pass


def analyser_frequences(texte):
    """
    Analyse les fréquences des lettres dans un texte.

    Utile pour la cryptanalyse (aide au brute force).

    Args:
        texte (str): Texte à analyser

    Returns:
        dict: Dictionnaire {lettre: fréquence}
    """
    # TODO: BONUS - Implémentez cette fonction
    pass


# ============================================================================
# EXÉCUTION
# ============================================================================

if __name__ == "__main__":
    print(__doc__)

    # Mode développement : lancer les tests
    # executer_tous_les_tests()

    # Mode production : lancer l'application
    # application_principale()

    print("\n📝 Consignes :")
    print("1. Implémentez toutes les fonctions marquées TODO")
    print("2. Ajoutez des docstrings complètes partout")
    print("3. Écrivez des tests pour chaque fonction")
    print("4. Testez la gestion d'erreurs")
    print("5. Créez une interface utilisateur fluide")
    print("\n✨ Bon courage !")

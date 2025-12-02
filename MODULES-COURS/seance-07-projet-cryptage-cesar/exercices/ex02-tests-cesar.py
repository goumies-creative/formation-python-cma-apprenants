# -*- coding: utf-8 -*-
"""
Exercice 2 : Tests Unitaires pour le Chiffre de César
Objectif : Écrire des tests complets pour valider le cryptage César
"""

print("=== EXERCICE 2 : TESTS DU CHIFFRE DE CÉSAR ===\n")

# ============================================================================
# FONCTIONS DE BASE (fournies)
# ============================================================================

def crypter_cesar(texte, decalage):
    """
    Crypte un texte avec le chiffre de César.

    Args:
        texte (str): Texte à crypter
        decalage (int): Nombre de positions de décalage

    Returns:
        str: Texte crypté
    """
    if not texte:
        return ""

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
    Décrypte un texte crypté avec César.

    Args:
        texte (str): Texte crypté
        decalage (int): Décalage utilisé pour le cryptage

    Returns:
        str: Texte décrypté
    """
    return crypter_cesar(texte, -decalage)


# ============================================================================
# PARTIE 1 : TESTS DES CAS NORMAUX
# ============================================================================

print("--- PARTIE 1 : TESTS CAS NORMAUX ---\n")

# TODO: Créez une fonction test_crypter_cas_normaux() qui teste :
# - Cryptage de "abc" avec décalage 3 → "def"
# - Cryptage de "ABC" avec décalage 3 → "DEF"
# - Cryptage de "Hello" avec décalage 5 → "Mjqqt"
# - Cryptage de "Python" avec décalage 1 → "Qzuipo"

# Utilisez des assertions avec messages clairs

def test_crypter_cas_normaux():
    """Tests des cas normaux de cryptage"""
    print("🧪 Tests cas normaux...")

    # Test 1 : Minuscules simples
    # assert crypter_cesar("abc", 3) == "def", "abc + 3 devrait donner def"

    # Test 2 : Majuscules simples
    # assert crypter_cesar("ABC", 3) == "DEF", "ABC + 3 devrait donner DEF"

    # TODO: Ajoutez les autres tests

    print("✅ Tests cas normaux OK\n")


# ============================================================================
# PARTIE 2 : TESTS DES CAS LIMITES
# ============================================================================

print("--- PARTIE 2 : TESTS CAS LIMITES ---\n")

# TODO: Créez une fonction test_crypter_cas_limites() qui teste :
# - Texte vide "" → ""
# - Décalage 0 (aucun changement)
# - Décalage 26 (retour au début de l'alphabet)
# - Débordement : "xyz" + 3 → "abc"
# - Débordement majuscules : "XYZ" + 3 → "ABC"
# - Un seul caractère : "a" + 1 → "b"

def test_crypter_cas_limites():
    """Tests des cas limites"""
    print("🧪 Tests cas limites...")

    # Test 1 : Texte vide
    # assert crypter_cesar("", 5) == "", "Texte vide devrait rester vide"

    # Test 2 : Décalage 0
    # assert crypter_cesar("Hello", 0) == "Hello", "Décalage 0 = pas de changement"

    # TODO: Ajoutez les autres tests

    print("✅ Tests cas limites OK\n")


# ============================================================================
# PARTIE 3 : TESTS DES CARACTÈRES SPÉCIAUX
# ============================================================================

print("--- PARTIE 3 : TESTS CARACTÈRES SPÉCIAUX ---\n")

# TODO: Créez une fonction test_crypter_caracteres_speciaux() qui teste :
# - Espaces préservés : "Hello World" + 3 → "Khoor Zruog"
# - Ponctuation : "Hello!" + 3 → "Khoor!"
# - Chiffres : "Test123" + 5 → "Yjxy123"
# - Caractères mixtes : "A-B-C" + 1 → "B-C-D"

def test_crypter_caracteres_speciaux():
    """Tests avec caractères spéciaux"""
    print("🧪 Tests caractères spéciaux...")

    # Test 1 : Espaces
    # assert crypter_cesar("Hello World", 3) == "Khoor Zruog", "Espaces préservés"

    # TODO: Ajoutez les autres tests

    print("✅ Tests caractères spéciaux OK\n")


# ============================================================================
# PARTIE 4 : TESTS DU DÉCRYPTAGE
# ============================================================================

print("--- PARTIE 4 : TESTS DÉCRYPTAGE ---\n")

# TODO: Créez une fonction test_decrypter() qui teste :
# - Décryptage de "def" avec décalage 3 → "abc"
# - Décryptage de "Khoor" avec décalage 3 → "Hello"
# - Test de symétrie : crypter puis décrypter = texte original

def test_decrypter():
    """Tests du décryptage"""
    print("🧪 Tests décryptage...")

    # Test 1 : Décryptage simple
    # assert decrypter_cesar("def", 3) == "abc", "Décryptage de 'def'"

    # Test 2 : Symétrie (crypter puis décrypter)
    # texte_original = "Python est génial"
    # texte_crypte = crypter_cesar(texte_original, 7)
    # texte_decrypte = decrypter_cesar(texte_crypte, 7)
    # assert texte_decrypte == texte_original, "Symétrie cryptage/décryptage"

    # TODO: Ajoutez d'autres tests

    print("✅ Tests décryptage OK\n")


# ============================================================================
# PARTIE 5 : TESTS AVEC DÉCALAGES NÉGATIFS
# ============================================================================

print("--- PARTIE 5 : TESTS DÉCALAGES NÉGATIFS ---\n")

# TODO: Créez une fonction test_decalages_negatifs() qui teste :
# - Décalage -1 : "bcd" → "abc"
# - Décalage -3 : "def" → "abc"
# - Équivalence : décalage -1 = décalage 25

def test_decalages_negatifs():
    """Tests avec décalages négatifs"""
    print("🧪 Tests décalages négatifs...")

    # Test 1 : Décalage négatif simple
    # assert crypter_cesar("bcd", -1) == "abc", "Décalage -1"

    # Test 2 : Équivalence -1 et 25
    # resultat_neg = crypter_cesar("abc", -1)
    # resultat_pos = crypter_cesar("abc", 25)
    # assert resultat_neg == resultat_pos, "Décalage -1 = décalage 25"

    # TODO: Ajoutez d'autres tests

    print("✅ Tests décalages négatifs OK\n")


# ============================================================================
# PARTIE 6 : TESTS DE TOUS LES DÉCALAGES (BONUS)
# ============================================================================

print("--- PARTIE 6 : TESTS EXHAUSTIFS (BONUS) ---\n")

# TODO: Créez une fonction test_tous_decalages() qui :
# - Teste TOUS les décalages de 0 à 25
# - Vérifie que crypter puis décrypter = texte original
# - Utilise une boucle for

def test_tous_decalages():
    """Tests exhaustifs avec tous les décalages possibles"""
    print("🧪 Tests exhaustifs (26 décalages)...")

    textes_test = ["Hello", "Python", "ABC xyz", "Test123!"]

    # TODO: Pour chaque texte, tester tous les décalages de 0 à 25
    # for texte in textes_test:
    #     for decalage in range(26):
    #         # Crypter puis décrypter
    #         # Vérifier que le résultat = texte original

    print("✅ Tests exhaustifs OK\n")


# ============================================================================
# PARTIE 7 : SUITE DE TESTS COMPLÈTE
# ============================================================================

def executer_tous_les_tests():
    """Exécute tous les tests du module"""
    print("=" * 60)
    print("EXÉCUTION DE TOUS LES TESTS")
    print("=" * 60)
    print()

    try:
        # test_crypter_cas_normaux()
        # test_crypter_cas_limites()
        # test_crypter_caracteres_speciaux()
        # test_decrypter()
        # test_decalages_negatifs()
        # test_tous_decalages()

        print("=" * 60)
        print("🎉 TOUS LES TESTS RÉUSSIS !")
        print("=" * 60)

    except AssertionError as e:
        print(f"\n❌ ÉCHEC DU TEST : {e}")
        print("=" * 60)


# ============================================================================
# PARTIE 8 : FONCTION DE BRUTE FORCE (À TESTER)
# ============================================================================

print("--- PARTIE 8 : FONCTION BRUTE FORCE ---\n")

def bruteforce_cesar(texte_crypte):
    """
    Essaie tous les décalages possibles pour décrypter un texte.

    Args:
        texte_crypte (str): Texte crypté à décrypter

    Returns:
        list: Liste de tuples (decalage, texte_decrypte)
    """
    resultats = []
    for decalage in range(26):
        texte_decrypte = decrypter_cesar(texte_crypte, decalage)
        resultats.append((decalage, texte_decrypte))
    return resultats


# TODO: Créez une fonction test_bruteforce() qui teste :
# - La fonction retourne une liste de 26 résultats
# - Un des résultats contient le texte original
# - Les décalages vont de 0 à 25

def test_bruteforce():
    """Tests de la fonction brute force"""
    print("🧪 Tests brute force...")

    # Test 1 : Nombre de résultats
    # texte_crypte = crypter_cesar("Secret", 5)
    # resultats = bruteforce_cesar(texte_crypte)
    # assert len(resultats) == 26, "Devrait retourner 26 résultats"

    # Test 2 : Le texte original est dans les résultats
    # textes_decryptes = [texte for _, texte in resultats]
    # assert "Secret" in textes_decryptes, "Le texte original doit être trouvé"

    # TODO: Ajoutez d'autres tests

    print("✅ Tests brute force OK\n")


# ============================================================================
# EXÉCUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Décommentez les appels de fonctions pour tester")
    print("=" * 60)

    # Exécuter tous les tests
    # executer_tous_les_tests()

    # Ou tester individuellement
    # test_crypter_cas_normaux()
    # test_crypter_cas_limites()
    # test_crypter_caracteres_speciaux()
    # test_decrypter()
    # test_decalages_negatifs()
    # test_tous_decalages()
    # test_bruteforce()

    print("\n✨ Exercice terminé ! Comparez avec la solution.")

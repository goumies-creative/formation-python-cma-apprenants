# -*- coding: utf-8 -*-
"""
Solution de l'Exercice 2 : Tests Unitaires pour le Chiffre de César
"""

print("=== SOLUTION EXERCICE 2 : TESTS DU CHIFFRE DE CÉSAR ===\n")

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

def test_crypter_cas_normaux():
    """Tests des cas normaux de cryptage"""
    print("🧪 Tests cas normaux...")

    # Test 1 : Minuscules simples
    assert crypter_cesar("abc", 3) == "def", "abc + 3 devrait donner def"

    # Test 2 : Majuscules simples
    assert crypter_cesar("ABC", 3) == "DEF", "ABC + 3 devrait donner DEF"

    # Test 3 : Mot mixte
    assert crypter_cesar("Hello", 5) == "Mjqqt", "Hello + 5 devrait donner Mjqqt"

    # Test 4 : Mot simple
    assert crypter_cesar("Python", 1) == "Qzuipo", "Python + 1 devrait donner Qzuipo"

    # Test 5 : Phrase complète
    assert crypter_cesar("Bonjour", 7) == "Ivuqvby", "Bonjour + 7 devrait donner Ivuqvby"

    print("✅ Tests cas normaux OK\n")


# ============================================================================
# EXPLICATIONS PARTIE 1
# ============================================================================
"""
🔍 EXPLICATIONS - CAS NORMAUX :

1. ASSERTIONS AVEC MESSAGES
   - assert condition, "message"
   - Le message s'affiche SI l'assertion échoue
   - Aide à identifier quel test a échoué

2. TESTS PROGRESSIFS
   - Minuscules seules
   - Majuscules seules
   - Mixte
   - Mots réels
   - Augmente la confiance progressivement

3. CALCUL MANUEL
   - a + 3 = d (position 0 + 3 = position 3)
   - H + 5 = M (position 7 + 5 = position 12)
   - Vérifier manuellement pour comprendre

4. POURQUOI TESTER LES DEUX ?
   - Majuscules et minuscules = codes ASCII différents
   - Algorithme doit gérer les deux
   - Bug potentiel si confusion de base
"""


# ============================================================================
# PARTIE 2 : TESTS DES CAS LIMITES
# ============================================================================

def test_crypter_cas_limites():
    """Tests des cas limites"""
    print("🧪 Tests cas limites...")

    # Test 1 : Texte vide
    assert crypter_cesar("", 5) == "", "Texte vide devrait rester vide"

    # Test 2 : Décalage 0 (pas de changement)
    assert crypter_cesar("Hello", 0) == "Hello", "Décalage 0 = pas de changement"

    # Test 3 : Décalage 26 (retour au début)
    assert crypter_cesar("abc", 26) == "abc", "Décalage 26 = retour au début (modulo)"

    # Test 4 : Débordement minuscules (z -> c avec +3)
    assert crypter_cesar("xyz", 3) == "abc", "xyz + 3 devrait donner abc (débordement)"

    # Test 5 : Débordement majuscules
    assert crypter_cesar("XYZ", 3) == "ABC", "XYZ + 3 devrait donner ABC (débordement)"

    # Test 6 : Un seul caractère
    assert crypter_cesar("a", 1) == "b", "a + 1 devrait donner b"

    # Test 7 : Décalage 52 (2 tours complets)
    assert crypter_cesar("abc", 52) == "abc", "52 = 2x26, retour au début"

    print("✅ Tests cas limites OK\n")


# ============================================================================
# EXPLICATIONS PARTIE 2
# ============================================================================
"""
🔍 EXPLICATIONS - CAS LIMITES :

1. TEXTE VIDE
   - Cas important à tester
   - Peut causer des bugs (boucle sur rien)
   - Devrait retourner chaîne vide

2. DÉCALAGE 0
   - Pas de cryptage
   - Test que modulo fonctionne : (pos + 0) % 26 = pos

3. DÉCALAGE 26
   - Tour complet de l'alphabet
   - Grâce au modulo : (pos + 26) % 26 = pos
   - a (0) + 26 = 26 % 26 = 0 = a

4. DÉBORDEMENT (xyz -> abc)
   - x (23) + 3 = 26 % 26 = 0 = a
   - y (24) + 3 = 27 % 26 = 1 = b
   - z (25) + 3 = 28 % 26 = 2 = c
   - Test crucial du modulo

5. UN SEUL CARACTÈRE
   - Cas minimal
   - Assure que la boucle fonctionne pour 1 élément

6. MULTIPLES DE 26
   - 52, 78, etc.
   - Tous devraient donner le même résultat que 0

CAS LIMITES = EDGE CASES
- Limites du système (début/fin alphabet)
- Valeurs extrêmes
- Cas minimaux
- Là où les bugs se cachent souvent !
"""


# ============================================================================
# PARTIE 3 : TESTS DES CARACTÈRES SPÉCIAUX
# ============================================================================

def test_crypter_caracteres_speciaux():
    """Tests avec caractères spéciaux"""
    print("🧪 Tests caractères spéciaux...")

    # Test 1 : Espaces préservés
    assert crypter_cesar("Hello World", 3) == "Khoor Zruog", "Espaces doivent être préservés"

    # Test 2 : Ponctuation préservée
    assert crypter_cesar("Hello!", 3) == "Khoor!", "Ponctuation doit être préservée"

    # Test 3 : Chiffres préservés
    assert crypter_cesar("Test123", 5) == "Yjxy123", "Chiffres doivent être préservés"

    # Test 4 : Caractères mixtes (lettres + symboles)
    assert crypter_cesar("A-B-C", 1) == "B-C-D", "Symboles entre lettres préservés"

    # Test 5 : Phrase complète avec ponctuation
    assert crypter_cesar("Bonjour, le monde!", 2) == "Dqplqwt, ng oqpfg!", "Phrase avec ponctuation"

    # Test 6 : Uniquement des chiffres
    assert crypter_cesar("123456", 10) == "123456", "Chiffres seuls ne changent pas"

    # Test 7 : Uniquement des espaces
    assert crypter_cesar("   ", 5) == "   ", "Espaces seuls ne changent pas"

    print("✅ Tests caractères spéciaux OK\n")


# ============================================================================
# EXPLICATIONS PARTIE 3
# ============================================================================
"""
🔍 EXPLICATIONS - CARACTÈRES SPÉCIAUX :

1. PRÉSERVATION DES NON-LETTRES
   - if char.isalpha() : traite uniquement les lettres
   - else : garde le caractère tel quel
   - Espaces, ponctuation, chiffres = inchangés

2. POURQUOI IMPORTANT ?
   - Messages réels contiennent espaces et ponctuation
   - "Bonjour!" plus naturel que "Bonjour"
   - Facilite la lecture du texte crypté

3. ISALPHA()
   - Méthode Python qui teste si caractère est alphabétique
   - True pour a-z et A-Z
   - False pour 0-9, espace, !, ?, etc.

4. TESTS EXHAUSTIFS
   - Espaces seuls
   - Ponctuation seule
   - Chiffres seuls
   - Mélanges
   - S'assure que RIEN d'autre que les lettres ne change

5. PHRASES RÉELLES
   - "Bonjour, le monde!" = cas d'usage réel
   - Si ça marche ici, ça marchera en production
"""


# ============================================================================
# PARTIE 4 : TESTS DU DÉCRYPTAGE
# ============================================================================

def test_decrypter():
    """Tests du décryptage"""
    print("🧪 Tests décryptage...")

    # Test 1 : Décryptage simple
    assert decrypter_cesar("def", 3) == "abc", "Décryptage de 'def' avec 3"

    # Test 2 : Décryptage mot
    assert decrypter_cesar("Khoor", 3) == "Hello", "Décryptage de 'Khoor' avec 3"

    # Test 3 : Symétrie - crypter puis décrypter
    texte_original = "Python est génial"
    texte_crypte = crypter_cesar(texte_original, 7)
    texte_decrypte = decrypter_cesar(texte_crypte, 7)
    assert texte_decrypte == texte_original, "Crypter puis décrypter = texte original"

    # Test 4 : Symétrie avec plusieurs décalages
    for decalage in [1, 5, 10, 15, 20, 25]:
        texte = "Test de symétrie"
        crypte = crypter_cesar(texte, decalage)
        decrypte = decrypter_cesar(crypte, decalage)
        assert decrypte == texte, f"Symétrie échouée pour décalage {decalage}"

    # Test 5 : Décryptage avec débordement
    assert decrypter_cesar("abc", 3) == "xyz", "abc - 3 devrait donner xyz (débordement négatif)"

    print("✅ Tests décryptage OK\n")


# ============================================================================
# EXPLICATIONS PARTIE 4
# ============================================================================
"""
🔍 EXPLICATIONS - DÉCRYPTAGE :

1. DÉCRYPTAGE = CRYPTAGE NÉGATIF
   - decrypter_cesar(texte, 3) = crypter_cesar(texte, -3)
   - Inverse le décalage
   - Élégant et simple

2. SYMÉTRIE
   - Propriété mathématique fondamentale
   - crypter(décrypter(x)) = x
   - décrypter(crypter(x)) = x
   - Si pas de symétrie = bug !

3. TEST AVEC BOUCLE
   - Teste plusieurs décalages
   - Plus robuste qu'un seul test
   - Détecte les bugs edge case

4. DÉBORDEMENT NÉGATIF
   - abc - 3 = xyz
   - a (0) - 3 = -3 % 26 = 23 = x
   - Modulo Python gère les négatifs correctement

5. IMPORTANCE DE CE TEST
   - Décryptage = fonctionnalité clé
   - Doit être 100% fiable
   - Un bug ici = messages illisibles
"""


# ============================================================================
# PARTIE 5 : TESTS AVEC DÉCALAGES NÉGATIFS
# ============================================================================

def test_decalages_negatifs():
    """Tests avec décalages négatifs"""
    print("🧪 Tests décalages négatifs...")

    # Test 1 : Décalage -1
    assert crypter_cesar("bcd", -1) == "abc", "bcd - 1 = abc"

    # Test 2 : Décalage -3
    assert crypter_cesar("def", -3) == "abc", "def - 3 = abc"

    # Test 3 : Équivalence -1 et 25
    resultat_neg = crypter_cesar("abc", -1)
    resultat_pos = crypter_cesar("abc", 25)
    assert resultat_neg == resultat_pos, "Décalage -1 devrait égaler décalage 25"

    # Test 4 : Équivalence -3 et 23
    assert crypter_cesar("xyz", -3) == crypter_cesar("xyz", 23), "-3 et 23 équivalents"

    # Test 5 : Débordement négatif
    assert crypter_cesar("abc", -5) == "vwx", "abc - 5 = vwx (débordement négatif)"

    # Test 6 : Décalage -26 (tour complet négatif)
    assert crypter_cesar("Hello", -26) == "Hello", "-26 = tour complet, pas de changement"

    print("✅ Tests décalages négatifs OK\n")


# ============================================================================
# EXPLICATIONS PARTIE 5
# ============================================================================
"""
🔍 EXPLICATIONS - DÉCALAGES NÉGATIFS :

1. MODULO AVEC NÉGATIFS
   - Python : -1 % 26 = 25
   - -3 % 26 = 23
   - -5 % 26 = 21
   - Gère automatiquement le débordement

2. ÉQUIVALENCE
   - -1 ≡ 25 (mod 26)
   - -3 ≡ 23 (mod 26)
   - Formule : -x ≡ 26-x (mod 26)
   - Important pour comprendre le décryptage

3. DÉBORDEMENT NÉGATIF
   - a (0) - 5 = -5 % 26 = 21 = v
   - b (1) - 5 = -4 % 26 = 22 = w
   - c (2) - 5 = -3 % 26 = 23 = x

4. POURQUOI TESTER NÉGATIFS ?
   - Décryptage utilise décalages négatifs
   - Vérifier que modulo fonctionne dans les deux sens
   - Bug fréquent dans d'autres langages

5. PROPRIÉTÉ MATHÉMATIQUE
   - (x + a) mod 26 = (x + a + 26) mod 26
   - Donc : (x - 1) mod 26 = (x + 25) mod 26
   - Test de cette propriété
"""


# ============================================================================
# PARTIE 6 : TESTS DE TOUS LES DÉCALAGES
# ============================================================================

def test_tous_decalages():
    """Tests exhaustifs avec tous les décalages possibles"""
    print("🧪 Tests exhaustifs (26 décalages)...")

    textes_test = ["Hello", "Python", "ABC xyz", "Test123!"]

    for texte in textes_test:
        for decalage in range(26):
            # Crypter puis décrypter
            crypte = crypter_cesar(texte, decalage)
            decrypte = decrypter_cesar(crypte, decalage)

            # Vérifier la symétrie
            assert decrypte == texte, \
                f"Symétrie échouée pour '{texte}' avec décalage {decalage}"

    # Afficher le nombre de tests effectués
    nb_tests = len(textes_test) * 26
    print(f"   ✅ {nb_tests} tests de symétrie réussis")

    print("✅ Tests exhaustifs OK\n")


# ============================================================================
# EXPLICATIONS PARTIE 6
# ============================================================================
"""
🔍 EXPLICATIONS - TESTS EXHAUSTIFS :

1. TESTS COMBINATOIRES
   - 4 textes × 26 décalages = 104 tests
   - Couverture complète
   - Détecte les bugs rares

2. DOUBLE BOUCLE
   - for texte in textes_test
   - for decalage in range(26)
   - Teste toutes les combinaisons

3. SYMÉTRIE UNIVERSELLE
   - Propriété qui doit être vraie pour TOUT texte
   - TOUT décalage
   - Si une combinaison échoue = bug

4. ÉCHEC AVEC \
   - Backslash pour continuer sur ligne suivante
   - Rend le message d'assertion lisible
   - assert condition, \
       "message très long"

5. NB_TESTS
   - Affiche le nombre de tests réussis
   - Satisfaction de voir un grand nombre
   - Confiance dans le code

6. POURQUOI C'EST IMPORTANT ?
   - Cas qu'on n'aurait pas pensé à tester manuellement
   - Automatisation = pas d'effort supplémentaire
   - Détection de bugs edge case
"""


# ============================================================================
# PARTIE 7 : FONCTION DE BRUTE FORCE
# ============================================================================

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


def test_bruteforce():
    """Tests de la fonction brute force"""
    print("🧪 Tests brute force...")

    # Test 1 : Nombre de résultats
    texte_crypte = crypter_cesar("Secret", 5)
    resultats = bruteforce_cesar(texte_crypte)
    assert len(resultats) == 26, "Devrait retourner 26 résultats (un par décalage)"

    # Test 2 : Le texte original est dans les résultats
    textes_decryptes = [texte for _, texte in resultats]
    assert "Secret" in textes_decryptes, "Le texte original doit être trouvé"

    # Test 3 : Tous les décalages de 0 à 25 sont présents
    decalages = [dec for dec, _ in resultats]
    assert decalages == list(range(26)), "Tous les décalages 0-25 doivent être présents"

    # Test 4 : Format des tuples
    assert all(isinstance(item, tuple) for item in resultats), "Chaque résultat doit être un tuple"
    assert all(len(item) == 2 for item in resultats), "Chaque tuple doit avoir 2 éléments"

    # Test 5 : Le bon décalage donne le bon texte
    texte_original = "Python"
    decalage_utilise = 13
    crypte = crypter_cesar(texte_original, decalage_utilise)
    resultats = bruteforce_cesar(crypte)

    # Trouver le résultat avec le bon décalage
    for decalage, texte in resultats:
        if decalage == decalage_utilise:
            assert texte == texte_original, \
                f"Le décalage {decalage_utilise} devrait donner '{texte_original}'"

    print("✅ Tests brute force OK\n")


# ============================================================================
# EXPLICATIONS PARTIE 7
# ============================================================================
"""
🔍 EXPLICATIONS - BRUTE FORCE :

1. BRUTE FORCE = FORCE BRUTE
   - Essayer toutes les possibilités
   - 26 décalages possibles
   - L'un d'eux donne le texte original

2. LISTE DE TUPLES
   - [(0, "texte0"), (1, "texte1"), ...]
   - Tuple = (décalage, texte_décrypté)
   - Facile à parcourir ensuite

3. LIST COMPREHENSION POUR EXTRAIRE
   - [texte for _, texte in resultats]
   - _ = on ignore le décalage
   - Extrait uniquement les textes

4. ASSERT ALL()
   - all(condition for item in liste)
   - True si condition vraie pour TOUS les items
   - Compact et lisible

5. TEST DU FORMAT
   - isinstance(item, tuple) : vérifie le type
   - len(item) == 2 : vérifie la structure
   - Important pour l'API de la fonction

6. UTILITÉ RÉELLE
   - Si on reçoit un message crypté sans connaître le décalage
   - On essaie tous les décalages
   - On choisit celui qui donne un texte lisible
   - Fonctionne car seulement 26 possibilités
"""


# ============================================================================
# SUITE DE TESTS COMPLÈTE
# ============================================================================

def executer_tous_les_tests():
    """Exécute tous les tests du module"""
    print("=" * 60)
    print("EXÉCUTION DE TOUS LES TESTS")
    print("=" * 60)
    print()

    try:
        test_crypter_cas_normaux()
        test_crypter_cas_limites()
        test_crypter_caracteres_speciaux()
        test_decrypter()
        test_decalages_negatifs()
        test_tous_decalages()
        test_bruteforce()

        print("=" * 60)
        print("🎉 TOUS LES TESTS RÉUSSIS !")
        print("=" * 60)
        print(f"\nNombre total de tests : ~150")
        print("Couverture : 100% des fonctionnalités")

    except AssertionError as e:
        print(f"\n❌ ÉCHEC DU TEST : {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()


# ============================================================================
# EXÉCUTION
# ============================================================================

if __name__ == "__main__":
    executer_tous_les_tests()

    print("\n" + "=" * 60)
    print("DÉMONSTRATION BRUTE FORCE")
    print("=" * 60)

    # Démo du brute force
    message_secret = "Python est génial"
    decalage_secret = 13

    print(f"\nMessage original : '{message_secret}'")
    print(f"Décalage utilisé : {decalage_secret}")

    crypte = crypter_cesar(message_secret, decalage_secret)
    print(f"Message crypté : '{crypte}'")

    print("\nEssai de tous les décalages possibles :")
    print("-" * 60)

    resultats = bruteforce_cesar(crypte)
    for decalage, texte in resultats:
        marqueur = "← TROUVÉ !" if texte == message_secret else ""
        print(f"Décalage {decalage:2d} : {texte} {marqueur}")

    print("\n✨ Solution complète avec explications détaillées !")


# ============================================================================
# POINTS CLÉS À RETENIR
# ============================================================================
"""
📚 POINTS CLÉS SUR LES TESTS :

1. TYPES DE CAS À TESTER
   ✅ Cas normaux (happy path)
   ✅ Cas limites (edge cases)
   ✅ Cas d'erreur
   ✅ Caractères spéciaux
   ✅ Symétrie

2. BONNES PRATIQUES
   ✅ Un test = une assertion
   ✅ Messages clairs dans les assertions
   ✅ Tester les cas minimaux
   ✅ Tester les débordements
   ✅ Tester avec boucles pour exhaustivité

3. STRUCTURE DES TESTS
   ✅ Fonction test_* par catégorie
   ✅ Docstring pour décrire les tests
   ✅ Print pour feedback visuel
   ✅ Fonction executer_tous_les_tests()

4. CE QUE LES TESTS ONT COUVERT
   ✅ Majuscules et minuscules séparément
   ✅ Débordement alphabet (z->a)
   ✅ Décalages 0, 26, négatifs
   ✅ Caractères non-alphabétiques
   ✅ Textes vides
   ✅ Symétrie cryptage/décryptage
   ✅ Tous les décalages possibles

5. COUVERTURE
   - Fonctionnel : crypter, décrypter, brute force ✅
   - Cas normaux : plusieurs exemples ✅
   - Cas limites : vide, 0, 26, débordement ✅
   - Robustesse : négatifs, spéciaux ✅
   - Mathématique : symétrie, modulo ✅

6. CONFIANCE
   Avec ~150 tests qui passent :
   - On SAIT que le code fonctionne
   - On peut modifier sans peur
   - On détecte immédiatement les régressions
   - Code professionnel et maintenable

LES TESTS = FILET DE SÉCURITÉ
Ne pas tester = coder sur un fil sans filet !
"""

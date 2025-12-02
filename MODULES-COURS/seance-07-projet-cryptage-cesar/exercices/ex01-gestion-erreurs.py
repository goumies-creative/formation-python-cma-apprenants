# -*- coding: utf-8 -*-
"""
Exercice 1 : Gestion des Erreurs
Objectif : Maîtriser try/except et la validation des entrées utilisateur
"""

print("=== EXERCICE 1 : GESTION DES ERREURS ===\n")

# ============================================================================
# PARTIE 1 : CONVERSION SÉCURISÉE
# ============================================================================

print("--- PARTIE 1 : CONVERSION SÉCURISÉE ---\n")

# TODO: Créez une fonction demander_nombre() qui :
# - Demande un nombre à l'utilisateur
# - Utilise try/except pour gérer les erreurs de conversion
# - Redemande tant que l'entrée n'est pas valide
# - Retourne le nombre (int) une fois valide

def demander_nombre(message):
    """
    Demande un nombre à l'utilisateur avec validation.

    Args:
        message (str): Message à afficher

    Returns:
        int: Nombre saisi par l'utilisateur
    """
    # Votre code ici
    pass


# Tests de la fonction
if __name__ == "__main__":
    # Test 1 : Demander l'âge
    # age = demander_nombre("Votre âge : ")
    # print(f"✅ Âge enregistré : {age}\n")
    pass

# ============================================================================
# PARTIE 2 : DIVISION SÉCURISÉE
# ============================================================================

print("--- PARTIE 2 : DIVISION SÉCURISÉE ---\n")

# TODO: Créez une fonction diviser_secure() qui :
# - Prend deux paramètres : a et b
# - Gère l'exception ZeroDivisionError
# - Gère l'exception TypeError (si a ou b ne sont pas des nombres)
# - Retourne le résultat ou None en cas d'erreur

def diviser_secure(a, b):
    """
    Division sécurisée avec gestion des erreurs.

    Args:
        a (float): Numérateur
        b (float): Dénominateur

    Returns:
        float or None: Résultat de la division, ou None si erreur
    """
    # Votre code ici
    pass


# Tests
if __name__ == "__main__":
    print("Tests de diviser_secure :")
    # Test 1 : Division normale
    # print(f"10 / 2 = {diviser_secure(10, 2)}")

    # Test 2 : Division par zéro
    # print(f"10 / 0 = {diviser_secure(10, 0)}")

    # Test 3 : Type incorrect
    # print(f"10 / 'abc' = {diviser_secure(10, 'abc')}")
    print()


# ============================================================================
# PARTIE 3 : VALIDATION D'ÂGE AVEC RAISE
# ============================================================================

print("--- PARTIE 3 : VALIDATION AVEC RAISE ---\n")

# TODO: Créez une fonction valider_age() qui :
# - Prend un paramètre age
# - Vérifie que age est un entier (isinstance)
# - Lève TypeError si ce n'est pas un int
# - Lève ValueError si age < 0 ou age > 150
# - Retourne True si tout est valide

def valider_age(age):
    """
    Valide un âge.

    Args:
        age (int): Âge à valider

    Returns:
        bool: True si l'âge est valide

    Raises:
        TypeError: Si age n'est pas un entier
        ValueError: Si age est hors limites (< 0 ou > 150)
    """
    # Votre code ici
    pass


# Tests
if __name__ == "__main__":
    print("Tests de valider_age :")

    # Test 1 : Âge valide
    # try:
    #     print(f"Âge 25 : {valider_age(25)}")
    # except Exception as e:
    #     print(f"❌ Erreur : {e}")

    # Test 2 : Âge négatif
    # try:
    #     print(f"Âge -5 : {valider_age(-5)}")
    # except ValueError as e:
    #     print(f"❌ ValueError attendue : {e}")

    # Test 3 : Type incorrect
    # try:
    #     print(f"Âge 'vingt' : {valider_age('vingt')}")
    # except TypeError as e:
    #     print(f"❌ TypeError attendue : {e}")
    print()


# ============================================================================
# PARTIE 4 : CALCULATRICE AVEC GESTION COMPLÈTE
# ============================================================================

print("--- PARTIE 4 : CALCULATRICE ROBUSTE ---\n")

# TODO: Créez une fonction calculatrice() qui :
# - Demande deux nombres à l'utilisateur
# - Demande une opération (+, -, *, /)
# - Gère TOUTES les erreurs possibles :
#   * ValueError (conversion impossible)
#   * ZeroDivisionError (division par zéro)
#   * Opération invalide
# - Utilise une boucle pour permettre plusieurs calculs
# - Utilise 'q' pour quitter

def calculatrice():
    """
    Calculatrice interactive avec gestion complète des erreurs.
    """
    print("🧮 CALCULATRICE ROBUSTE")
    print("=" * 40)
    print("Opérations disponibles : +, -, *, /")
    print("Tapez 'q' pour quitter\n")

    # Votre code ici
    pass


# ============================================================================
# PARTIE 5 : VALIDATION D'EMAIL (BONUS)
# ============================================================================

print("--- PARTIE 5 : VALIDATION D'EMAIL (BONUS) ---\n")

# TODO: Créez une fonction demander_email() qui :
# - Demande un email à l'utilisateur
# - Vérifie que l'email contient @ et .
# - Vérifie que l'email n'est pas vide
# - Vérifie que le domaine (après @) contient un .
# - Redemande tant que l'email n'est pas valide
# - Retourne l'email valide

def demander_email():
    """
    Demande un email avec validation basique.

    Returns:
        str: Email valide
    """
    # Votre code ici
    pass


# Tests
if __name__ == "__main__":
    # Test de l'email
    # email = demander_email()
    # print(f"✅ Email enregistré : {email}\n")
    pass


# ============================================================================
# TESTS FINAUX
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TESTS DE VALIDATION")
    print("=" * 60)

    # Décommentez pour tester vos fonctions

    # print("\n1. Test demander_nombre :")
    # try:
    #     nb = demander_nombre("Entrez un nombre : ")
    #     print(f"✅ Nombre valide : {nb}")
    # except Exception as e:
    #     print(f"❌ Erreur : {e}")

    # print("\n2. Test diviser_secure :")
    # print(f"   15 / 3 = {diviser_secure(15, 3)}")
    # print(f"   10 / 0 = {diviser_secure(10, 0)}")

    # print("\n3. Test valider_age :")
    # try:
    #     valider_age(30)
    #     print("   ✅ Âge 30 valide")
    # except Exception as e:
    #     print(f"   ❌ {e}")

    # try:
    #     valider_age(-10)
    #     print("   ❌ Âge -10 devrait être invalide")
    # except ValueError:
    #     print("   ✅ Âge -10 correctement rejeté")

    # print("\n4. Test calculatrice :")
    # calculatrice()

    print("\n✨ Exercice terminé ! Vérifiez vos solutions.")

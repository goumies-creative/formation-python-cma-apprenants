# -*- coding: utf-8 -*-
"""
Solution de l'Exercice 1 : Gestion des Erreurs
"""

print("=== SOLUTION EXERCICE 1 : GESTION DES ERREURS ===\n")

# ============================================================================
# PARTIE 1 : CONVERSION SÉCURISÉE
# ============================================================================

print("--- PARTIE 1 : CONVERSION SÉCURISÉE ---\n")


def demander_nombre(message):
    """
    Demande un nombre à l'utilisateur avec validation.

    Args:
        message (str): Message à afficher

    Returns:
        int: Nombre saisi par l'utilisateur
    """
    while True:
        try:
            nombre = int(input(message))
            return nombre
        except ValueError:
            print("❌ Erreur : Veuillez entrer un nombre valide")


# ============================================================================
# EXPLICATIONS PARTIE 1
# ============================================================================
"""
🔍 EXPLICATIONS :

1. BOUCLE INFINIE (while True)
   - Continue jusqu'à obtenir une valeur valide
   - Sort uniquement avec return

2. TRY/EXCEPT
   - try : Tente la conversion en int
   - except ValueError : Capture l'erreur si la conversion échoue
   - Message d'erreur clair pour l'utilisateur

3. RETURN DANS TRY
   - Si conversion réussit, on retourne immédiatement
   - Si échec, on reste dans la boucle

EXEMPLE D'EXÉCUTION :
> Votre âge : abc
❌ Erreur : Veuillez entrer un nombre valide
> Votre âge : vingt
❌ Erreur : Veuillez entrer un nombre valide
> Votre âge : 25
✅ Âge enregistré : 25
"""


# Tests
if __name__ == "__main__":
    print("Test demander_nombre :")
    print("(Testez avec : 'abc', 'vingt', puis '25')")
    # age = demander_nombre("Votre âge : ")
    # print(f"✅ Âge enregistré : {age}\n")


# ============================================================================
# PARTIE 2 : DIVISION SÉCURISÉE
# ============================================================================

print("--- PARTIE 2 : DIVISION SÉCURISÉE ---\n")


def diviser_secure(a, b):
    """
    Division sécurisée avec gestion des erreurs.

    Args:
        a (float): Numérateur
        b (float): Dénominateur

    Returns:
        float or None: Résultat de la division, ou None si erreur
    """
    try:
        resultat = a / b
        return resultat

    except ZeroDivisionError:
        print("❌ Erreur : Division par zéro impossible")
        return None

    except TypeError:
        print("❌ Erreur : Les deux valeurs doivent être des nombres")
        return None


# ============================================================================
# EXPLICATIONS PARTIE 2
# ============================================================================
"""
🔍 EXPLICATIONS :

1. MULTIPLES EXCEPTIONS
   - Premier except : Gère division par zéro
   - Deuxième except : Gère types incorrects (ex: int / str)
   - Ordre n'a pas d'importance ici (exceptions différentes)

2. RETOUR DE None
   - Convention Python pour signaler un échec
   - Permet à l'appelant de tester : if resultat is not None

3. MESSAGES CLAIRS
   - Chaque erreur a son propre message
   - L'utilisateur sait exactement ce qui ne va pas

POURQUOI PLUSIEURS EXCEPT ?
- Plus spécifique = meilleur debugging
- Messages d'erreur adaptés
- Code plus maintenable
"""


# Tests
if __name__ == "__main__":
    print("Tests de diviser_secure :")

    # Test 1 : Division normale
    print(f"10 / 2 = {diviser_secure(10, 2)}")

    # Test 2 : Division par zéro
    print(f"10 / 0 = {diviser_secure(10, 0)}")

    # Test 3 : Type incorrect
    print(f"10 / 'abc' = {diviser_secure(10, 'abc')}")
    print()


# ============================================================================
# PARTIE 3 : VALIDATION D'ÂGE AVEC RAISE
# ============================================================================

print("--- PARTIE 3 : VALIDATION AVEC RAISE ---\n")


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
    # Vérification du type
    if not isinstance(age, int):
        raise TypeError(f"L'âge doit être un entier, pas {type(age).__name__}")

    # Vérification des limites
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")

    if age > 150:
        raise ValueError("L'âge ne peut pas dépasser 150 ans")

    return True


# ============================================================================
# EXPLICATIONS PARTIE 3
# ============================================================================
"""
🔍 EXPLICATIONS :

1. RAISE = CRÉER UNE EXCEPTION
   - Interrompt l'exécution de la fonction
   - L'appelant doit gérer l'exception (try/except)

2. ISINSTANCE POUR LE TYPE
   - isinstance(age, int) : True si age est un int
   - Plus pythonique que type(age) == int
   - Gère aussi les sous-classes

3. QUAND UTILISER RAISE ?
   - Données invalides passées à une fonction
   - Pré-conditions non respectées
   - Situations exceptionnelles

4. DOCSTRING RAISES
   - Documente les exceptions possibles
   - Aide les utilisateurs de la fonction

FLOW :
valider_age("25") → TypeError levée → except TypeError la capture
valider_age(-5)   → ValueError levée → except ValueError la capture
valider_age(25)   → return True → Pas d'exception
"""


# Tests
if __name__ == "__main__":
    print("Tests de valider_age :")

    # Test 1 : Âge valide
    try:
        print(f"Âge 25 : {valider_age(25)}")
    except Exception as e:
        print(f"❌ Erreur : {e}")

    # Test 2 : Âge négatif
    try:
        print(f"Âge -5 : {valider_age(-5)}")
    except ValueError as e:
        print(f"✅ ValueError attendue : {e}")

    # Test 3 : Type incorrect
    try:
        print(f"Âge 'vingt' : {valider_age('vingt')}")
    except TypeError as e:
        print(f"✅ TypeError attendue : {e}")

    # Test 4 : Âge trop élevé
    try:
        print(f"Âge 200 : {valider_age(200)}")
    except ValueError as e:
        print(f"✅ ValueError attendue : {e}")

    print()


# ============================================================================
# PARTIE 4 : CALCULATRICE AVEC GESTION COMPLÈTE
# ============================================================================

print("--- PARTIE 4 : CALCULATRICE ROBUSTE ---\n")


def calculatrice():
    """
    Calculatrice interactive avec gestion complète des erreurs.
    """
    print("🧮 CALCULATRICE ROBUSTE")
    print("=" * 40)
    print("Opérations disponibles : +, -, *, /")
    print("Tapez 'q' pour quitter\n")

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    while True:
        try:
            # Demander premier nombre
            entree = input("\nPremier nombre (ou 'q' pour quitter) : ").strip()

            # Vérifier si l'utilisateur veut quitter
            if entree.lower() == 'q':
                print("\n👋 Au revoir !")
                break

            # Convertir en nombre
            num1 = float(entree)

            # Demander l'opération
            op = input("Opération (+, -, *, /) : ").strip()

            # Vérifier que l'opération est valide
            if op not in operations:
                print(f"❌ Opération '{op}' non reconnue. Utilisez +, -, *, ou /")
                continue

            # Demander second nombre
            num2 = float(input("Second nombre : "))

            # Calculer
            resultat = operations[op](num1, num2)
            print(f"✅ Résultat : {num1} {op} {num2} = {resultat}")

        except ValueError:
            print("❌ Erreur : Veuillez entrer un nombre valide")

        except ZeroDivisionError:
            print("❌ Erreur : Division par zéro impossible")

        except KeyboardInterrupt:
            print("\n\n👋 Interruption détectée. Au revoir !")
            break

        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

        finally:
            # Séparateur pour clarté
            print("-" * 40)


# ============================================================================
# EXPLICATIONS PARTIE 4
# ============================================================================
"""
🔍 EXPLICATIONS :

1. DICTIONNAIRE D'OPÉRATIONS
   - Clé : symbole de l'opération
   - Valeur : fonction lambda
   - Plus élégant que des if/elif multiples

2. VÉRIFICATION DE QUIT
   - Avant la conversion en float
   - Sinon, 'q' causerait une ValueError

3. VALIDATION DE L'OPÉRATION
   - if op not in operations : vérifie si l'opération existe
   - continue : retourne au début de la boucle

4. FINALLY
   - S'exécute toujours (erreur ou pas)
   - Ici : affiche le séparateur pour la lisibilité

5. KeyboardInterrupt
   - Exception levée quand l'utilisateur tape Ctrl+C
   - Permet de quitter proprement

FLOW TYPIQUE :
1. Utilisateur entre "10"
2. Utilisateur entre "+"
3. Utilisateur entre "5"
4. Calcul : 10 + 5 = 15
5. Affichage du résultat
6. Retour au début de la boucle

FLOW AVEC ERREUR :
1. Utilisateur entre "abc"
2. ValueError levée lors de float(entree)
3. except ValueError capture
4. Message d'erreur affiché
5. Retour au début de la boucle
"""


# ============================================================================
# PARTIE 5 : VALIDATION D'EMAIL (BONUS)
# ============================================================================

print("--- PARTIE 5 : VALIDATION D'EMAIL (BONUS) ---\n")


def demander_email():
    """
    Demande un email avec validation basique.

    Returns:
        str: Email valide
    """
    while True:
        email = input("Votre email : ").strip()

        # Validation 1 : Email non vide
        if not email:
            print("❌ L'email ne peut pas être vide")
            continue

        # Validation 2 : Contient @
        if '@' not in email:
            print("❌ L'email doit contenir un @")
            continue

        # Validation 3 : Domaine contient un point
        try:
            partie_locale, domaine = email.split('@')

            if not partie_locale:
                print("❌ La partie avant @ ne peut pas être vide")
                continue

            if '.' not in domaine:
                print("❌ Le domaine doit contenir un point (ex: .com)")
                continue

            if not domaine.split('.')[-1]:
                print("❌ L'extension ne peut pas être vide (ex: .com)")
                continue

        except ValueError:
            print("❌ Format d'email invalide (plusieurs @ détectés)")
            continue

        # Toutes les validations passées
        return email


# ============================================================================
# EXPLICATIONS PARTIE 5
# ============================================================================
"""
🔍 EXPLICATIONS :

1. STRIP()
   - Enlève les espaces au début et à la fin
   - " test@mail.com " → "test@mail.com"

2. VALIDATIONS PROGRESSIVES
   - Vide ? → Message spécifique
   - Pas de @ ? → Message spécifique
   - Domaine invalide ? → Message spécifique
   - Plus facile à débugger

3. SPLIT('@')
   - Divise l'email en deux parties
   - "test@mail.com" → ["test", "mail.com"]
   - ValueError si plusieurs @ (email@test@mail.com)

4. CONTINUE
   - Retourne au début de la boucle
   - Ne sort que quand toutes les validations passent

5. VALIDATION BASIQUE
   - Pas de regex (trop complexe pour débutants)
   - Suffisant pour 90% des cas
   - Validation complète = regex ou librairie email-validator

EXEMPLES :
✅ "test@mail.com"      → Valide
✅ "alice@example.fr"   → Valide
❌ "test"               → Pas de @
❌ "test@"              → Domaine vide
❌ "test@mail"          → Pas de point dans domaine
❌ "@mail.com"          → Partie locale vide
❌ "test@@mail.com"     → Plusieurs @
"""


# Tests
if __name__ == "__main__":
    print("Test demander_email :")
    print("(Testez avec : 'test', 'test@', 'test@mail', puis 'test@mail.com')")
    # email = demander_email()
    # print(f"✅ Email enregistré : {email}\n")


# ============================================================================
# TESTS FINAUX
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TESTS DE VALIDATION")
    print("=" * 60)

    print("\n1. Test demander_nombre :")
    try:
        # nb = demander_nombre("Entrez un nombre : ")
        # print(f"✅ Nombre valide : {nb}")
        print("(Décommentez pour tester)")
    except Exception as e:
        print(f"❌ Erreur : {e}")

    print("\n2. Test diviser_secure :")
    print(f"   15 / 3 = {diviser_secure(15, 3)}")
    print(f"   10 / 0 = {diviser_secure(10, 0)}")
    print(f"   10 / 'abc' = {diviser_secure(10, 'abc')}")

    print("\n3. Test valider_age :")
    try:
        valider_age(30)
        print("   ✅ Âge 30 valide")
    except Exception as e:
        print(f"   ❌ {e}")

    try:
        valider_age(-10)
        print("   ❌ Âge -10 devrait être invalide")
    except ValueError:
        print("   ✅ Âge -10 correctement rejeté")

    try:
        valider_age("vingt")
        print("   ❌ Âge 'vingt' devrait être invalide")
    except TypeError:
        print("   ✅ Âge 'vingt' correctement rejeté")

    print("\n4. Test calculatrice :")
    print("   (Décommentez pour tester)")
    # calculatrice()

    print("\n5. Test demander_email :")
    print("   (Décommentez pour tester)")
    # email = demander_email()
    # print(f"   ✅ Email : {email}")

    print("\n" + "=" * 60)
    print("✨ SOLUTION COMPLÈTE")
    print("=" * 60)


# ============================================================================
# POINTS CLÉS À RETENIR
# ============================================================================
"""
📚 POINTS CLÉS :

1. TRY/EXCEPT
   - Gérer les erreurs prévisibles
   - Éviter les plantages
   - Messages clairs

2. BOUCLE DE VALIDATION (while True)
   - Continue jusqu'à valeur valide
   - Sort avec return ou break
   - Pattern très courant

3. RAISE
   - Créer des exceptions personnalisées
   - Documenter dans docstring (Raises)
   - Pour les pré-conditions

4. MULTIPLE EXCEPT
   - Une exception = un except
   - Messages spécifiques
   - Ordre important (du plus spécifique au plus général)

5. FINALLY
   - S'exécute TOUJOURS
   - Nettoyage de ressources
   - Fermeture de fichiers/connexions

6. VALIDATION PROGRESSIVE
   - Vérifier une chose à la fois
   - Messages d'erreur précis
   - Facile à maintenir

7. EXCEPTIONS COURANTES
   - ValueError : Valeur invalide
   - TypeError : Type incorrect
   - ZeroDivisionError : Division par zéro
   - KeyboardInterrupt : Ctrl+C

BONNES PRATIQUES :
✅ Messages d'erreur clairs et spécifiques
✅ Une exception = une cause
✅ Documenter les exceptions dans docstrings
✅ Valider tôt, échouer tôt
✅ Utiliser isinstance() pour vérifier les types
✅ strip() pour nettoyer les entrées utilisateur
✅ continue pour retenter, raise pour signaler un problème
"""

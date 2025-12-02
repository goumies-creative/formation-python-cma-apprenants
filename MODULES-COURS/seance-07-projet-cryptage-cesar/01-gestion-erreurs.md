# Gestion des Erreurs en Python

## Objectifs

- Comprendre les exceptions et leur rôle dans un programme
- Maîtriser la structure try/except/finally
- Connaître les types d'exceptions courantes
- Créer et lever ses propres exceptions
- Valider les entrées utilisateur de manière robuste
- Appliquer les techniques de debugging

## Introduction / Métaphore

### Les Erreurs = Signaux Routiers

Imaginez conduire sur une route. Vous voyez un panneau "Déviation - Route fermée". Que faites-vous ?
1. **Option A (sans gestion d'erreur)** : Vous foncez dans le mur. CRASH. Fin du programme.
2. **Option B (avec gestion d'erreur)** : Vous voyez le panneau, prenez la déviation, arrivez à destination.

**En Python, c'est pareil :**
- **Sans try/except** : Le programme plante à la première erreur.
- **Avec try/except** : Le programme gère l'erreur et continue.

```python
# Sans gestion d'erreur : CRASH
nombre = int("abc")  # ❌ ValueError: invalid literal
# Le programme s'arrête brutalement

# Avec gestion d'erreur : DÉVIATION
try:
    nombre = int("abc")
except ValueError:
    print("Désolé, je ne peux pas convertir 'abc' en nombre")
    nombre = 0  # Valeur par défaut
# Le programme continue tranquillement
```

## Concept Fondamental : Les Exceptions

### Qu'est-ce qu'une Exception ?

Une **exception** est un événement qui interrompt le flux normal d'un programme. Elle signale qu'une erreur s'est produite.

### Types d'Exceptions Courantes

| Exception | Cause | Exemple |
|-----------|-------|---------|
| `ValueError` | Valeur inappropriée | `int("abc")` |
| `TypeError` | Type inapproprié | `"5" + 5` |
| `KeyError` | Clé absente dans dictionnaire | `dico["cle_inexistante"]` |
| `IndexError` | Index hors limites | `liste[100]` sur liste de 3 éléments |
| `ZeroDivisionError` | Division par zéro | `10 / 0` |
| `FileNotFoundError` | Fichier introuvable | `open("inexistant.txt")` |
| `AttributeError` | Attribut inexistant | `"texte".methode_qui_existe_pas()` |

## La Structure try/except

### Syntaxe de Base

```python
try:
    # Code qui PEUT provoquer une erreur
    resultat = 10 / 0
except ZeroDivisionError:
    # Code exécuté SI l'erreur se produit
    print("Impossible de diviser par zéro !")
    resultat = None
```

### Exemple Progressif : Conversion d'Entrée

```python
# Version 1 : Sans gestion d'erreur (fragile)
age = int(input("Votre âge : "))
# Si l'utilisateur tape "vingt", le programme PLANTE

# Version 2 : Avec gestion d'erreur (robuste)
try:
    age = int(input("Votre âge : "))
    print(f"Vous avez {age} ans")
except ValueError:
    print("❌ Veuillez entrer un nombre valide")
    age = None
```

### Capturer Plusieurs Exceptions

```python
def diviser(a, b):
    """Division sécurisée avec gestion d'erreurs"""
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        print("❌ Erreur : Division par zéro impossible")
        return None
    except TypeError:
        print("❌ Erreur : Les deux valeurs doivent être des nombres")
        return None

# Tests
print(diviser(10, 2))      # 5.0
print(diviser(10, 0))      # Message d'erreur, retourne None
print(diviser(10, "abc"))  # Message d'erreur, retourne None
```

### Exception Générique (à utiliser avec précaution)

```python
try:
    # Code risqué
    valeur = int(input("Entrez un nombre : "))
    resultat = 100 / valeur
except Exception as e:
    # Capture TOUTES les exceptions
    print(f"❌ Une erreur s'est produite : {e}")
    print(f"Type d'erreur : {type(e).__name__}")
```

**⚠️ Attention :** Capturer `Exception` capture TOUT. Préférez des exceptions spécifiques quand c'est possible.

## La Clause else

La clause `else` s'exécute **seulement si aucune exception n'est levée**.

```python
try:
    age = int(input("Votre âge : "))
except ValueError:
    print("❌ Âge invalide")
else:
    # Exécuté UNIQUEMENT si la conversion a réussi
    print(f"✅ Âge valide : {age} ans")
    if age >= 18:
        print("Vous êtes majeur")
```

## La Clause finally

La clause `finally` s'exécute **TOUJOURS**, qu'il y ait eu erreur ou non.

**Utilité :** Nettoyer les ressources (fermer fichiers, connexions réseau, etc.)

```python
fichier = None
try:
    fichier = open("donnees.txt", "r")
    contenu = fichier.read()
    print(contenu)
except FileNotFoundError:
    print("❌ Fichier introuvable")
finally:
    # Exécuté TOUJOURS (erreur ou pas)
    if fichier:
        fichier.close()
        print("🔒 Fichier fermé proprement")
```

### Structure Complète try/except/else/finally

```python
def lire_nombre():
    """Lit un nombre avec gestion complète des erreurs"""
    try:
        nombre = int(input("Entrez un nombre : "))
    except ValueError:
        print("❌ Erreur : Ce n'est pas un nombre valide")
        return None
    else:
        # Exécuté SI pas d'erreur
        print(f"✅ Nombre valide : {nombre}")
        return nombre
    finally:
        # Exécuté TOUJOURS
        print("🔄 Fin de la saisie")

# Test
resultat = lire_nombre()
```

## Lever des Exceptions : raise

Parfois, **vous voulez créer une erreur** pour signaler un problème.

### Syntaxe raise

```python
def verifier_age(age):
    """Vérifie qu'un âge est valide"""
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")
    if age > 150:
        raise ValueError("L'âge ne peut pas dépasser 150 ans")
    return True

# Utilisation
try:
    verifier_age(-5)
except ValueError as e:
    print(f"❌ Erreur : {e}")
```

### Créer ses Propres Exceptions

```python
class AgeInvalideError(Exception):
    """Exception personnalisée pour les âges invalides"""
    pass

def verifier_age(age):
    """Vérifie qu'un âge est valide"""
    if not isinstance(age, int):
        raise TypeError("L'âge doit être un nombre entier")
    if age < 0:
        raise AgeInvalideError("L'âge ne peut pas être négatif")
    if age > 150:
        raise AgeInvalideError("L'âge ne peut pas dépasser 150 ans")
    return True

# Utilisation
try:
    verifier_age(-10)
except AgeInvalideError as e:
    print(f"❌ Âge invalide : {e}")
except TypeError as e:
    print(f"❌ Type incorrect : {e}")
```

## Validation des Entrées Utilisateur

### Pattern : Boucle de Validation

```python
def demander_nombre(message, min_valeur=None, max_valeur=None):
    """
    Demande un nombre à l'utilisateur avec validation

    Args:
        message (str): Message à afficher
        min_valeur (int): Valeur minimale acceptée
        max_valeur (int): Valeur maximale acceptée

    Returns:
        int: Nombre valide saisi par l'utilisateur
    """
    while True:
        try:
            nombre = int(input(message))

            # Validation des limites
            if min_valeur is not None and nombre < min_valeur:
                print(f"❌ Le nombre doit être >= {min_valeur}")
                continue

            if max_valeur is not None and nombre > max_valeur:
                print(f"❌ Le nombre doit être <= {max_valeur}")
                continue

            return nombre

        except ValueError:
            print("❌ Veuillez entrer un nombre valide")

# Utilisation
age = demander_nombre("Votre âge : ", min_valeur=0, max_valeur=150)
print(f"✅ Âge enregistré : {age}")
```

### Pattern : Validation d'Email Basique

```python
def demander_email():
    """Demande un email avec validation basique"""
    while True:
        email = input("Votre email : ").strip()

        # Validations
        if not email:
            print("❌ L'email ne peut pas être vide")
            continue

        if '@' not in email:
            print("❌ L'email doit contenir un @")
            continue

        if '.' not in email.split('@')[1]:
            print("❌ L'email doit avoir un domaine valide (ex: .com)")
            continue

        return email

# Utilisation
email = demander_email()
print(f"✅ Email valide : {email}")
```

## Techniques de Debugging

### 1. Messages de Debug avec print()

```python
def calculer_moyenne(notes):
    """Calcule la moyenne avec messages de debug"""
    print(f"🐛 DEBUG: notes reçues = {notes}")

    if not notes:
        print("🐛 DEBUG: Liste vide détectée")
        raise ValueError("La liste ne peut pas être vide")

    total = sum(notes)
    print(f"🐛 DEBUG: total = {total}")

    moyenne = total / len(notes)
    print(f"🐛 DEBUG: moyenne = {moyenne}")

    return moyenne
```

### 2. Assertions pour les Conditions

```python
def calculer_moyenne(notes):
    """Calcule la moyenne avec assertions"""
    assert isinstance(notes, list), "notes doit être une liste"
    assert len(notes) > 0, "La liste ne peut pas être vide"
    assert all(isinstance(n, (int, float)) for n in notes), "Toutes les notes doivent être des nombres"

    return sum(notes) / len(notes)

# Test
try:
    moyenne = calculer_moyenne([15, 18, "abc"])
except AssertionError as e:
    print(f"❌ Assertion échouée : {e}")
```

### 3. Module traceback pour Analyse d'Erreurs

```python
import traceback

def fonction_problematique():
    """Fonction qui génère une erreur"""
    return 10 / 0

try:
    fonction_problematique()
except Exception as e:
    print("❌ Erreur capturée")
    print(f"Type : {type(e).__name__}")
    print(f"Message : {e}")
    print("\n📋 Traceback complet :")
    traceback.print_exc()
```

## Bonnes Pratiques

### ✅ À FAIRE

```python
# 1. Être spécifique dans les exceptions
try:
    valeur = int(texte)
except ValueError:  # ✅ Spécifique
    print("Erreur de conversion")

# 2. Logger les erreurs
import logging

try:
    resultat = operation_risquee()
except Exception as e:
    logging.error(f"Erreur dans operation_risquee : {e}")

# 3. Nettoyer les ressources avec finally
try:
    fichier = open("data.txt")
    # Traitement
finally:
    fichier.close()  # ✅ Toujours exécuté
```

### ❌ À ÉVITER

```python
# 1. Exception trop large
try:
    valeur = int(texte)
except:  # ❌ Capture TOUT, même KeyboardInterrupt
    print("Erreur")

# 2. Exceptions vides
try:
    operation_dangereuse()
except Exception:
    pass  # ❌ Erreur silencieuse = bug impossible à trouver

# 3. Utiliser les exceptions pour le flux normal
try:
    if cle in dico:
        valeur = dico[cle]
except KeyError:  # ❌ Pas pour le flux normal
    valeur = None
```

## Exercice Pratique : Calculatrice Robuste

```python
def calculatrice():
    """Calculatrice avec gestion complète des erreurs"""
    print("🧮 CALCULATRICE ROBUSTE")
    print("=" * 40)

    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }

    while True:
        try:
            # Saisie premier nombre
            num1 = float(input("\nPremier nombre (ou 'q' pour quitter) : "))

            # Saisie opération
            op = input("Opération (+, -, *, /) : ").strip()
            if op not in operations:
                raise ValueError(f"Opération '{op}' non reconnue")

            # Saisie second nombre
            num2 = float(input("Second nombre : "))

            # Calcul
            resultat = operations[op](num1, num2)
            print(f"✅ Résultat : {num1} {op} {num2} = {resultat}")

        except ValueError as e:
            if "could not convert" in str(e):
                choix = input("").lower()
                if choix == 'q':
                    print("Au revoir !")
                    break
                print("❌ Veuillez entrer un nombre valide")
            else:
                print(f"❌ Erreur : {e}")

        except ZeroDivisionError:
            print("❌ Division par zéro impossible")

        except KeyboardInterrupt:
            print("\n👋 Interruption détectée. Au revoir !")
            break

        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

        finally:
            print("-" * 40)

# Lancer la calculatrice
if __name__ == "__main__":
    calculatrice()
```

## Checklist de Maîtrise

- [ ] Je comprends ce qu'est une exception
- [ ] Je sais utiliser try/except pour capturer des erreurs
- [ ] Je connais les exceptions courantes (ValueError, TypeError, etc.)
- [ ] Je sais utiliser else et finally
- [ ] Je peux lever des exceptions avec raise
- [ ] Je peux créer des exceptions personnalisées
- [ ] Je sais valider les entrées utilisateur en boucle
- [ ] Je peux utiliser des assertions pour débugger
- [ ] J'applique les bonnes pratiques de gestion d'erreurs

**Les erreurs ne sont pas vos ennemies - elles sont des indicateurs pour rendre votre code plus robuste !**

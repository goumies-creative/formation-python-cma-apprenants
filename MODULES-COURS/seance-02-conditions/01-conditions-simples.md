# Conditions Simples et Input Utilisateur

## Objectifs

- Comprendre la structure if/else
- Utiliser les opérateurs de comparaison
- Interagir avec l'utilisateur via input()
- Valider les entrées utilisateur

## Structure de Base if/else

### Syntaxe de base
```python
if condition:
    # Code exécuté si condition est True
    print("La condition est vraie")
else:
    # Code exécuté si condition est False
    print("La condition est fausse")
```

### Exemple concret
```python
age = 20

if age >= 18:
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")
``` 

## Opérateurs de Comparaison
### Comparaisons de base
```python
# Égalité
10 == 10    # True
10 == 5     # False

# Inégalité
10 != 5     # True
10 != 10    # False

# Comparaisons numériques
10 > 5      # True
10 < 5      # False
10 >= 10    # True
10 <= 5     # False
``` 

### Comparaisons de chaînes
```python
# Comparaison lexicographique
"apple" == "apple"    # True
"apple" == "banana"   # False
"a" < "b"             # True
"apple" < "banana"    # True
``` 

## Interaction avec l'Utilisateur
### La fonction input()
```python
# Saisie simple
nom = input("Entrez votre nom : ")
print(f"Bonjour {nom}!")

# Conversion des entrées
age = int(input("Entrez votre âge : "))
prix = float(input("Entrez le prix : "))
```

### Validation basique
```python
# Validation d'âge
age = int(input("Entrez votre âge : "))

if age < 0:
    print("Âge invalide !")
elif age < 18:
    print("Vous êtes mineur")
elif age < 65:
    print("Vous êtes adulte")
else:
    print("Vous êtes senior")
```

## Structures if/elif/else
### Conditions multiples
```python
note = int(input("Entrez votre note (0-20) : "))

if note >= 16:
    print("Excellent !")
elif note >= 14:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

### Conditions imbriquées
```python
age = int(input("Entrez votre âge : "))
a_permis = input("Avez-vous le permis ? (oui/non) : ").lower() == "oui"

if age >= 18:
    if a_permis:
        print("Vous pouvez conduire !")
    else:
        print("Vous êtes majeur mais n'avez pas le permis")
else:
    print("Vous êtes mineur, vous ne pouvez pas conduire")
```

## Bonnes Pratiques
### Conditions claires
```python
# Bon
if est_majeur and a_permis:
    print("Peut conduire")

# Confus
if age >= 18 and permis == True:
    print("Peut conduire")
```

### Validation des entrées
```python
try:
    age = int(input("Entrez votre âge : "))
    if age < 0 or age > 120:
        print("Âge invalide")
    else:
        print(f"Vous avez {age} ans")
except ValueError:
    print("Veuillez entrer un nombre valide")
```

## Exercices Pratiques
### Exercice 1 : Calculateur de majorité
```python
age = int(input("Quel âge avez-vous ? "))

if age >= 18:
    print("Vous êtes majeur !")
else:
    annees_restantes = 18 - age
    print(f"Vous serez majeur dans {annees_restantes} an(s)")
```

### Exercice 2 : Convertisseur température
```python
temperature = float(input("Entrez la température : "))
unite = input("Est-ce en C ou F ? ").upper()

if unite == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C = {fahrenheit}°F")
elif unite == "F":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F = {celsius}°C")
else:
    print("Unité non reconnue")
```

### Exercice 3 : Validateur de mot de passe
```python
mot_de_passe = input("Créez un mot de passe : ")

if len(mot_de_passe) < 8:
    print("Le mot de passe doit faire au moins 8 caractères")
elif mot_de_passe.isnumeric():
    print("Le mot de passe ne doit pas être uniquement des chiffres")
elif mot_de_passe.isalpha():
    print("Le mot de passe doit contenir des chiffres et des lettres")
else:
    print("Mot de passe valide !")
```

## Pièges Courants
### Comparaison vs assignation
```python
# ❌ Erreur courante
if age = 18:    # SyntaxError!
    print("18 ans")

# ✅ Correct
if age == 18:
    print("18 ans")
```

### Comparaison de types différents
```python
# ❌ Comportement inattendu
"10" == 10      # False

# ✅ Conversion si nécessaire
int("10") == 10  # True
```

## Checklist de Maîtrise
- Je maîtrise la syntaxe if/elif/else
- Je connais tous les opérateurs de comparaison
- Je sais utiliser input() pour interagir avec l'utilisateur
- Je peux valider les entrées utilisateur
- J'évite les pièges courants des conditions

**Les conditions donnent vie à vos programmes en leur permettant de prendre des décisions !**
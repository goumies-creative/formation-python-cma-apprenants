# VS Code pour Python

## Pourquoi VS Code ?

**Visual Studio Code** est l'éditeur que nous utiliserons car il est :
- **Gratuit** et open source
- **Excellent pour Python** avec de superbes extensions
- **Extensible** avec des milliers d'extensions
- **Multiplateforme** (Windows, Mac, Linux)
- **Parfait pour les débutants** et les experts

## Première Ouverture

### Lancement de VS Code
```bash
# Depuis le terminal :
code .

# Ou ouvrez VS Code et :
# Fichier → Ouvrir un dossier → formation-python-cma
```

### Interface Principale
1. Barre d'activité (à gauche) :
   - Explorateur de fichiers
   - Recherche
   - Débogage
   - Extensions
2. Éditeur (au centre) :
   - Où vous écrivez votre code
   - Coloration syntaxique
   - Auto-complétion

3. Panels (en bas) :
   - Terminal intégré
   - Problèmes
   - Sortie

4. Barre d'état (en bas) :
- Version Python
- Encodage
- Retour chariot

###  Extensions Essentielles
- Déjà installées par nos scripts :
- Python (Microsoft) - Support complet Python
- Pylance (Microsoft) - Intelligence artificielle pour le code
- Black Formatter - Formatage automatique du code
- GitLens - Superpouvoirs pour Git
- French Language Pack - Interface en français

### Vérification des extensions :
1. Cliquez sur l'icône Extensions (carrés)
2. Recherchez "Python"
3. Vérifiez que c'est installé

### Configuration Python
#### Sélection de l'interpréteur
1. Ouvrez un fichier .py
2. En bas à gauche : cliquez sur la version Python
3. Choisissez Python 3.11.x

### Création d'un premier fichier
1. Clic droit dans l'explorateur → "Nouveau fichier"
2. Nommez-le hello.py
3. Écrivez votre premier code :

```python
print("Bonjour VS Code !")
print("Je suis prêt(e) pour la formation Python CMA !")

# Calcul simple
resultat = 5 + 3
print(f"5 + 3 = {resultat}")
```

### Exécution du Code
### Méthode 1 : Terminal intégré
1. Ouvrez le terminal : Ctrl + ù (Windows) ou Cmd + ù (Mac)
2. Exécutez :

```bash
python hello.py
# ou
python3 hello.py
```

### Méthode 2 : Bouton Run
1. Cliquez sur le triangle ▶️ en haut à droite
2. Le code s'exécute dans le terminal intégré

### Méthode 3 : Débogage (avancé)
1. Cliquez sur l'icône bug
2. Créez un launch configuration
3. Lancez le débogage

## Fonctionnalités Magiques
### Auto-complétion
- Tapez pri puis Tab → print()
- Tapez for puis Tab → complète la boucle for
- Ctrl + Espace : force les suggestions

### Coloration syntaxique
```python
# Les couleurs vous aident à comprendre la structure
def calculer_moyenne(nombres):
    """Calcule la moyenne d'une liste de nombres"""
    if not nombres:
        return 0
    return sum(nombres) / len(nombres)
```

### Formatage automatique
1. Écrivez du code mal indenté
2. Sauvegardez (Ctrl + S)
3. Black reformate automatiquement !

### Recherche et remplacement
- `Ctrl + F` : Rechercher dans le fichier
- `Ctrl + H` : Rechercher et remplacer
- `Ctrl + Shift + F` : Rechercher dans tous les fichiers

## Exercices Pratiques
### Exercice 1 : Exploration de l'interface
1. Ouvrez VS Code dans votre dossier formation-python-cma
2. Créez la structure de dossiers :
   - seance-00/
   - seance-01/
   - projets/
3. Créez un fichier presentation.py dans seance-00/

### Exercice 2 : Premier programme
Dans `presentation.py` :

```python
# Présentation personnelle
nom = "Votre Prénom"
age = 25  # Remplacez par votre âge
ville = "Paris"

print("=== Présentation ===")
print(f"Je m'appelle {nom}")
print(f"J'ai {age} ans")
print(f"Je vis à {ville}")
print("Je suis en formation Python CMA !")

# Calcul de l'année de naissance
from datetime import datetime
annee_actuelle = datetime.now().year
annee_naissance = annee_actuelle - age
print(f"Je suis né(e) en {annee_naissance}")
```

### Exercice 3 : Exploration des extensions
1. Ouvrez les extensions (icône carrés)
2. Recherchez "Python" et explorez les fonctionnalités
3. Testez l'auto-complétion sur votre code
4. Vérifiez que le formatage automatique fonctionne

## Raccourcis Clavier Essentiels
### Navigation
- `Ctrl + P` : Ouvrir un fichier rapidement
- `Ctrl + Shift + E` : Explorateur de fichiers
- `Ctrl + B` : Montrer/cacher la barre latérale

### Édition
- `Ctrl + S` : Sauvegarder
- `Ctrl + Z` : Annuler
- `Ctrl + Y` : Rétablir
- `Ctrl + D` : Sélectionner le mot suivant identique
- `Ctrl + /` : Commenter/décommenter

### Terminal
- `Ctrl + ù` : Ouvrir/fermer le terminal

- `Ctrl + Shift + ù` : Nouveau terminal

### Débogage de Base
#### Méthode simple : print()
```python
def calcul_complexe(a, b):
    print(f"DEBUG: a={a}, b={b}")  # Voir les valeurs
    resultat = a * b + 10
    print(f"DEBUG: résultat={resultat}")  # Voir le calcul
    return resultat

# Test
calcul_complexe(5, 3)
```

#### Points d'arrêt (avancé)
1. Cliquez dans la marge à gauche des numéros de ligne
2. Un point rouge apparaît
3. Lancez le débogage (F5)
4. Le programme s'arrête à cette ligne

### Problèmes Courants
#### "Python not found"
- Vérifiez que Python est installé
- Sélectionnez l'interpréteur en bas à gauche
- Redémarrez VS Code

### Extensions non chargées
- Allez dans Extensions
- Rechargez l'extension
- Redémarrez VS Code

### Terminal ne fonctionne pas
- Menu Terminal → Nouveau Terminal
- Vérifiez que Python est dans le PATH

## Checklist de Maîtrise
- Je sais ouvrir VS Code dans mon dossier projet
- Je sais créer et éditer des fichiers Python
- Je sais exécuter mon code depuis VS Code
- J'utilise l'auto-complétion
- Je bénéficie du formatage automatique
- Je me sers du terminal intégré
- Je sais déboguer avec print()

## Bonnes Pratiques
### Organisation
- Un dossier par projet
- Des sous-dossiers par séance
- Noms de fichiers clairs et descriptifs

### Édition
- Sauvegardez souvent (`Ctrl + S`)
- Utilisez l'auto-complétion
- Laissez Black formater votre code
- Testez régulièrement votre code

### Workflow
- Ouvrir VS Code dans le bon dossier
- Éditer le code avec toutes les aides
- Tester dans le terminal intégré
- Sauvegarder et commiter avec Git

VS Code est maintenant votre meilleur allié pour coder !

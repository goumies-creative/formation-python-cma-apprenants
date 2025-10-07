# Premiers Pas avec Git

## Qu'est-ce que Git ?

**Git** est un système de contrôle de version qui permet de :
- Sauvegarder l'historique de votre code
- Travailler à plusieurs sur le même projet
- ⏪ Revenir en arrière si vous faites une erreur
- Suivre l'évolution de votre projet

## Métaphore de l'Appareil Photo

Imaginez Git comme un appareil photo :
- **`git add`** = Préparer la scène, placer les personnes
- **`git commit`** = Prendre la photo
- **`git log`** = Feuilleter l'album photo
- **`git push`** = Envoyer les photos dans le cloud

## ⚙️ Configuration Initiale
### Configuration de votre identité
```bash
git config --global user.name "Votre Prénom Nom"
git config --global user.email "votre.email@example.com"
```

### Vérification
```bash
git config --list
# Doit afficher votre nom et email
```

### Configuration supplémentaire (optionnelle)
```bash
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

## Premier Repository
1. Créer un dossier pour le projet
```bash
mkdir mon-premier-projet
cd mon-premier-projet
```
2. Initialiser Git
```bash
git init
# Crée un repository Git vide
```
3. Vérifier le statut
```bash
git status
# Affiche l'état des fichiers
```
4. Créer un premier fichier
```bash
echo "# Mon Premier Projet" > README.md
```
5. Vérifier à nouveau le statut
```bash
git status
# README.md apparaît en rouge = non suivi
```

### Premier Commit
1. Ajouter le fichier à la zone de préparation
```bash
git add README.md
# Ou pour ajouter tous les fichiers :
git add .
```
2. Vérifier le statut
```bash
git status
# README.md apparaît en vert = prêt à être commité
```
3. Faire le commit (prendre la photo)
```bash
git commit -m "Premier commit : README initial"
```
4. Vérifier l'historique
```bash
git log
# Affiche l'historique des commits
```

## Exercices Pratiques
### Exercice 1 : Configuration et Premier Projet
```bash
# 1. Configurer Git
git config --global user.name "Marie Dupont"
git config --global user.email "marie.dupont@cma-paris.fr"

# 2. Créer un projet
mkdir formation-python
cd formation-python

# 3. Initialiser Git
git init

# 4. Créer un fichier
echo "# Ma Formation Python" > README.md

# 5. Premier commit
git add .
git commit -m "Initialisation projet formation"
```

### Exercice 2 : Travail Quotidien
```bash
# 1. Créer un fichier Python
touch hello.py

# 2. Éditer le fichier (avec VS Code)
code hello.py
# Ajouter : print("Hello Git!")

# 3. Vérifier le statut
git status

# 4. Ajouter le fichier
git add hello.py

# 5. Faire un commit descriptif
git commit -m "Ajout script hello.py avec message de bienvenue"

# 6. Vérifier l'historique
git log --oneline
```

### Exercice 3 : Modifications et Historique
```bash
# 1. Modifier README.md
echo "## Progression" >> README.md
echo "- [x] Séance 0 : Installfest" >> README.md

# 2. Voir les modifications
git diff

# 3. Ajouter et commiter
git add README.md
git commit -m "Ajout progression séance 0 dans README"

# 4. Voir l'historique détaillé
git log --stat
```

## Commandes Essentielles
### Statut et Information
```bash
git status                    # État des fichiers
git log                       # Historique complet
git log --oneline            # Historique condensé
git log --stat               # Historique avec modifications
git show                     # Dernier commit en détail
```

### Ajout et Commit
```bash
git add fichier.py           # Ajouter un fichier spécifique
git add .                    # Ajouter tous les fichiers modifiés
git commit -m "Message"      # Commiter avec un message
git commit -am "Message"     # Ajouter ET commiter (fichiers suivis)
```
### Annulation (si besoin)
```bash
git restore fichier.py       # Annuler modifications d'un fichier
git restore --staged fichier.py # Retirer un fichier de la zone de préparation
git reset --soft HEAD~1      # Annuler le dernier commit mais garder modifications
```

### Bonnes Pratiques
Messages de commit clairs
```bash
# ❌ Mauvais
git commit -m "fix"

# ✅ Bon
git commit -m "Correction bug calcul moyenne dans stats.py"

# ✅ Excellent
git commit -m "Fix: calcul moyenne incorrect avec liste vide

- Gestion cas liste vide dans calculate_moyenne()
- Ajout test unitaire pour cas limite
- Mise à jour documentation fonction"
```

### Fréquence des commits
- Commitez souvent : après chaque petite fonctionnalité
- Messages descriptifs : expliquez POURQUOI vous avez fait ces changements
- Un commit = une idée : ne mélangez pas plusieurs modifications sans rapport

## Pièges Courants
### Oubli de git add
```bash
# ❌ Modification faite mais...
git commit -m "Modifications"
# → "rien à commiter"

# ✅
git add .
git commit -m "Modifications"
```

### Mauvais dossier
```bash
# ❌
cd /mauvais/dossier
git init
# Git initialisé au mauvais endroit

# ✅
cd /bon/dossier/projet
git init
```

### Fichiers non suivis
```bash
# Création fichier
touch nouveau.py
git status
# → "untracked files"

# Pour le suivre :
git add nouveau.py
```

## Checklist de Maîtrise
- Je sais configurer Git avec mon identité
- Je sais initialiser un repository
- Je sais vérifier le statut avec `git status`
- Je sais ajouter des fichiers avec `git add`
- Je sais faire des commits avec `git commit`
- Je sais consulter l'historique avec `git log`
- J'écris des messages de commit descriptifs
- Je commite régulièrement

## Workflow de Base
Le workflow Git de base que vous utiliserez quotidiennement :
1. Travailler : Éditer des fichiers
2. Vérifier : git status pour voir les modifications
3. Préparer : git add . pour ajouter les changements
4. Sauvegarder : git commit -m "Message clair"
5. Vérifier : git log pour confirmer

Répétez ce cycle souvent !

## Prochaines Étapes
- Dans les séances suivantes, vous apprendrez :
- Travailler avec les branches
- Utiliser GitHub pour sauvegarder en ligne
- Collaborer avec d'autres développeurs
- Gérer les conflits

Vous maîtrisez maintenant les bases de Git !

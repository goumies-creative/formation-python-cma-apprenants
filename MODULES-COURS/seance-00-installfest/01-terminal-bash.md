# Terminal Bash - Commandes Essentielles

## Pourquoi le Terminal ?

Le terminal (ou ligne de commande) est l'outil de base des développeurs. Il permet de :
- Naviguer rapidement dans les fichiers
- Automatiser des tâches
- Utiliser des outils comme Git
- Exécuter des programmes

## Métaphore du Bâtiment

Imaginez que votre ordinateur est un bâtiment :
- **Dossiers** = Pièces et étages
- **Fichiers** = Objets dans les pièces
- **Terminal** = Vous qui vous déplacez dans le bâtiment

## Commandes de Base

### Où suis-je ? → `pwd`
```bash
pwd
# Affiche : /Users/votrenom
# Vous dit dans quel dossier vous êtes
```

### Que vois-je ? → `ls`
```bash
ls          # Liste les fichiers visibles
ls -l       # Liste détaillée (permissions, taille)
ls -la      # Liste TOUS les fichiers (y compris cachés)
ls Documents # Liste le contenu du dossier Documents
```

### Je me déplace → `cd`
```bash
cd Documents                    # Entre dans Documents
cd ..                          # Remonte d'un niveau
cd ~                           # Retourne au dossier personnel
cd /                           # Va à la racine du système
cd -                           # Retourne au dossier précédent
```

### Je crée → `mkdir` et `touch`
```bash
mkdir mon-projet               # Crée un dossier "mon-projet"
mkdir -p projet/sous-dossier   # Crée toute l'arborescence
touch fichier.txt              # Crée un fichier vide
touch script.py readme.md      # Crée plusieurs fichiers
```

### Je manipule → `cp`, `mv`, `rm`
```bash
cp fichier.txt copie.txt       # Copie un fichier
cp -r dossier/ nouveau-dossier/ # Copie un dossier entier

mv ancien.txt nouveau.txt      # Renomme un fichier
mv fichier.txt dossier/        # Déplace un fichier

rm fichier.txt                 # Supprime un fichier
rm -r dossier/                 # Supprime un dossier (ATTENTION !)
```

### Je regarde → `cat`, `head`, `tail`
```bash
cat fichier.txt                # Affiche tout le contenu
head -5 fichier.txt            # Affiche les 5 premières lignes
tail -3 fichier.txt            # Affiche les 3 dernières lignes
```

## Exercices Pratiques
### Exercice 1 : Exploration
```bash
# 1. Où suis-je ?
pwd

# 2. Que contient ce dossier ?
ls -la

# 3. Allons dans le dossier Documents
cd Documents

# 4. Créons un dossier pour la formation
mkdir formation-python-cma

# 5. Entrons dans ce dossier
cd formation-python-cma
```

### Exercice 2 : Organisation
```bash
# 1. Créons la structure de dossiers
mkdir seance-00 seance-01 seance-02 seance-03 projets

# 2. Allons dans seance-00
cd seance-00

# 3. Créons quelques fichiers
touch notes.md exercice-terminal.py

# 4. Retournons au dossier formation-python-cma
cd ..

# 5. Vérifions la structure créée
ls -R
```

### Exercice 3 : Manipulation
```bash
# 1. Créons un fichier test
echo "Hello Terminal!" > test.txt

# 2. Lisons son contenu
cat test.txt

# 3. Faisons une copie
cp test.txt backup.txt

# 4. Renommons le fichier original
mv test.txt bonjour.txt

# 5. Vérifions
ls
cat bonjour.txt
cat backup.txt
```

## Astuces Utiles
### Auto-complétion
Appuyez sur TAB pour compléter automatiquement :
```bash
cd Docu[TAB] → cd Documents/
ls Dow[TAB] → ls Downloads/
```

### Historique des commandes
- Flèche haut/bas : Naviguer dans l'historique
- `history` : Voir toutes les commandes récentes
- `Ctrl + R` : Rechercher dans l'historique

### Commandes utiles
```bash
clear                         # Nettoie l'écran
whoami                        # Affiche votre nom d'utilisateur
date                          # Affiche la date et l'heure
which python                  # Montre où est installé Python
```

## Pièges à Éviter
### Attention à `rm -r`
```bash
# ❌ DANGEREUX - supprime tout sans confirmation
rm -rf /

# ✅ Plus sûr - demande confirmation
rm -ri dossier/
```

### Chemins relatifs vs absolus
```bash
# Relatif (depuis l'endroit où vous êtes)
cd Documents
./mon-script.py

# Absolu (depuis n'importe où)
cd /Users/votrenom/Documents
/Users/votrenom/Documents/mon-script.py
```

### Checklist de Maîtrise
[] Je sais me repérer avec pwd
[] Je sais lister les fichiers avec ls
[] Je sais naviguer avec cd
[] Je sais créer dossiers/fichiers avec mkdir/touch
[] Je sais copier/déplacer avec cp/mv
[] J'utilise TAB pour l'auto-complétion
[] Je fais attention avec rm

###  Pratique Quotidienne
**Pendant la formation, utilisez le terminal pour :**
- Naviguer dans vos projets
- Lancer vos scripts Python
- Utiliser Git
- Installer des packages

**Plus vous pratiquerez, plus cela deviendra naturel !**


# Pip et Packages Externes

## Objectifs

- Comprendre l'écosystème PyPI
- Maîtriser l'outil pip
- Installer et gérer des packages externes
- Créer et utiliser requirements.txt
- Gérer les versions de packages

## Introduction / Métaphore

### Le Magasin d'Applications

**PyPI** (Python Package Index) est comme un **App Store gigantesque** pour Python avec plus de 500 000 packages gratuits !

**pip** est votre assistant personnel qui :
- 🔍 Trouve les packages que vous voulez
- 📥 Les télécharge et les installe
- 🔄 Les met à jour
- 🗑️ Les désinstalle proprement

```python
# Sans package externe : des centaines de lignes de code
def telecharger_page_web(url):
    # Code complexe avec sockets, HTTP, encodage...
    pass

# Avec le package 'requests' : 2 lignes !
import requests
response = requests.get('https://example.com')
```

## Concept Fondamental : PyPI et pip

### PyPI (Python Package Index)

**Site web :** [pypi.org](https://pypi.org/)

PyPI héberge des packages créés par la communauté mondiale de développeurs Python.

**Exemples populaires :**
- `requests` : pour faire des requêtes HTTP simplement
- `pandas` : pour analyser des données
- `flask` : pour créer des applications web
- `pytest` : pour tester votre code
- `pillow` : pour manipuler des images

### pip (Package Installer for Python)

**pip** est installé automatiquement avec Python et permet de gérer les packages.

## Syntaxe de Base

### 1. Vérifier que pip est installé

```bash
# Vérifier la version de pip
pip --version

# Ou avec Python
python -m pip --version
```

### 2. Installer un package

```bash
# Syntaxe de base
pip install nom_du_package

# Exemples
pip install requests
pip install colorama
pip install pillow
```

### 3. Lister les packages installés

```bash
pip list

# Affiche quelque chose comme :
# Package    Version
# ---------- -------
# pip        23.0.1
# requests   2.31.0
# colorama   0.4.6
```

### 4. Afficher les infos d'un package

```bash
pip show requests

# Affiche :
# Name: requests
# Version: 2.31.0
# Summary: Python HTTP for Humans.
# Location: /usr/lib/python3/...
```

### 5. Mettre à jour un package

```bash
# Mettre à jour un package spécifique
pip install --upgrade requests

# Mettre à jour pip lui-même
pip install --upgrade pip
```

### 6. Désinstaller un package

```bash
pip uninstall requests

# Avec confirmation automatique
pip uninstall -y requests
```

## Exemples Progressifs

### Exemple 1 : Package colorama (couleurs terminal)

```bash
# Installation
pip install colorama
```

```python
from colorama import Fore, Back, Style, init

# Initialiser colorama
init(autoreset=True)

# Texte en couleur
print(Fore.RED + "Erreur : Fichier introuvable")
print(Fore.GREEN + "✅ Opération réussie")
print(Fore.YELLOW + "⚠️ Attention : Espace disque faible")

# Texte avec fond coloré
print(Back.BLUE + Fore.WHITE + "Message important")

# Style gras/dim
print(Style.BRIGHT + "Texte en gras")
print(Style.DIM + "Texte atténué")

# Combinaisons
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "🎨 Super stylé !")
```

### Exemple 2 : Versions Spécifiques

```bash
# Installer une version précise
pip install requests==2.28.0

# Installer une version minimale
pip install requests>=2.28.0

# Installer une version dans une plage
pip install "requests>=2.28.0,<3.0.0"
```

### Exemple 3 : Installation Multiple

```bash
# Installer plusieurs packages en une commande
pip install requests colorama pillow

# Installer depuis requirements.txt
pip install -r requirements.txt
```

## Requirements.txt : Le Fichier de Dépendances

### Pourquoi requirements.txt ?

Imaginez que vous partagez votre projet avec un collègue. Au lieu de lui dire :
> "Installe requests version 2.31.0, colorama 0.4.6, et pillow 10.0.0"

Vous créez un fichier `requirements.txt` et il tape juste :
```bash
pip install -r requirements.txt
```

### Créer un requirements.txt

#### Méthode 1 : Automatique
```bash
# Générer depuis les packages installés
pip freeze > requirements.txt
```

Contenu généré :
```
certifi==2023.7.22
charset-normalizer==3.2.0
colorama==0.4.6
idna==3.4
requests==2.31.0
urllib3==2.0.4
```

#### Méthode 2 : Manuel (recommandé)
```
# requirements.txt
# Packages essentiels pour mon projet

requests==2.31.0
colorama==0.4.6
pillow>=10.0.0
```

### Utiliser requirements.txt

```bash
# Installer toutes les dépendances listées
pip install -r requirements.txt

# Mettre à jour toutes les dépendances
pip install --upgrade -r requirements.txt
```

### Bonnes Pratiques

```
# ✅ BON requirements.txt
# Liste claire et commentée

# Requêtes HTTP
requests==2.31.0

# Couleurs dans le terminal
colorama==0.4.6

# Manipulation d'images
pillow>=10.0.0,<11.0.0

# Tests
pytest>=7.0.0
```

## Pattern Courant : Projet avec Dépendances

### Structure d'un Projet

```
mon_projet/
├── requirements.txt     # Dépendances
├── README.md           # Documentation
├── src/
│   ├── __init__.py
│   └── main.py
└── tests/
    └── test_main.py
```

### Workflow Complet

```bash
# 1. Créer le projet
mkdir mon_projet
cd mon_projet

# 2. Créer requirements.txt
echo "requests==2.31.0" > requirements.txt
echo "colorama==0.4.6" >> requirements.txt

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Développer...

# 5. Ajouter une nouvelle dépendance
pip install pillow
pip freeze > requirements.txt  # Mettre à jour

# 6. Partager le projet
# Commit requirements.txt avec Git
```

## Packages Populaires à Connaître

### Utilitaires Généraux

```python
# colorama - Couleurs terminal
from colorama import Fore
print(Fore.GREEN + "Succès !")

# python-dotenv - Variables d'environnement
from dotenv import load_dotenv
load_dotenv()

# tqdm - Barres de progression
from tqdm import tqdm
for i in tqdm(range(100)):
    # Traitement...
    pass
```

### Manipulation de Données

```python
# pandas - Analyse de données
import pandas as pd
df = pd.read_csv('data.csv')

# numpy - Calculs numériques
import numpy as np
array = np.array([1, 2, 3, 4])

# openpyxl - Fichiers Excel
import openpyxl
wb = openpyxl.load_workbook('data.xlsx')
```

### Web et Réseau

```python
# requests - Requêtes HTTP
import requests
response = requests.get('https://api.example.com')

# flask - Applications web
from flask import Flask
app = Flask(__name__)

# beautifulsoup4 - Scraping web
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
```

## Exercice Pratique : Mini Projet avec colorama

```python
"""
Mini Projet : Système de Notifications Colorées
Nécessite: pip install colorama
"""

from colorama import Fore, Back, Style, init
from datetime import datetime

# Initialiser
init(autoreset=True)

class NotificationSystem:
    """Système de notifications avec couleurs"""

    @staticmethod
    def timestamp():
        """Retourne l'heure actuelle formatée"""
        return datetime.now().strftime("%H:%M:%S")

    def success(self, message):
        """Notification de succès (vert)"""
        print(f"{Fore.GREEN}✅ [{self.timestamp()}] {message}")

    def error(self, message):
        """Notification d'erreur (rouge)"""
        print(f"{Fore.RED}❌ [{self.timestamp()}] {message}")

    def warning(self, message):
        """Notification d'avertissement (jaune)"""
        print(f"{Fore.YELLOW}⚠️  [{self.timestamp()}] {message}")

    def info(self, message):
        """Notification d'information (bleu)"""
        print(f"{Fore.CYAN}ℹ️  [{self.timestamp()}] {message}")

    def critical(self, message):
        """Notification critique (rouge sur blanc)"""
        print(f"{Back.RED}{Fore.WHITE}{Style.BRIGHT}🚨 [{self.timestamp()}] {message}")

# Utilisation
notif = NotificationSystem()

notif.info("Démarrage de l'application...")
notif.success("Connexion à la base de données réussie")
notif.warning("Espace disque faible (15% restant)")
notif.error("Impossible de charger le fichier config.json")
notif.critical("ERREUR CRITIQUE : Arrêt du serveur")
```

## Pièges Courants

### Erreur 1 : Permissions insuffisantes

```bash
# ❌ Erreur : Permission denied
pip install requests

# ✅ Solution : Installer pour l'utilisateur
pip install --user requests

# ✅ Ou utiliser un environnement virtuel (voir séance suivante)
```

### Erreur 2 : pip non trouvé

```bash
# ❌ Erreur : 'pip' is not recognized
pip install requests

# ✅ Solution : Utiliser python -m pip
python -m pip install requests

# Ou ajouter Python au PATH système
```

### Erreur 3 : Conflits de versions

```bash
# ❌ Package A nécessite requests==2.28.0
# ❌ Package B nécessite requests==2.31.0

# ✅ Solution : Utiliser des environnements virtuels séparés
```

### Erreur 4 : Requirements.txt incomplet

```python
# ❌ Oublier de lister une dépendance
# requirements.txt
requests==2.31.0
# Oups, le projet utilise aussi colorama !

# ✅ Toujours vérifier et tester
pip install -r requirements.txt
python main.py  # Vérifier que tout fonctionne
```

## Commandes pip Avancées

```bash
# Rechercher un package
pip search nom_package  # (Désactivé sur PyPI depuis 2021)
# À la place : https://pypi.org/

# Voir les dépendances d'un package
pip show requests

# Vérifier les packages obsolètes
pip list --outdated

# Installer depuis un dépôt Git
pip install git+https://github.com/user/repo.git

# Installer en mode éditable (développement)
pip install -e .
```

## Checklist de Maîtrise

- [ ] Je sais vérifier si pip est installé
- [ ] Je peux installer un package avec pip install
- [ ] Je sais lister les packages installés
- [ ] Je peux créer un fichier requirements.txt
- [ ] Je sais installer depuis requirements.txt
- [ ] Je comprends les versions de packages (==, >=, <)
- [ ] Je connais quelques packages populaires
- [ ] Je sais mettre à jour et désinstaller des packages

**Ne réinventez jamais la roue ! Avant de coder une fonctionnalité, cherchez si un package PyPI ne le fait pas déjà mieux que vous ne pourriez le faire.**

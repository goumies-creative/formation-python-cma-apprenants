# Séance 6 - Librairies et Modules Python

## Objectifs de la Séance

À la fin de cette séance, vous serez capable de :
- Comprendre l'écosystème des modules et librairies Python
- Importer et utiliser des modules de la bibliothèque standard
- Installer des packages externes avec pip
- Créer vos propres modules personnalisés
- Structurer un projet Python professionnel
- Gérer des environnements virtuels pour isoler vos projets

## Timing de la Séance (3 heures)

### 0h00 - 0h15 : Rappel et Objectifs
- Révision séance 5 (POO avancée, héritage)
- L'écosystème Python : pourquoi les modules ?
- Présentation des objectifs
- Questions/réponses

### 0h15 - 1h00 : Import et Bibliothèque Standard
- Comprendre l'import : from, import, as
- Modules essentiels : random, datetime, os, sys
- Exploration de la bibliothèque standard
- Exercice pratique : jeu de dés avec random

### 1h00 - 1h10 : PAUSE

### 1h10 - 1h50 : Pip et Packages Externes
- Gestionnaire de paquets pip
- Installation, mise à jour, désinstallation
- Fichier requirements.txt
- Exercice guidé : manipuler dates avec datetime

### 1h50 - 2h30 : Modules Personnalisés et Structure de Projet
- Créer ses propres modules
- Organisation d'un projet Python professionnel
- __name__ et __main__
- Exercice avancé : créer un module utils.py

### 2h30 - 3h00 : Environnements Virtuels et Bonnes Pratiques
- Pourquoi isoler ses projets ?
- Création et activation d'environnements virtuels
- Récapitulatif des acquis
- Devoirs pour la séance 7 (Projet Cryptage César)

## Concepts Clés

### Import et Modules
- **Module** : fichier Python (.py) contenant du code réutilisable
- **Package** : collection de modules organisés dans un dossier
- **import module** : importer un module complet
- **from module import fonction** : importer des éléments spécifiques
- **import module as alias** : créer un alias pour simplifier

### Bibliothèque Standard
- **random** : génération de nombres aléatoires, choix aléatoires
- **datetime** : manipulation de dates et heures
- **os** : interactions avec le système d'exploitation
- **sys** : paramètres et fonctions système
- **math** : fonctions mathématiques avancées

### Pip et Gestion de Dépendances
- **pip install** : installer un package
- **pip list** : lister les packages installés
- **pip freeze** : générer requirements.txt
- **requirements.txt** : fichier listant toutes les dépendances

### Modules Personnalisés
- **Créer un .py** : définir fonctions et classes
- **Importer** : utiliser dans d'autres fichiers
- **__name__ == "__main__"** : code exécuté uniquement si fichier lancé directement

## Exercices Pratiques

Voir le dossier [`exercices/`](exercices/) pour tous les exercices de cette séance :
- `ex01-modules-standard.py` : Exploration random et datetime
- `ex02-projet-des-statistiques.py` : Jeu de dés avec statistiques
- `ex03-module-personnalise.py` : Créer et utiliser un module utils.py

Toutes les solutions sont disponibles dans [`solutions/`](solutions/)

## Validation des Acquis

En fin de séance, vérifiez que vous savez :
- [ ] Importer un module de la bibliothèque standard
- [ ] Utiliser random pour générer nombres et choix aléatoires
- [ ] Manipuler dates et heures avec datetime
- [ ] Installer un package avec pip
- [ ] Créer un fichier requirements.txt
- [ ] Créer votre propre module personnalisé
- [ ] Structurer un projet Python avec plusieurs fichiers
- [ ] Créer et activer un environnement virtuel

## Ressources Complémentaires

- [Documentation Python - Modules](https://docs.python.org/fr/3/tutorial/modules.html)
- [PyPI - Python Package Index](https://pypi.org/)
- [Cours - Fichiers de leçon](01-import-modules.md)
- [Real Python - Python Modules](https://realpython.com/python-modules-packages/)

## Devoirs pour la Prochaine Séance

1. Compléter tous les exercices de la séance 6
2. Créer un module `calculatrice.py` avec 4 fonctions (+, -, *, /)
3. Créer un fichier `main.py` qui importe et utilise ce module
4. Installer un package de votre choix avec pip et l'explorer
5. Faire au moins 3 commits (feat: add random dice game)
6. Lire la documentation séance 7 (Projet Cryptage César)

---

**Conseil du jour :** "Ne réinventez pas la roue ! Python offre des milliers de modules. Avant de coder quelque chose, cherchez si un module ne le fait pas déjà. Votre code sera plus robuste et vous gagnerez un temps précieux !"

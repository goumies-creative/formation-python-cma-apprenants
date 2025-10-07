# Guide Complet GitHub Codespaces

## Qu'est-ce que Codespaces ?

**GitHub Codespaces** est un environnement de développement dans le cloud qui vous donne :
- Un VS Code complet dans votre navigateur
- Python, Git, et tous les outils pré-installés
- Rien à installer sur votre ordinateur
- 60 heures gratuites par mois

## Création de Compte GitHub

### Étape 1 : Inscription
1. Allez sur [github.com](https://github.com)
2. Cliquez sur "Sign up"
3. Choisissez un nom d'utilisateur
4. Utilisez votre email professionnel
5. Validez votre email

### Étape 2 : Configuration de base
1. Complétez votre profil
2. Téléchargez une photo si vous le souhaitez
3. C'est tout ! Compte prêt en 2 minutes

## Lancement de Votre Codespace

### Méthode 1 : Badge Rapide
1. Retournez sur cette page
2. Cliquez sur le badge vert "Code"
3. Sélectionnez l'onglet "Codespaces"
4. Cliquez sur "Create codespace on main"

### Méthode 2 : Lien Direct
1. Allez sur `https://github.com/codespaces`
2. Cliquez sur "New codespace"
3. Sélectionnez ce repository
4. Cliquez sur "Create codespace"

## ⏱️ Premier Lancement (2-3 minutes)

**Pendant le chargement :**
- VSCode s'installe dans le navigateur
- Python 3.11+ est configuré
- Git est initialisé
- Les extensions sont installées
- Les packages Python sont téléchargés

**Quand c'est prêt :**
- Vous voyez VS Code dans votre navigateur
- Le terminal est ouvert en bas
- L'explorateur de fichiers est à gauche

## Interface Codespaces

### Parties principales :
1. **Explorateur de fichiers** (à gauche)
   - Voir tous vos fichiers
   - Créer des dossiers
   - Ouvrir des fichiers

2. **Éditeur de code** (au centre)
   - Écrire et modifier du code
   - Coloration syntaxique
   - Auto-complétion

3. **Terminal intégré** (en bas)
   - Exécuter des commandes
   - Lancer des programmes Python
   - Utiliser Git

4. **Barre d'activité** (à gauche)
   - Explorateur de fichiers
   - Recherche
   - Gestion Git
   - Extensions

## Utilisation Quotidienne

### Ouvrir un Codespace existant :
1. Allez sur [github.com/codespaces](https://github.com/codespaces)
2. Cliquez sur votre codespace
3. Il se rouvre là où vous en étiez

### Sauvegarder votre travail :
- **Automatique** : Codespaces sauvegarde toutes les 30 secondes
- **Manuel** : Utilisez Git (appris en Séance 0)

### Arrêter proprement :
- Menu "Codespaces" en bas à gauche
- Cliquez sur "Stop Current Codespace"

## Fonctionnalités Avancées

### Ports (pour applications web) :
- Séances 14-15 : vos applications Flask s'ouvriront ici
- Accès via `https://votre-codespace-8080.preview.app.github.dev`

### Extensions pré-installées :
- Python IntelliSense
- GitLens
- French Language Pack
- Black Formatter

### Terminal personnalisable :
- Bash (Linux) par défaut
- Personnalisable dans les paramètres

## Gestion des Heures Gratuites

### Compteur d'heures :
- **120 heures gratuites** par mois pour les comptes personnels
- **Utilisation réelle** : seulement quand le codespace est actif
- **Pause automatique** après 30 minutes d'inactivité

### Économiser des heures :
- Arrêtez votre codespace après chaque session
- Utilisez "Stop" plutôt que fermer l'onglet
- Les fichiers sont sauvegardés même arrêté

## Dépannage Codespaces

### Codespace lent :
- Vérifiez votre connexion internet
- Redémarrez le codespace
- Essayez à un autre moment de la journée

### Terminal ne répond pas :
- Menu Terminal → New Terminal
- Ou redémarrez le codespace

### Problème d'extension :
- Menu Extensions (carré de 4)
- Rechargez l'extension problématique

### Perte de connexion :
- Codespaces se reconnecte automatiquement
- Votre travail est sauvegardé

## Commandes Utiles

### Vérifier l'installation :
```bash
python3 --version
git --version
code --version
```

### Lancer un script Python :
```bash
python3 mon_script.py
```

### Ouvrir un fichier avec VS Code :
```bash
code nom_du_fichier.py
```

## Félicitations !
Vous maîtrisez maintenant GitHub Codespaces. Cet environnement vous suivra pendant toute la formation.

Prochaine étape : [Séance 0 - Installfest](../MODULES-COURS/seance-00-installfest/README.md)
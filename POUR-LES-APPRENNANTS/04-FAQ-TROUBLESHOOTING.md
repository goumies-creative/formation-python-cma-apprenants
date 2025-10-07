# ❓ FAQ & Troubleshooting

## 🔧 Problèmes d'Installation

### "Python n'est pas reconnu comme commande"
**Windows :**
```powershell
# Réinstaller Python en cochant "Add Python to PATH"
# Ou ajouter manuellement au PATH :
# 1. Rechercher "Variables d'environnement"
# 2. Modifier la variable PATH
# 3. Ajouter : C:\Users\VotreNom\AppData\Local\Programs\Python\Python311\
```

**MacOS/Linux :**
```bash 
# Utiliser python3 au lieu de python
python3 --version
```

### "Permission denied" sur les scripts
**MacOS/Linux :**
```bash 
chmod +x install-macos.sh  # ou install-linux.sh
./install-macos.sh
```

**Windows :**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Le script s'arrête en cours d'installation
- Vérifiez votre connexion internet
- Relancez le script
- Si problème persiste, utilisez GitHub Codespaces

### Problèmes Python

#### "ModuleNotFoundError: No module named '...'"
```bash
# Installer le package manuellement
pip install nom_du_package

# Ou pour les packages de la formation :
pip install -r requirements.txt 
``` 

#### "SyntaxError: invalid syntax"
- Vérifiez les deux-points : après les conditions
- Vérifiez l'indentation (espaces, pas de tabs mélangés)
- Vérifiez les guillemets (utilisez toujours les mêmes)

#### Le programme ne fait rien quand je le lance
- Vérifiez que vous avez des print() pour voir le résultat
- Ajoutez input() à la fin pour garder la fenêtre ouverte (Windows)

### Problèmes Git
#### "Please tell me who you are"
```bash
git config --global user.name "Votre Prénom Nom"
git config --global user.email "votre.email@example.com"
``` 

#### "fatal: not a git repository"
```bash
# Initialiser Git dans le dossier
git init
``` 

#### J'ai fait un mauvais commit
```bash
# Annuler le dernier commit mais garder les modifications
git reset --soft HEAD~1

# Annuler complètement le dernier commit
git reset --hard HEAD~1
``` 

### Problèmes VS Code
#### Les extensions Python ne marchent pas
1. Ouvrez VS Code
2. Allez dans Extensions (Ctrl+Shift+X)
3. Recherchez "Python"
4. Installez l'extension de Microsoft
5. Redémarrez VS Code

#### Le terminal ne s'ouvre pas
- Ctrl+` (backtick) pour ouvrir/fermer le terminal
- Ou menu View → Terminal

#### IntelliSense ne fonctionne pas
- Vérifiez que l'extension Python est installée
- Redémarrez VS Code
- Vérifiez que le fichier a l'extension `.py`

### Problèmes GitHub Codespaces
#### Codespace lent
- Fermez les onglets inutiles
- Vérifiez votre connexion internet
- Redémarrez le codespace

#### "You have used ... of 120 free hours"
- Arrêtez votre codespace quand vous ne l'utilisez pas
- Menu Codespaces → Stop Current Codespace
- Les fichiers sont sauvegardés automatiquement

#### Perte de connexion
- Codespaces se reconnecte automatiquement
- Votre travail est sauvegardé en temps réel

### Problèmes Fichiers et Dossiers 
#### Je ne trouve pas mes fichiers
Terminal :
```bash
pwd                    # Voir où je suis
ls                     # Voir les fichiers ici
cd nom_du_dossier      # Aller dans un dossier
cd ..                  # Remonter d'un niveau
``` 

#### "No such file or directory"
- Vérifiez l'orthographe du nom de fichier
- Vérifiez que vous êtes dans le bon dossier
- Utilisez la complétion par tabulation

#### Permission pour créer des fichiers
```bash
# Si erreur de permission, utilisez un dossier utilisateur
cd ~/Documents
mkdir formation-python
cd formation-python
```

###  Problèmes Courants par OS
#### Windows
PowerShell bloqué :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Fenêtre qui se ferme :
```python
# Ajouter à la fin de vos scripts :
input("Appuyez sur Entrée pour quitter...")
```
#### MacOS
"xcode-select" demandé :
```bash
xcode-select --install
```

Problème Homebrew :
```bash
# Réinstaller Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Linux
Problèmes de permissions :
```bash
# Utiliser sudo si nécessaire
sudo apt update

# Ou installer dans le dossier utilisateur
pip install --user nom_du_package
```

Snap non installé (VS Code) :
```bash
# Alternative pour VS Code
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt install code
```
#### Debugging de Base
##### Mon code ne fait pas ce que je veux
1. Ajoutez des print() pour voir les valeurs des variables
2. Testez par petites parties au lieu de tout le programme
3. Lisez les messages d'erreur - ils indiquent où est le problème

##### Exemple de debugging :
```python
# Au lieu de :
resultat = calcul_complexe()

# Faites :
print("Début du calcul")
etape1 = premiere_partie()
print("Étape 1:", etape1)
etape2 = deuxieme_partie(etape1)
print("Étape 2:", etape2)
resultat = etape1 + etape2
print("Résultat final:", resultat)
```
### Quand Contacter la Formatrice
#### Contactez-moi SI :
- ❌ Le script d'installation échoue complètement
- ❌ TEST-ENVIRONNEMENT.py montre des erreurs critiques
- ❌ Vous ne pouvez pas créer de compte GitHub
- ❌ Aucune solution de cette FAQ ne fonctionne

#### Fournissez TOUJOURS :
1. Votre système d'exploitation
2. Le message d'erreur exact (copie/colle)
3. Ce que vous avez déjà essayé
4. Capture d'écran si possible

#### Ne contactez pas POUR :
- ✅ Questions sur les exercices (attendez la séance)
- ✅ Problèmes mineurs de syntaxe
- ✅ Compréhension des concepts (nous verrons en cours)

### Urgences Absolues
#### Rien ne fonctionne :
Utilisez GitHub Codespaces - c'est la solution de secours intégrée !

#### Séance qui commence dans 10 minutes :
1. Créez un compte GitHub si pas fait
2. Utilisez Codespaces pour aujourd'hui
3. Nous résoudrons les problèmes d'installation après

### Conseils de Prévention
#### Avant chaque séance :
- ✅ Lancez python3 TEST-ENVIRONNEMENT.py
- ✅ Vérifiez que tout est vert
- ✅ Sauvegardez votre travail avec Git

#### Bonnes pratiques :
- Travaillez dans le dossier formation-python-cma-apprenants
- Faites des commits réguliers
- Testez souvent votre code
- Demandez de l'aide dès que vous êtes bloqué 15 minutes

Rappel : Faire des erreurs est normal ! C'est comme cela qu'on apprend.
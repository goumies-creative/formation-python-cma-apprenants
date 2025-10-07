# 💻 Guide d'Installation Locale

## ⚠️ Avant de Commencer

### Vérifications préalables :
- **Espace disque** : 2 Go minimum
- **Connexion internet** : stable
- **Droits administrateur** : nécessaires pour l'installation
- **Temps** : 15-30 minutes selon votre connexion

### 📥 Téléchargement des Scripts

1. **Allez dans le dossier** `POUR-LA-FORMATRICE/SCRIPTS-INSTALLATION/`
2. **Téléchargez le script** pour votre système :
   - Windows : `install-windows.ps1`
   - macOS : `install-macos.sh`
   - Linux : `install-linux.sh`

## 🪟 Installation sur Windows

### Méthode Recommandée (PowerShell)

1. **Téléchargez** `install-windows.ps1`
2. **Clic droit** sur le fichier
3. **Sélectionnez** "Exécuter avec PowerShell"
4. **Autorisez** si Windows Defender demande
5. **Patientez** 10-20 minutes
6. **Redémarrez** votre ordinateur

### Si PowerShell est bloqué :

**Ouvrez PowerShell en administrateur** :
1. Menu Démarrer → Tapez "PowerShell"
2. Clic droit → "Exécuter en tant qu'administrateur"
3. Tapez cette commande :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
4.Puis exécutez le script normalement

### Installation Manuelle Windows :
1. Python : python.org/downloads

   - Cocher "Add Python to PATH"
   - Choisir "Install Now"
2. Git : git-scm.com/download/win
   - Options par défaut
   - Choisir VS Code comme éditeur
3. VS Code : code.visualstudio.com
   - Installation standard


## Installation sur macOS

### Méthode Script (Recommandée)
1. Téléchargez install-macos.sh
2. Ouvrez le Terminal (Cmd + Espace, tapez "Terminal")
3. Naviguez vers le dossier de téléchargement :

```bash
cd ~/Downloads
```
4. Rendez le script exécutable :
```bash
chmod +x install-macos.sh
```
5. Exécutez le script :
```bash
./install-macos.sh
```
6. Entrez votre mot de passe si demandé

### Installation Manuelle macOS :
1. Homebrew (gestionnaire de paquets) :
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Python :
```bash
brew install python@3.11
```
3. Git :
```bash
brew install git
```
4. VS Code :
```bash
brew install --cask visual-studio-code
```

## Installation sur Linux (Ubuntu/Debian)
### Méthode Script (Recommandée)
1. Téléchargez install-linux.sh
2. Ouvrez un terminal
3. Rendez le script exécutable :

```bash
chmod +x install-linux.sh
```

4.Exécutez avec les droits admin :
```bash
sudo ./install-linux.sh
```

5.Entrez votre mot de passe

### Installation Manuelle Linux :
1. Mettre à jour les paquets :
```bash
sudo apt update && sudo apt upgrade -y
```

2.Installer Python :
```bash
sudo apt install python3 python3-pip python3-venv -y
```

3.Installer Git :
```bash
sudo apt install git -y
```

4.Installer VS Code :
```bash
sudo snap install --classic code
```

## Vérification de l'Installation
### Test commun à tous les systèmes :
Ouvrez un terminal/console et tapez :

```bash
python3 --version
# Doit afficher : Python 3.11.x ou supérieur

git --version  
# Doit afficher : git version 2.x.x

code --version
# Doit afficher la version de VS Code
```

### Test complet avec notre script :
```bash
python3 TEST-ENVIRONNEMENT.py
```

### Résultat attendu :
```text
🎉 ENVIRONNEMENT PRÊT ! Tout est configuré pour la formation.
```

## Configuration Post-Installation
### Configuration Git (IMPORTANT) :
```bash
git config --global user.name "Votre Prénom Nom"
git config --global user.email "votre.email@example.com"
```

## Extensions VS Code recommandées :
1. Ouvrez VS Code
2. Allez dans Extensions (icône carrés)
3. Installez :
   - Python (Microsoft)
   - Pylance (Microsoft)
   - French Language Pack (Microsoft)

## Problèmes Courants et Solutions
### "Python n'est pas reconnu" (Windows)
- Réinstallez Python en cochant "Add to PATH"
- Ou redémarrez votre ordinateur

### "Permission denied" (macOS/Linux)
- Utilisez sudo devant la commande
- Vérifiez les droits du fichier

### Git ne se configure pas
- Vérifiez l'email et le nom sans fautures
- Redémarrez le terminal

### VS Code ne s'ouvre pas depuis le terminal
- Windows : Rouvrez VS Code en admin une fois
- macOS/Linux : Relancez le terminal

### 📞 Support Technique
**Si vous rencontrez des problèmes :**
1. Notez le message d'erreur exact
2. Faites une capture d'écran
3. Contactez la formatrice avec ces informations

Ne restez pas bloqué(e) ! La Séance 0 est justement prévue pour résoudre ces problèmes.

### 🎉 Félicitations !
Votre environnement local est maintenant configuré. Vous êtes prêt(e) pour la Séance 0 !

Prochaine étape : [Préparation Séance 0](./06-PREPARATION-SEANCE-0.md)
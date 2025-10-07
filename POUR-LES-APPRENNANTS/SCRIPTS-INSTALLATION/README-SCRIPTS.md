Scripts d'Installation Automatisée

## 📋 Présentation

Ces scripts automatisent l'installation complète de l'environnement de développement pour la formation Python CMA.

## 🎯 Ce qui est installé

- **Python 3.11+** avec pip
- **Git** avec configuration de base
- **Visual Studio Code** avec extensions Python
- **Packages Python** (requirements.txt)
- **Configuration** de l'environnement

## 🔒 Sécurité

### Sources officielles uniquement :
- **Windows** : winget (Microsoft officiel)
- **macOS** : Homebrew (officiel) + XCode Tools (Apple)
- **Linux** : dépôts officiels Ubuntu/Debian

### Aucun téléchargement externe :
- Tous les installateurs viennent des sites officiels
- Pas de compilation de code
- Vérifications de hash (si disponibles)

## 🚀 Utilisation

### Windows
```powershell
# Méthode 1 (Recommandée) :
# Clic droit sur install-windows.ps1 → "Exécuter avec PowerShell"

# Méthode 2 (Si bloqué) :
# Ouvrez PowerShell en admin, puis :
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Puis exécutez le script normalement
```

### macOS
```bash
# Terminal :
chmod +x install-macos.sh
./install-macos.sh
```

### Linux (Ubuntu/Debian)
```bash
# Terminal :
chmod +x install-linux.sh
sudo ./install-linux.sh
```
###  Temps d'installation
- Windows : 10-20 minutes
- MacOS : 15-25 minutes
- Linux : 10-15 minutes

### Vérification
Après installation, exécutez :
```bash
python3 ../TEST-ENVIRONNEMENT.py
```
Le script doit afficher "🎉 ENVIRONNEMENT PRÊT !" avec tous les ✅ verts.

### Dépannage
#### Problèmes courants :
Script PowerShell bloqué :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Permission denied (macOS/Linux) :
```bash
chmod +x install-*.sh
```

#### Échec connexion :
- Vérifiez votre connexion internet
- Relancez le script

**Alternative** : Utilisez GitHub Codespaces si problèmes persistants

### Support
En cas de problème :
- Notez le message d'erreur exact
- Capture d'écran de l'erreur
- Contactez la formatrice avec ces informations

Ne restez pas bloqué(e) ! La Séance 0 est prévue pour résoudre ces problèmes.
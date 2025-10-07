#!/bin/bash

# =============================================
# Script d'Installation macOS - Formation Python CMA
# CMA - École Informatique - Mairie de Paris
# Version: 1.0 - Octobre 2025
# =============================================

# Configuration
set -e  # Arrêter en cas d'erreur
LOG_FILE="installation-macos.log"

# Couleurs pour une meilleure lisibilité
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Fonction de journalisation
log() {
    local message=$1
    local type=${2:-INFO}
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$timestamp] [$type] $message" | tee -a "$LOG_FILE"
}

# Fonction d'affichage coloré
print_color() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Fonction de vérification de commande
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Fonction d'attente avec animation
wait_animation() {
    local seconds=${1:-5}
    local animation=("⣾" "⣽" "⣻" "⢿" "⡿" "⣟" "⣯" "⣷")
    for ((i=0; i<seconds; i++)); do
        for frame in "${animation[@]}"; do
            printf "\r%s Installation en cours... %d/%d secondes" "$frame" $((i+1)) "$seconds"
            sleep 0.25
        done
    done
    printf "\r\033[K"
}

# Début de l'installation
clear
print_color $CYAN "============================================="
print_color $CYAN "   INSTALLATION FORMATION PYTHON CMA"
print_color $CYAN "   CMA - École Informatique - Mairie de Paris"
print_color $CYAN "   Système: macOS"
print_color $CYAN "============================================="
log "Début de l'installation sur macOS"

# Vérification de la version macOS
log "Vérification de la version macOS..."
MACOS_VERSION=$(sw_vers -productVersion)
print_color $CYAN "��� macOS version: $MACOS_VERSION"
if [[ $(echo "$MACOS_VERSION" | cut -d. -f1) -lt 10 ]] || 
   ([[ $(echo "$MACOS_VERSION" | cut -d. -f1) -eq 10 ]] && [[ $(echo "$MACOS_VERSION" | cut -d. -f2) -lt 15 ]]); then
    print_color $RED "❌ macOS 10.15 (Catalina) ou supérieur requis"
    exit 1
fi

# Vérification des outils de développement
log "Vérification des XCode Command Line Tools..."
if ! command_exists xcode-select || ! xcode-select -p >/dev/null 2>&1; then
    print_color $YELLOW "��� Installation des XCode Command Line Tools..."
    print_color $YELLOW "Une fenêtre d'installation va s'ouvrir. Suivez les instructions."
    xcode-select --install
    
    # Attendre la fin de l'installation
    print_color $CYAN "⏳ En attente de l'installation des XCode Tools..."
    while ! xcode-select -p >/dev/null 2>&1; do
        sleep 10
    done
    print_color $GREEN "✅ XCode Command Line Tools installés"
else
    print_color $GREEN "✅ XCode Command Line Tools déjà installés"
fi

# Installation de Homebrew
log "Vérification de Homebrew..."
if ! command_exists brew; then
    print_color $CYAN "��� Installation de Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Configuration du PATH pour Homebrew
    if [[ $(uname -m) == "arm64" ]]; then
        # Apple Silicon
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
        eval "$(/opt/homebrew/bin/brew shellenv)"
    else
        # Intel
        echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
        eval "$(/usr/local/bin/brew shellenv)"
    fi
    print_color $GREEN "✅ Homebrew installé"
else
    print_color $GREEN "✅ Homebrew déjà installé"
    
    # Mise à jour de Homebrew
    print_color $CYAN "��� Mise à jour de Homebrew..."
    brew update
fi

# Installation de Python
log "Installation de Python..."
if ! command_exists python3 || ! python3 -c "import sys; assert sys.version_info >= (3, 11)" 2>/dev/null; then
    print_color $CYAN "��� Installation de Python 3.11..."
    brew install python@3.11
    
    # Lien symbolique pour python3 -> python
    if [[ $(uname -m) == "arm64" ]]; then
        # Apple Silicon
        ln -sf /opt/homebrew/bin/python3.11 /opt/homebrew/bin/python 2>/dev/null || true
    else
        # Intel
        ln -sf /usr/local/bin/python3.11 /usr/local/bin/python 2>/dev/null || true
    fi
    
    print_color $GREEN "✅ Python 3.11 installé"
else
    print_color $GREEN "✅ Python 3.11+ déjà installé"
fi

# Installation de Git
log "Installation de Git..."
if ! command_exists git; then
    print_color $CYAN "��� Installation de Git..."
    brew install git
    print_color $GREEN "✅ Git installé"
else
    print_color $GREEN "✅ Git déjà installé"
fi

# Installation de VS Code
log "Installation de Visual Studio Code..."
if ! command_exists code; then
    print_color $CYAN "��� Installation de Visual Studio Code..."
    brew install --cask visual-studio-code
    print_color $GREEN "✅ VS Code installé"
else
    print_color $GREEN "✅ VS Code déjà installé"
fi

# Configuration de Git
log "Configuration de Git..."
print_color $CYAN "⚙️ Configuration de Git..."
git config --global user.name "Apprenant CMA" || true
git config --global user.email "apprenant@cma-paris.fr" || true
git config --global init.defaultBranch main || true
git config --global core.autocrlf input || true
print_color $GREEN "✅ Git configuré"

# Installation des extensions VS Code
log "Installation des extensions VS Code..."
print_color $CYAN "��� Installation des extensions VS Code..."

# Attendre que VS Code soit disponible
wait_animation 3

# Extensions essentielles
extensions=(
    "ms-python.python"
    "ms-python.vscode-pylance"
    "ms-python.black-formatter"
    "eamodio.gitlens"
    "ms-ceintl.vscode-language-pack-fr"
)

for extension in "${extensions[@]}"; do
    print_color $CYAN "  Installation de $extension..."
    if code --install-extension "$extension" --force; then
        log "Extension $extension installée" "SUCCESS"
    else
        log "Échec installation extension $extension" "WARN"
        print_color $YELLOW "⚠️ Échec de l'installation de $extension"
    fi
done
print_color $GREEN "✅ Extensions VS Code installées"

# Installation des packages Python
log "Installation des packages Python..."
print_color $CYAN "��� Installation des packages Python..."

# Mise à jour de pip
if python3 -m pip install --upgrade pip; then
    log "pip mis à jour" "SUCCESS"
else
    log "Échec mise à jour pip" "WARN"
    print_color $YELLOW "⚠️ Échec de la mise à jour de pip"
fi

# Packages de base pour la formation
packages=(
    "pandas"
    "numpy"
    "matplotlib"
    "jupyter"
    "flask"
    "requests"
    "beautifulsoup4"
    "sqlalchemy"
    "python-dotenv"
    "black"
    "pytest"
)

for package in "${packages[@]}"; do
    print_color $CYAN "  Installation de $package..."
    if python3 -m pip install "$package"; then
        log "Package $package installé" "SUCCESS"
    else
        log "Échec installation package $package" "WARN"
        print_color $YELLOW "⚠️ Échec de l'installation de $package"
    fi
done
print_color $GREEN "✅ Packages Python installés"

# Vérification finale
log "Vérification finale de l'installation..."
print_color $CYAN "�� Vérification finale..."

checks=(
    "Python:python3 --version"
    "Git:git --version"
    "VS Code:code --version"
)

all_success=true
for check in "${checks[@]}"; do
    IFS=':' read -r name command <<< "$check"
    if output=$($command 2>/dev/null); then
        print_color $GREEN "✅ $name : $(echo "$output" | head -n1)"
    else
        print_color $RED "❌ $name : Non disponible"
        all_success=false
    fi
done

# Résumé final
echo
print_color $CYAN "============================================="
if $all_success; then
    print_color $GREEN "��� INSTALLATION RÉUSSIE !"
    print_color $GREEN "Tous les outils sont installés et configurés."
    log "Installation terminée avec succès" "SUCCESS"
else
    print_color $YELLOW "⚠️ INSTALLATION PARTIELLE"
    print_color $YELLOW "Certains composants peuvent nécessiter une attention."
    log "Installation terminée avec des avertissements" "WARN"
fi

print_color $CYAN ""
print_color $CYAN "Prochaines étapes :"
print_color $NC "1. Redémarrez votre terminal"
print_color $NC "2. Exécutez 'python3 TEST-ENVIRONNEMENT.py'"
print_color $NC "3. Vérifiez que tous les tests passent au vert"
print_color $YELLOW ""
print_color $YELLOW "En cas de problème, contactez la formatrice."
print_color $CYAN "============================================="

# Journalisation finale
log "Script d'installation terminé"
print_color $CYAN "��� Journal d'installation : $LOG_FILE"

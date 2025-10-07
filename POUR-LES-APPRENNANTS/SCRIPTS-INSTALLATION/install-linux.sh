#!/bin/bash

# =============================================
# Script d'Installation Linux - Formation Python CMA
# CMA - École Informatique - Mairie de Paris
# Version: 1.0 - Octobre 2025
# Testé sur : Ubuntu 20.04+, Debian 11+
# =============================================

# Configuration
set -e  # Arrêter en cas d'erreur
LOG_FILE="installation-linux.log"

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

# Fonction de vérification de distribution
get_linux_distro() {
    if command_exists lsb_release; then
        lsb_release -is
    elif [ -f /etc/os-release ]; then
        source /etc/os-release
        echo "$NAME"
    else
        echo "unknown"
    fi
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

# Vérification des droits sudo
check_sudo() {
    if [ "$EUID" -ne 0 ]; then
        print_color $YELLOW "🔐 Demande des droits administrateur..."
        if ! sudo -n true 2>/dev/null; then
            print_color $YELLOW "Veuillez entrer votre mot de passe sudo :"
            if ! sudo -v; then
                print_color $RED "❌ Droits administrateur requis"
                exit 1
            fi
        fi
    fi
}

# Début de l'installation
clear
print_color $CYAN "============================================="
print_color $CYAN "   INSTALLATION FORMATION PYTHON CMA"
print_color $CYAN "   CMA - École Informatique - Mairie de Paris"
print_color $CYAN "   Système: Linux"
print_color $CYAN "============================================="

# Détection de la distribution
DISTRO=$(get_linux_distro)
print_color $CYAN "📋 Distribution détectée: $DISTRO"
log "Début de l'installation sur $DISTRO"

# Vérification des droits
check_sudo

# Mise à jour des paquets
log "Mise à jour des paquets système..."
print_color $CYAN "🔄 Mise à jour des paquets système..."
sudo apt update
sudo apt upgrade -y
print_color $GREEN "✅ Système mis à jour"

# Installation des dépendances système
log "Installation des dépendances système..."
print_color $CYAN "📦 Installation des dépendances système..."
sudo apt install -y \
    curl \
    wget \
    gnupg \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    git \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential

print_color $GREEN "✅ Dépendances système installées"

# Installation de Python 3.11 si nécessaire
log "Vérification de la version Python..."
CURRENT_PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
REQUIRED_PYTHON_VERSION="3.11"

if printf '%s\n%s\n' "$REQUIRED_PYTHON_VERSION" "$CURRENT_PYTHON_VERSION" | sort -V | head -1 | grep -q "$REQUIRED_PYTHON_VERSION"; then
    print_color $GREEN "✅ Python $CURRENT_PYTHON_VERSION déjà installé"
else
    print_color $CYAN "🐍 Installation de Python 3.11..."
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt update
    sudo apt install -y python3.11 python3.11-venv python3.11-dev
    
    # Créer un lien symbolique pour python3 -> python3.11
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
    print_color $GREEN "✅ Python 3.11 installé"
fi

# Installation de Git (au cas où)
log "Vérification de Git..."
if command_exists git; then
    print_color $GREEN "✅ Git déjà installé"
else
    print_color $CYAN "📚 Installation de Git..."
    sudo apt install -y git
    print_color $GREEN "✅ Git installé"
fi

# Installation de VS Code
log "Installation de Visual Studio Code..."
if command_exists code; then
    print_color $GREEN "✅ VS Code déjà installé"
else
    print_color $CYAN "💻 Installation de Visual Studio Code..."
    
    # Méthode 1 : Snap (recommandée)
    if command_exists snap; then
        sudo snap install --classic code
    else
        # Méthode 2 : Repository officiel Microsoft
        wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
        sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
        sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
        sudo apt update
        sudo apt install -y code
        rm packages.microsoft.gpg
    fi
    print_color $GREEN "✅ VS Code installé"
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
print_color $CYAN "🔌 Installation des extensions VS Code..."

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
print_color $CYAN "📦 Installation des packages Python..."

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

# Configuration des alias (optionnel)
print_color $CYAN "⚙️ Configuration de l'environnement..."
if ! grep -q "alias python=python3" ~/.bashrc 2>/dev/null; then
    echo "alias python=python3" >> ~/.bashrc
    echo "alias pip=pip3" >> ~/.bashrc
fi

# Vérification finale
log "Vérification finale de l'installation..."
print_color $CYAN "🔍 Vérification finale..."

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

# Redémarrage recommandé des services
print_color $CYAN "🔄 Finalisation de l'installation..."
wait_animation 3

# Résumé final
echo
print_color $CYAN "============================================="
if $all_success; then
    print_color $GREEN "🎉 INSTALLATION RÉUSSIE !"
    print_color $GREEN "Tous les outils sont installés et configurés."
    log "Installation terminée avec succès" "SUCCESS"
else
    print_color $YELLOW "⚠️ INSTALLATION PARTIELLE"
    print_color $YELLOW "Certains composants peuvent nécessiter une attention."
    log "Installation terminée avec des avertissements" "WARN"
fi

print_color $CYAN ""
print_color $CYAN "Prochaines étapes :"
print_color $NC "1. Redémarrez votre terminal : 'source ~/.bashrc'"
print_color $NC "2. Exécutez 'python3 TEST-ENVIRONNEMENT.py'"
print_color $NC "3. Vérifiez que tous les tests passent au vert"
print_color $YELLOW ""
print_color $YELLOW "En cas de problème, contactez la formatrice."
print_color $CYAN "============================================="

# Journalisation finale
log "Script d'installation terminé"
print_color $CYAN "📄 Journal d'installation : $LOG_FILE"
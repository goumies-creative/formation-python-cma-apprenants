#!/bin/bash

# Script de mise à jour du cours Python CMA
# Compatible macOS et Linux

# Couleurs pour l'affichage
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "  Mise à jour du cours Python CMA"
echo "========================================"
echo ""

# Étape 1 : Sauvegarder les modifications locales
echo -e "${BLUE}[ÉTAPE 1/4]${NC} Sauvegarde de vos modifications locales..."
echo ""

# Vérifier si nous sommes dans un repo git
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}[ERREUR]${NC} Ce dossier n'est pas un dépôt Git."
    echo "Contactez votre formatrice."
    exit 1
fi

# Sauvegarder les modifications locales
git add .
if git commit -m "Sauvegarde automatique avant mise à jour - $(date '+%Y-%m-%d %H:%M:%S')"; then
    echo -e "${GREEN}[OK]${NC} Vos modifications ont été sauvegardées !"
else
    echo "Aucune modification locale à sauvegarder."
fi
echo ""

# Étape 2 : Récupérer les nouveautés
echo -e "${BLUE}[ÉTAPE 2/4]${NC} Récupération des nouveautés du cours..."
echo ""
if ! git fetch origin; then
    echo -e "${RED}[ERREUR]${NC} Impossible de contacter le serveur distant."
    echo "Vérifiez votre connexion Internet."
    exit 1
fi
echo -e "${GREEN}[OK]${NC} Nouveautés récupérées !"
echo ""

# Étape 3 : Intégrer les mises à jour
echo -e "${BLUE}[ÉTAPE 3/4]${NC} Intégration des mises à jour..."
echo ""
if ! git pull origin main --no-edit; then
    echo ""
    echo -e "${YELLOW}[ATTENTION]${NC} Il y a peut-être des conflits."
    echo "Pas de panique ! Voici quoi faire :"
    echo ""
    echo "1. Notez les fichiers en conflit affichés ci-dessus"
    echo "2. Ouvrez VS Code"
    echo "3. Les fichiers en conflit auront des marqueurs <<<<<<< HEAD"
    echo "4. Choisissez la version à garder (la vôtre ou celle du cours)"
    echo "5. Enregistrez les fichiers"
    echo "6. Dans le terminal, tapez : git add ."
    echo "7. Puis tapez : git commit -m \"Résolution des conflits\""
    echo ""
    echo "Appelez votre formatrice si besoin !"
    exit 1
fi
echo -e "${GREEN}[OK]${NC} Mises à jour intégrées !"
echo ""

# Étape 4 : Vérification finale
echo -e "${BLUE}[ÉTAPE 4/4]${NC} Vérification finale..."
echo ""
git status
echo ""

echo "========================================"
echo -e "  ${GREEN}MISE À JOUR TERMINÉE AVEC SUCCÈS !${NC}"
echo "========================================"
echo ""
echo "Vous avez maintenant accès aux nouveaux contenus."
echo "Vos exercices précédents sont sauvegardés."
echo ""
echo "Bon courage pour la suite du cours !"
echo ""

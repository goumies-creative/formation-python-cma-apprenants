@echo off
echo ========================================
echo  Mise a jour du cours Python CMA
echo ========================================
echo.

REM Couleurs et affichage sympathique
echo [ETAPE 1/4] Sauvegarde de vos modifications locales...
echo.

REM Vérifier si nous sommes dans un repo git
git status >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Ce dossier n'est pas un depot Git.
    echo Contactez votre formatrice.
    pause
    exit /b 1
)

REM Sauvegarder les modifications locales
git add .
git commit -m "Sauvegarde automatique avant mise a jour - %date% %time%"
if errorlevel 1 (
    echo Aucune modification locale a sauvegarder.
) else (
    echo [OK] Vos modifications ont ete sauvegardees !
)
echo.

echo [ETAPE 2/4] Recuperation des nouveautes du cours...
echo.
git fetch origin
if errorlevel 1 (
    echo [ERREUR] Impossible de contacter le serveur distant.
    echo Verifiez votre connexion Internet.
    pause
    exit /b 1
)
echo [OK] Nouveautes recuperees !
echo.

echo [ETAPE 3/4] Integration des mises a jour...
echo.
git pull origin main --no-edit
if errorlevel 1 (
    echo.
    echo [ATTENTION] Il y a peut-etre des conflits.
    echo Pas de panique ! Voici quoi faire :
    echo.
    echo 1. Notez les fichiers en conflit affiches ci-dessus
    echo 2. Ouvrez VS Code
    echo 3. Les fichiers en conflit auront des marqueurs ^<^<^<^<^<^<^< HEAD
    echo 4. Choisissez la version a garder (la votre ou celle du cours)
    echo 5. Enregistrez les fichiers
    echo 6. Dans le terminal, tapez : git add .
    echo 7. Puis tapez : git commit -m "Resolution des conflits"
    echo.
    echo Appelez votre formatrice si besoin !
    pause
    exit /b 1
)
echo [OK] Mises a jour integrees !
echo.

echo [ETAPE 4/4] Verification finale...
echo.
git status
echo.

echo ========================================
echo  MISE A JOUR TERMINEE AVEC SUCCES !
echo ========================================
echo.
echo Vous avez maintenant acces aux nouveaux contenus.
echo Vos exercices precedents sont sauvegardes.
echo.
echo Bon courage pour la suite du cours !
echo.
pause

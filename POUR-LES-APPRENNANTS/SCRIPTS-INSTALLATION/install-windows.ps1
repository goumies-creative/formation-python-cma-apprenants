# =============================================
# Script d'Installation Windows - Formation Python CMA
# CMA - École Informatique - Mairie de Paris
# Version: 1.0 - Octobre 2025
# =============================================

# Forcer l'encodage UTF-8 pour la console et la sortie
[Console]::InputEncoding  = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding           = [System.Text.Encoding]::UTF8
chcp 65001 | Out-Null

# Configuration
$ProgressPreference = 'SilentlyContinue'
$ErrorActionPreference = 'Continue'

# Couleurs pour une meilleure lisibilité
function Write-ColorOutput {
    param(
        [string]$Message,
        [string]$Color = "White"
    )
    Write-Host $Message -ForegroundColor $Color
}

# Fonction de journalisation
function Write-Log {
    param([string]$Message, [string]$Type = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] [$Type] $Message"
    Write-ColorOutput $logMessage
    Add-Content -Path "installation-log.txt" -Value $logMessage
}

# Fonction de test de commande
function Test-Command {
    param([string]$Command)
    try {
        Get-Command $Command -ErrorAction Stop | Out-Null
        return $true
    } catch {
        return $false
    }
}

# Fonction d'attente avec animation
function Show-WaitAnimation {
    param([int]$Seconds = 5)
    $animation = @('|', '/', '-', '\')
    for ($i = 0; $i -lt $Seconds; $i++) {
        foreach ($char in $animation) {
            Write-Host "`r$char Installation en cours... $($i+1)/$Seconds secondes" -NoNewline
            Start-Sleep -Milliseconds 250
        }
    }
    Write-Host "`r" -NoNewline
}

# Début de l'installation
Clear-Host
Write-ColorOutput "=============================================" "Cyan"
Write-ColorOutput "   INSTALLATION FORMATION PYTHON CMA" "Cyan"
Write-ColorOutput "   CMA - École Informatique - Mairie de Paris" "Cyan"
Write-ColorOutput "=============================================" "Cyan"
Write-Log "Début de l'installation"

# Vérification administrateur
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")
if (-not $isAdmin) {
    Write-Log "ATTENTION: Script exécuté sans droits administrateur" "WARN"
    Write-ColorOutput "Il est recommandé d'exécuter ce script en tant qu'administrateur." "Yellow"
    Write-ColorOutput "Certaines installations peuvent échouer." "Yellow"
    $continue = Read-Host "Continuer quand même ? (O/N)"
    if ($continue -ne 'O' -and $continue -ne 'o') {
        exit 1
    }
}

# Vérification de winget
Write-Log "Vérification de winget..."
if (-not (Test-Command "winget")) {
    Write-Log "winget non disponible" "ERROR"
    Write-ColorOutput "❌ winget n'est pas disponible sur ce système." "Red"
    Write-ColorOutput "winget est nécessaire pour l'installation automatique." "Red"
    Write-ColorOutput "Windows 10 1809+ ou Windows 11 est requis." "Red"
    Write-ColorOutput "`nSolutions alternatives :" "Yellow"
    Write-ColorOutput "1. Mettez à jour Windows" "Yellow"
    Write-ColorOutput "2. Utilisez GitHub Codespaces (recommandé)" "Yellow"
    Write-ColorOutput "3. Installation manuelle : voir la documentation" "Yellow"
    exit 1
}
Write-Log "winget disponible" "SUCCESS"

# Installation de Python
Write-Log "Installation de Python 3.11..."
try {
    Write-ColorOutput "`n��� Installation de Python 3.11..." "Cyan"
    $pythonResult = winget install --id Python.Python.3.11 --exact --accept-package-agreements --source winget --disable-interactivity
    if ($LASTEXITCODE -eq 0) {
        Write-Log "Python installé avec succès" "SUCCESS"
        Write-ColorOutput "✅ Python installé" "Green"
    } else {
        Write-Log "Échec installation Python" "ERROR"
        Write-ColorOutput "❌ Échec de l'installation de Python" "Red"
        exit 1
    }
} catch {
    Write-Log "Erreur lors de l'installation de Python: $($_.Exception.Message)" "ERROR"
    Write-ColorOutput "❌ Erreur lors de l'installation de Python" "Red"
    exit 1
}

# Installation de Git
Write-Log "Installation de Git..."
try {
    Write-ColorOutput "`n��� Installation de Git..." "Cyan"
    $gitResult = winget install --id Git.Git --exact --accept-package-agreements --source winget --disable-interactivity
    if ($LASTEXITCODE -eq 0) {
        Write-Log "Git installé avec succès" "SUCCESS"
        Write-ColorOutput "✅ Git installé" "Green"
    } else {
        Write-Log "Échec installation Git" "ERROR"
        Write-ColorOutput "❌ Échec de l'installation de Git" "Red"
        exit 1
    }
} catch {
    Write-Log "Erreur lors de l'installation de Git: $($_.Exception.Message)" "ERROR"
    Write-ColorOutput "❌ Erreur lors de l'installation de Git" "Red"
    exit 1
}

# Installation de VS Code
Write-Log "Installation de Visual Studio Code..."
try {
    Write-ColorOutput "`n��� Installation de Visual Studio Code..." "Cyan"
    $vscodeResult = winget install --id Microsoft.VisualStudioCode --exact --accept-package-agreements --source winget --disable-interactivity
    if ($LASTEXITCODE -eq 0) {
        Write-Log "VS Code installé avec succès" "SUCCESS"
        Write-ColorOutput "✅ VS Code installé" "Green"
    } else {
        Write-Log "Échec installation VS Code" "ERROR"
        Write-ColorOutput "❌ Échec de l'installation de VS Code" "Red"
        exit 1
    }
} catch {
    Write-Log "Erreur lors de l'installation de VS Code: $($_.Exception.Message)" "ERROR"
    Write-ColorOutput "❌ Erreur lors de l'installation de VS Code" "Red"
    exit 1
}

# Configuration de Git
Write-Log "Configuration de Git..."
try {
    Write-ColorOutput "`n⚙️ Configuration de Git..." "Cyan"
    
    # Attendre que Git soit disponible
    Show-WaitAnimation -Seconds 3
    
    # Configuration basique
    git config --global user.name "Apprenant CMA"
    git config --global user.email "apprenant@cma-paris.fr"
    git config --global init.defaultBranch main
    git config --global core.autocrlf true
    
    Write-Log "Git configuré avec succès" "SUCCESS"
    Write-ColorOutput "✅ Git configuré" "Green"
} catch {
    Write-Log "Erreur lors de la configuration de Git: $($_.Exception.Message)" "ERROR"
    Write-ColorOutput "⚠️ Erreur lors de la configuration de Git" "Yellow"
}

# Installation des extensions VS Code
Write-Log "Installation des extensions VS Code..."
try {
    Write-ColorOutput "`n��� Installation des extensions VS Code..." "Cyan"
    
    # Attendre que VS Code soit disponible
    Show-WaitAnimation -Seconds 5
    
    # Extensions essentielles
    $extensions = @(
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "eamodio.gitlens",
        "ms-ceintl.vscode-language-pack-fr"
    )
    
    foreach ($extension in $extensions) {
        Write-ColorOutput "  Installation de $extension..." "Gray"
        & "code" --install-extension $extension --force
        if ($LASTEXITCODE -eq 0) {
            Write-Log "Extension $extension installée" "SUCCESS"
        } else {
            Write-Log "Échec installation extension $extension" "WARN"
        }
    }
    
    Write-ColorOutput "✅ Extensions VS Code installées" "Green"
} catch {
    Write-Log "Erreur lors de l'installation des extensions: $($_.Exception.Message)" "ERROR"
    Write-ColorOutput "⚠️ Erreur lors de l'installation des extensions" "Yellow"
}

# Installation des packages Python
Write-Log "Installation des packages Python..."
try {
    Write-ColorOutput "`n��� Installation des packages Python..." "Cyan"
    
    # Vérifier que Python est dans le PATH
    $pythonPath = where.exe python 2>$null
    if (-not $pythonPath) {
        $pythonPath = where.exe python3 2>$null
    }
    
    if ($pythonPath) {
        # Mettre à jour pip
        python -m pip install --upgrade pip
        if ($LASTEXITCODE -eq 0) {
            Write-Log "pip mis à jour" "SUCCESS"
        }
        
        # Packages de base pour la formation
        $packages = @(
            "pandas",
            "numpy", 
            "matplotlib",
            "jupyter",
            "flask",
            "requests",
            "beautifulsoup4",
            "sqlalchemy",
            "python-dotenv",
            "black",
            "pytest"
        )
        
        foreach ($package in $packages) {
            Write-ColorOutput "  Installation de $package..." "Gray"
            python -m pip install $package
            if ($LASTEXITCODE -eq 0) {
                Write-Log "Package $package installé" "SUCCESS"
            } else {
                Write-Log "Échec installation package $package" "WARN"
            }
        }
        
        Write-ColorOutput "✅ Packages Python installés" "Green"
    } else {
        Write-Log "Python non trouvé dans le PATH" "ERROR"
        Write-ColorOutput "❌ Python non trouvé dans le PATH" "Red"
    }
} catch {
    Write-Log "Erreur lors de l'installation des packages: $($_.Exception.Message)" "ERROR"
    Write-ColorOutput "⚠️ Erreur lors de l'installation des packages" "Yellow"
}

# Vérification finale
Write-Log "Vérification finale de l'installation..."
Write-ColorOutput "`n��� Vérification finale..." "Cyan"

$checks = @(
    @{Name = "Python"; Command = "python --version"},
    @{Name = "Git"; Command = "git --version"},
    @{Name = "VS Code"; Command = "code --version"}
)

$allSuccess = $true
foreach ($check in $checks) {
    try {
        $output = Invoke-Expression $check.Command 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-ColorOutput "✅ $($check.Name) : $($output[0])" "Green"
        } else {
            Write-ColorOutput "❌ $($check.Name) : Non disponible" "Red"
            $allSuccess = $false
        }
    } catch {
        Write-ColorOutput "❌ $($check.Name) : Erreur de vérification" "Red"
        $allSuccess = $false
    }
}

# Résumé final
Write-ColorOutput "`n" "White"
Write-ColorOutput "=============================================" "Cyan"
if ($allSuccess) {
    Write-ColorOutput "��� INSTALLATION RÉUSSIE !" "Green"
    Write-ColorOutput "Tous les outils sont installés et configurés." "Green"
    Write-Log "Installation terminée avec succès" "SUCCESS"
} else {
    Write-ColorOutput "⚠️ INSTALLATION PARTIELLE" "Yellow"
    Write-ColorOutput "Certains composants peuvent nécessiter une attention." "Yellow"
    Write-Log "Installation terminée avec des avertissements" "WARN"
}

Write-ColorOutput "`nProchaines étapes :" "Cyan"
Write-ColorOutput "1. Redémarrez votre ordinateur" "White"
Write-ColorOutput "2. Exécutez 'python TEST-ENVIRONNEMENT.py'" "White"
Write-ColorOutput "3. Vérifiez que tous les tests passent au vert" "White"
Write-ColorOutput "`nEn cas de problème, contactez la formatrice." "Yellow"
Write-ColorOutput "=============================================" "Cyan"

# Journalisation finale
Write-Log "Script d'installation terminé"
Write-Log "Journal complet disponible dans: installation-log.txt"

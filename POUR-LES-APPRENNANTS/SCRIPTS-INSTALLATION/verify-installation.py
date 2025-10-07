#!/usr/bin/env python3
"""
Script de vérification de l'environnement - Formation Python CMA
Teste tous les outils nécessaires pour les 15 séances
"""

import sys
import subprocess
import importlib.util
import os
from pathlib import Path

class Colors:
    """Codes de couleurs pour le terminal"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_color(text, color=Colors.END):
    """Affiche du texte coloré"""
    print(f"{color}{text}{Colors.END}")

def print_header(text):
    """Affiche un en-tête"""
    print_color(f"\n{text}", Colors.CYAN + Colors.BOLD)
    print("=" * 60)

def print_success(text):
    """Affiche un succès"""
    print_color(f"✅ {text}", Colors.GREEN)

def print_warning(text):
    """Affiche un avertissement"""
    print_color(f"⚠️  {text}", Colors.YELLOW)

def print_error(text):
    """Affiche une erreur"""
    print_color(f"❌ {text}", Colors.RED)

def run_command(cmd, capture_output=True):
    """Exécute une commande et retourne le résultat"""
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        else:
            result = subprocess.run(cmd, shell=True, timeout=30)
        return result
    except subprocess.TimeoutExpired:
        return None
    except Exception as e:
        return None

def test_python():
    """Test de l'installation Python"""
    print_header("VÉRIFICATION PYTHON")
    
    # Version Python
    try:
        version = sys.version
        print_success(f"Python version: {sys.version.split()[0]}")
        
        # Vérification version minimale
        if sys.version_info >= (3, 11):
            print_success("Version Python ≥ 3.11 (OK)")
        else:
            print_warning(f"Version Python {sys.version_info.major}.{sys.version_info.minor} - 3.11+ recommandé")
        
        return True
    except Exception as e:
        print_error(f"Erreur Python: {e}")
        return False

def test_package(package_name):
    """Test l'installation d'un package"""
    try:
        spec = importlib.util.find_spec(package_name)
        if spec is not None:
            print_success(f"{package_name:20} - Installé")
            return True
        else:
            print_error(f"{package_name:20} - MANQUANT")
            return False
    except ImportError:
        print_error(f"{package_name:20} - ERREUR")
        return False

def test_git():
    """Test de l'installation Git"""
    print_header("VÉRIFICATION GIT")
    
    try:
        result = run_command("git --version")
        if result and result.returncode == 0:
            print_success(f"Git: {result.stdout.strip()}")
            
            # Test configuration basique
            result_name = run_command("git config --global user.name")
            result_email = run_command("git config --global user.email")
            
            if result_name and result_name.stdout.strip():
                print_success("Git user.name configuré")
            else:
                print_warning("Git user.name non configuré")
                
            if result_email and result_email.stdout.strip():
                print_success("Git user.email configuré")
            else:
                print_warning("Git user.email non configuré")
                
            return True
        else:
            print_error("Git non installé ou non trouvé")
            return False
    except Exception as e:
        print_error(f"Erreur Git: {e}")
        return False

def test_vscode():
    """Test de l'installation VS Code"""
    print_header("VÉRIFICATION VS CODE")
    
    try:
        # Test commande code
        result = run_command("code --version")
        if result and result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print_success(f"VS Code: {version_line}")
            
            # Test extensions (approximatif)
            extensions_result = run_command("code --list-extensions")
            if extensions_result and extensions_result.returncode == 0:
                extensions = extensions_result.stdout.split('\n')
                python_ext = any('python' in ext.lower() for ext in extensions)
                if python_ext:
                    print_success("Extension Python détectée")
                else:
                    print_warning("Extension Python non détectée")
            return True
        else:
            print_warning("VS Code non trouvé dans le PATH (peut être normal)")
            return True  # Pas critique
    except Exception as e:
        print_warning(f"VS Code: {e}")
        return True  # Pas critique

def test_environment_variables():
    """Test des variables d'environnement"""
    print_header("VARIABLES D'ENVIRONNEMENT")
    
    issues = []
    
    # Vérification PATH Python
    python_path = run_command("which python || which python3")
    if python_path and python_path.stdout.strip():
        print_success(f"Python trouvé: {python_path.stdout.strip()}")
    else:
        print_error("Python non trouvé dans le PATH")
        issues.append("Python PATH")
    
    # Vérification pip
    pip_path = run_command("which pip || which pip3")
    if pip_path and pip_path.stdout.strip():
        print_success(f"Pip trouvé: {pip_path.stdout.strip()}")
    else:
        print_error("Pip non trouvé dans le PATH")
        issues.append("Pip PATH")
    
    return len(issues) == 0

def test_file_system():
    """Test des permissions du système de fichiers"""
    print_header("SYSTÈME DE FICHIERS")
    
    try:
        # Test création fichier
        test_file = Path("test_verification.txt")
        test_file.write_text("Test de fonctionnement")
        test_file.unlink()  # Nettoyer
        
        # Test création dossier
        test_dir = Path("test_dir_verification")
        test_dir.mkdir()
        test_dir.rmdir()
        
        print_success("Permissions fichiers/dossiers OK")
        return True
    except Exception as e:
        print_error(f"Problème permissions: {e}")
        return False

def test_network():
    """Test de la connectivité réseau"""
    print_header("CONNECTIVITÉ RÉSEAU")
    
    try:
        # Test connexion basique
        import urllib.request
        urllib.request.urlopen("https://www.python.org", timeout=10)
        print_success("Connectivité internet OK")
        return True
    except Exception as e:
        print_warning(f"Problème connectivité: {e}")
        return True  # Pas critique pour l'instant

def main():
    """Fonction principale"""
    print_color("VÉRIFICATION ENVIRONNEMENT - FORMATION PYTHON CMA", Colors.CYAN + Colors.BOLD)
    print_color("CMA - École Informatique - Mairie de Paris", Colors.CYAN)
    print("=" * 60)
    
    # Résultats des tests
    results = []
    
    # Exécution des tests
    results.append(test_python())
    results.append(test_git())
    results.append(test_vscode())
    results.append(test_environment_variables())
    results.append(test_file_system())
    results.append(test_network())
    
    # Test des packages Python
    print_header("PACKAGES PYTHON")
    
    packages_obligatoires = [
        "pandas",      # Séance 9 - Données
        "flask",       # Séance 14-15 - Web
        "requests",    # Séance 11 - APIs
        "sqlalchemy",  # Séance 13 - Bases de données
    ]
    
    packages_importants = [
        "numpy",           # Calcul scientifique
        "matplotlib",      # Visualisation
        "jupyter",         # Notebooks
        "beautifulsoup4",  # Web scraping
    ]
    
    packages_optionnels = [
        "tweepy",         # Twitter API
        "python-dotenv",  # Variables environnement
        "black",          # Formatage
        "pytest",         # Tests
    ]
    
    print_color("\nPackages OBLIGATOIRES:", Colors.BOLD)
    obligatoires_ok = []
    for package in packages_obligatoires:
        if test_package(package):
            obligatoires_ok.append(package)
    
    print_color("\nPackages IMPORTANTS:", Colors.BOLD)
    for package in packages_importants:
        test_package(package)
    
    print_color("\nPackages OPTIONNELS:", Colors.BOLD)
    for package in packages_optionnels:
        test_package(package)
    
    # Résumé final
    print_header("RÉSULTATS FINAUX")
    
    total_tests = len(results)
    tests_ok = sum(results)
    packages_obligatoires_ok = len(obligatoires_ok) == len(packages_obligatoires)
    
    print(f"Tests système: {tests_ok}/{total_tests} OK")
    print(f"Packages obligatoires: {'✅ TOUS' if packages_obligatoires_ok else '❌ MANQUANTS'}")
    
    if tests_ok == total_tests and packages_obligatoires_ok:
        print_color("\nENVIRONNEMENT PRÊT !", Colors.GREEN + Colors.BOLD)
        print_color("Tout est configuré pour la formation.", Colors.GREEN)
        print_color("\nVous êtes prêt(e) pour la Séance 0 !", Colors.CYAN)
    else:
        print_color("\n❌ PROBLEMES DÉTECTÉS", Colors.RED + Colors.BOLD)
        
        if tests_ok < total_tests:
            print_color("• Problèmes avec les outils système", Colors.RED)
        
        if not packages_obligatoires_ok:
            print_color("• Packages Python manquants", Colors.RED)
        
        print_color("\nContactez la formatrice avec:", Colors.YELLOW)
        print_color("1. Ce résultat complet", Colors.YELLOW)
        print_color("2. Votre système d'exploitation", Colors.YELLOW)
        print_color("3. Les messages d'erreur spécifiques", Colors.YELLOW)
    
    # Conseils
    print_color("\nCONSEILS:", Colors.CYAN)
    print_color("• Sauvegardez ce résultat pour référence", Colors.CYAN)
    print_color("• Testez après chaque installation", Colors.CYAN)
    print_color("• Utilisez GitHub Codespaces si problèmes persistants", Colors.CYAN)
    
    return tests_ok == total_tests and packages_obligatoires_ok

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print_color("\n❌ Vérification interrompue", Colors.RED)
        sys.exit(1)
    except Exception as e:
        print_color(f"\n❌ Erreur lors de la vérification: {e}", Colors.RED)
        sys.exit(1)

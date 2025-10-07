#!/usr/bin/env python3
"""
Script de test de l'environnement pour le cours Python
Mairie de Paris - SCAP
"""

import sys
import subprocess
import importlib.util

print("🧪 Test de l'environnement de cours Python")
print("=" * 50)

# Test version Python
print(f"🐍 Python version: {sys.version}")

# Test packages essentiels
packages = [
    "pandas",
    "numpy", 
    "matplotlib",
    "flask",
    "requests",
    "bs4"
]

print("\n📦 Vérification des packages installés:")
for package in packages:
    try:
        spec = importlib.util.find_spec(package)
        if spec is not None:
            print(f"✅ {package} est installé")
        else:
            print(f"❌ {package} est manquant")
    except ImportError:
        print(f"❌ {package} est manquant")

# Test Git
try:
    git_version = subprocess.check_output(["git", "--version"], stderr=subprocess.STDOUT)
    print(f"\n📚 {git_version.decode().strip()}")
except FileNotFoundError:
    print("\n❌ Git n'est pas installé ou pas dans le PATH")

print("\n" + "=" * 50)
print("🎉 Test terminé !")
print("\nProchaines étapes:")
print("1. Tous les packages marqués ✅ doivent être installés")
print("2. En cas de ❌, contactez la formatrice")
print("3. Sauvegardez ce résultat pour référence")
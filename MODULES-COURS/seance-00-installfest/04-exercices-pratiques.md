# Exercices Pratiques - Séance 0

## Objectifs des Exercices

Pratiquer les compétences vues en séance :
- ✅ Navigation terminal
- ✅ Manipulation fichiers
- ✅ Configuration Git
- ✅ Écriture Python de base
- ✅ Workflow complet

## Exercice 1 : Maîtrise du Terminal

### Partie A - Exploration
```bash
# 1. Allez dans votre dossier personnel
cd ~

# 2. Créez un dossier "formation-python-cma"
mkdir formation-python-cma

# 3. Entrez dans ce dossier
cd formation-python-cma

# 4. Créez la structure de dossiers
mkdir seance-00 seance-01 seance-02 seance-03 projets notes

# 5. Vérifiez la création
ls -la
```

### Partie B - Manipulation
```bash
# 1. Allez dans seance-00
cd seance-00

# 2. Créez des fichiers
touch terminal-practice.py git-practice.py vscode-practice.py

# 3. Créez un fichier avec du contenu
echo "Exercices Terminal" > description.txt

# 4. Copiez ce fichier
cp description.txt backup-description.txt

# 5. Renommez le fichier copié
mv backup-description.txt sauvegarde.txt

# 6. Listez pour vérifier
ls -la

# 7. Affichez le contenu d'un fichier
cat description.txt

# 8. Créez un sous-dossier et déplacez un fichier
mkdir sous-dossier
mv sauvegarde.txt sous-dossier/

# 9. Vérifiez la structure finale
cd ..
tree  # Si disponible, sinon : ls -R
```

### Partie C - Nettoyage
```bash
# 1. Retournez dans seance-00
cd seance-00

# 2. Supprimez un fichier (prudemment)
rm terminal-practice.py

# 3. Supprimez le sous-dossier et son contenu
rm -r sous-dossier/

# 4. Vérifiez
ls -la
```

## Exercice 2 : Premier Pas avec Git
### Partie A - Configuration et Initialisation
```bash
# 1. Configurez Git (si pas déjà fait)
git config --global user.name "Votre Prénom Nom"
git config --global user.email "votre.email@example.com"

# 2. Initialisez Git dans votre projet
cd ~/formation-python-cma
git init

# 3. Vérifiez le statut
git status
```

### Partie B - Premier Commit
```bash
# 1. Créez un fichier README
echo "# Formation Python CMA" > README.md
echo "## Par Votre Prénom" >> README.md

# 2. Ajoutez le fichier
git add README.md

# 3. Vérifiez le statut
git status

# 4. Faites le premier commit
git commit -m "Initialisation projet : README ajouté"

# 5. Vérifiez l'historique
git log --oneline
```

### Partie C - Travail Quotidien
```bash
# 1. Créez un fichier Python
cd seance-00
echo 'print("Hello Git!")' > hello.py

# 2. Ajoutez et commitez
git add .
git commit -m "Ajout script hello.py"

# 3. Modifiez le fichier
echo 'print("Deuxième message")' >> hello.py

# 4. Vérifiez les modifications
git diff

# 5. Ajoutez et commitez les modifications
git add .
git commit -m "Ajout deuxième message dans hello.py"

# 6. Voir l'historique complet
git log --stat
```

##  Exercice 3 : VS Code et Python
### Partie A - Exploration VS Code
```bash
# 1. Ouvrez VS Code dans votre projet
code ~/formation-python-cma
```

#### Dans VS Code :
1. Explorez l'interface : barre d'activité, éditeur, terminal
2. Ouvrez le fichier seance-00/hello.py
3. Modifiez-le pour ajouter :

```python
print("=== Mon Premier Programme ===")
print("Bienvenue dans VS Code !")

# Variables de présentation
nom = "Votre Nom"
age = 25
ville = "Paris"

print(f"Je m'appelle {nom}")
print(f"J'ai {age} ans")
print(f"Je vis à {ville}")

# Petit calcul
annee_naissance = 2025 - age
print(f"Je suis né(e) en {annee_naissance}")
```
### Partie B - Exécution et Test
```bash
# 1. Ouvrez le terminal intégré dans VS Code (Ctrl+ù)
# 2. Exécutez votre script
python hello.py
# ou
python3 hello.py

# 3. Vous devriez voir :
# === Mon Premier Programme ===
# Bienvenue dans VS Code !
# Je m'appelle Votre Nom
# J'ai 25 ans
# Je vis à Paris
# Je suis né(e) en 2000
```

### Partie C - Fonctionnalités VS Code
1. Testez l'auto-complétion : tapez pri puis Tab
2. Testez le formatage : sauvegardez (Ctrl+S)
3. Utilisez la recherche : Ctrl+F pour trouver "print"
4. Ouvrez un nouveau terminal : Ctrl+Shift+ù

## Exercice 4 : Workflow Complet
### Scénario : Création d'un mini-projet
```bash
# 1. Créez un dossier pour l'exercice
cd ~/formation-python-cma
mkdir mon-cv-python
cd mon-cv-python

# 2. Initialisez Git
git init

# 3. Créez le fichier principal
touch cv.py
```

#### Dans VS Code, éditez `cv.py` :
```python
"""
Mon CV en Python
Formation CMA - Séance 0
"""

# Informations personnelles
nom = "Alexandre Martin"
age = 28
ville = "Paris"
email = "alexandre.martin@email.fr"

# Compétences
competences = ["Python", "Git", "VS Code", "Terminal"]

# Expérience
experiences = [
    "Formation Python CMA - 2025",
    "Autodidacte programmation - 2024",
    "Baccalauréat Scientifique - 2015"
]

# Affichage du CV
print("=" * 40)
print("            MON CURRICULUM VITAE")
print("=" * 40)

print(f"\n📋 INFORMATIONS PERSONNELLES")
print(f"Nom : {nom}")
print(f"Âge : {age} ans")
print(f"Ville : {ville}")
print(f"Email : {email}")

print(f"\n🛠️ COMPÉTENCES")
for i, competence in enumerate(competences, 1):
    print(f"{i}. {competence}")

print(f"\n📚 EXPÉRIENCE")
for i, experience in enumerate(experiences, 1):
    print(f"{i}. {experience}")

print(f"\n" + "=" * 40)
print("Fin du CV - Merci de votre lecture !")
```

#### Workflow Git :
```bash
# 1. Vérifiez le statut
git status

# 2. Ajoutez le fichier
git add cv.py

# 3. Commitez
git commit -m "Création CV interactif en Python"

# 4. Testez le programme
python cv.py

# 5. Modifiez (ajoutez dans cv.py) :
print(f"\n💡 Objectif : Devenir développeur Python professionnel")

# 6. Ajoutez et commitez la modification
git add cv.py
git commit -m "Ajout objectif professionnel"

# 7. Vérifiez l'historique
git log --oneline
```

## Exercice 5 : Défi Final
### Créez un programme de calculatrice simple :
```python
# calculatrice.py
"""
Calculatrice Simple
Formation Python CMA - Séance 0
"""

print("🧮 CALCULATRICE SIMPLE")
print("Opérations disponibles : +, -, *, /")

# Saisie utilisateur
nombre1 = float(input("Entrez le premier nombre : "))
operation = input("Entrez l'opération (+, -, *, /) : ")
nombre2 = float(input("Entrez le deuxième nombre : "))

# Calcul
if operation == "+":
    resultat = nombre1 + nombre2
    symbole = "+"
elif operation == "-":
    resultat = nombre1 - nombre2
    symbole = "-"
elif operation == "*":
    resultat = nombre1 * nombre2
    symbole = "×"
elif operation == "/":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
        symbole = "÷"
    else:
        resultat = "Erreur: division par zéro"
        symbole = "/"
else:
    resultat = "Opération non reconnue"
    symbole = operation

# Affichage du résultat
print(f"\n📊 RÉSULTAT :")
print(f"{nombre1} {symbole} {nombre2} = {resultat}")
```

### Workflow complet :
1. Créez le fichier `calculatrice.py`
2. Testez-le avec différentes opérations
3. Utilisez Git pour le versionner
4. Faites au moins 3 commits avec des messages descriptifs

## Checklist de Validation
### Terminal
- Je peux naviguer dans les dossiers
- Je sais créer/déplacer/supprimer fichiers et dossiers
- J'utilise les commandes essentielles sans hésitation

### Git
- Mon identité est configurée
- Je peux initialiser un repository
- Je maîtrise add/commit/status/log
- Mes messages de commit sont clairs

### VS Code
- Je me repère dans l'interface
- J'utilise l'auto-complétion
- Je lance mes programmes depuis VS Code
- Je bénéficie du formatage automatique

### Python
- Je crée et exécute des scripts simples
- J'utilise print() et input()
- Je travaille avec des variables
- Je comprends la syntaxe de base

### Défi Bonus (Optionnel)
Créez un programme qui :

- Demande le nom, l'âge et la ville de l'utilisateur
- Calcule l'année de naissance
- Affiche un message personnalisé
- Utilise des variables et du formatage
- Est versionné avec Git

**Exemple de sortie :**

```text
Bonjour Marie !
Tu as 30 ans et tu vis à Lyon.
Tu es donc né(e) en 1995.
Merci d'avoir utilisé mon programme !
```

### En Cas de Difficulté
- Relisez les guides précédents
- Utilisez la FAQ du repository
- Demandez de l'aide à la formatrice
- N'oubliez pas : chaque expert a commencé comme vous !

Félicitations ! Vous maîtrisez maintenant les bases de votre environnement de développement.
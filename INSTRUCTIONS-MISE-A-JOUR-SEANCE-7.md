# 📥 Instructions de Mise à Jour - Séance 7

## Pour récupérer le contenu de la séance 7

Vous avez **deux options** selon votre système :

---

## Option 1 : Script Automatique (Recommandé)

### Sur Windows (PowerShell ou Git Bash)

**Double-cliquez** sur le fichier `mise-a-jour.bat`

**OU** dans le terminal :

#### PowerShell
```powershell
.\mise-a-jour.bat
```

#### Git Bash
```bash
./mise-a-jour.sh
```

Le script va automatiquement :
- ✅ Sauvegarder vos modifications locales
- ✅ Récupérer les nouveautés (séance 7)
- ✅ Intégrer sans écraser votre travail
- ✅ Gérer les éventuels conflits

---

## Option 2 : Commandes Git Manuelles

Si vous préférez utiliser Git directement :

### PowerShell

```powershell
# 1. Sauvegarder vos modifications
git add .
git commit -m "Sauvegarde avant mise à jour séance 7"

# 2. Récupérer les nouveautés
git fetch origin

# 3. Intégrer les mises à jour
git pull origin main

# 4. Vérifier l'état
git status
```

### Git Bash

```bash
# 1. Sauvegarder vos modifications
git add .
git commit -m "Sauvegarde avant mise à jour séance 7"

# 2. Récupérer les nouveautés
git fetch origin

# 3. Intégrer les mises à jour
git pull origin main

# 4. Vérifier l'état
git status
```

---

## Que contient la séance 7 ?

Vous allez récupérer :

📁 **MODULES-COURS/seance-07-projet-cryptage-cesar/**
- `README.md` - Vue d'ensemble du projet
- `01-gestion-erreurs.md` - Cours sur try/except/finally
- `02-tests-unitaires.md` - Cours sur les tests avec assert
- `03-documentation-code.md` - Cours sur les docstrings
- **demo/** - 3 fichiers de démonstration
- **exercices/** - 3 exercices pratiques

---

## En cas de problème

### Message "Aucune modification locale à sauvegarder"
✅ **C'est normal !** Cela signifie que vous n'avez rien modifié depuis votre dernière mise à jour. Le script continue pour récupérer les nouveautés.

### Message "Il y a peut-être des conflits"
⚠️ **Pas de panique !** Suivez les instructions affichées :
1. Notez les fichiers en conflit
2. Ouvrez VS Code
3. Choisissez la version à garder (la vôtre ou celle du cours)
4. Enregistrez
5. Tapez : `git add .`
6. Puis : `git commit -m "Résolution des conflits"`

### Erreur "impossible de contacter le serveur"
🌐 Vérifiez :
- Votre connexion Internet
- Que vous êtes dans le bon dossier du cours

---

## Vérification

Après la mise à jour, vérifiez que vous avez bien le dossier :

```
MODULES-COURS/
└── seance-07-projet-cryptage-cesar/
    ├── README.md
    ├── 01-gestion-erreurs.md
    ├── 02-tests-unitaires.md
    ├── 03-documentation-code.md
    ├── demo/
    │   ├── gestion-erreur-finally.py
    │   ├── gestion-erreurs-securisee.py
    │   └── gestion-erreurs.py
    └── exercices/
        ├── ex01-gestion-erreurs.py
        ├── ex02-tests-cesar.py
        └── ex03-projet-cesar-complet.py
```

---

## Support

En cas de difficulté, contactez votre formatrice :
- **Email** : support@resources.goumies-creative.com
- **Pendant le cours** : Posez vos questions dans le chat

---

**Bon courage pour la séance 7 ! 🚀🔐**

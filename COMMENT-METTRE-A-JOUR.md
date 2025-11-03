# Comment Mettre à Jour Votre Espace de Formation

Ce guide explique comment récupérer les nouvelles séances et mises à jour du cours tout en conservant votre travail personnel.

---

## Mise à Jour Automatique (Recommandé)

Nous avons créé des scripts qui automatisent tout le processus pour vous !

### Sur Windows

1. **Double-cliquez** sur le fichier `mise-a-jour.bat`
2. Laissez le script faire son travail
3. C'est tout ! ✅

**OU** dans le terminal :
```bash
.\mise-a-jour.bat
```

### Sur macOS / Linux

Dans le terminal :
```bash
chmod +x mise-a-jour.sh  # Première fois seulement
./mise-a-jour.sh
```

---

## Que Fait le Script Automatiquement ?

Le script effectue 4 étapes pour vous :

1. **Sauvegarde vos modifications** - Tous vos exercices et notes sont mis en sécurité
2. **Récupère les nouveautés** - Télécharge les dernières séances et corrections
3. **Intègre les mises à jour** - Fusionne intelligemment votre travail avec les nouveautés
4. **Vérifie tout** - S'assure que tout s'est bien passé

**Vos fichiers ne seront JAMAIS écrasés !** Le script protège votre travail.

---

## En Cas de Conflit

Si le script vous signale un conflit (très rare), voici comment le résoudre :

### Étape 1 : Identifier les fichiers en conflit

Le script vous affichera quelque chose comme :
```
CONFLIT (contenu) : Fusion conflict dans MODULES-COURS/seance-02-conditions/exercices/ex01-if-else.py
```

### Étape 2 : Ouvrir le fichier dans VS Code

Le fichier contiendra des marqueurs spéciaux :
```python
<<<<<<< HEAD
# Votre code personnel
mon_resultat = 42
=======
# Le nouveau code du cours
mon_resultat = 0
>>>>>>> origin/main
```

### Étape 3 : Choisir la version à garder

- **Garder votre version** : Supprimez les marqueurs `<<<`, `===`, `>>>` et le code du cours
- **Garder la version du cours** : Supprimez les marqueurs et votre code
- **Garder les deux** : Combinez les deux morceaux de code

Résultat final (exemple) :
```python
# Mon code que je garde
mon_resultat = 42
```

### Étape 4 : Terminer la résolution

Dans le terminal :
```bash
git add .
git commit -m "Résolution des conflits de mise à jour"
```

**💡 Astuce** : En cas de doute, appelez votre formatrice ! Elle est là pour vous aider.

---

## Mise à Jour Manuelle (Pour les Curieux)

Si vous voulez comprendre ce que fait le script, voici les commandes manuelles :

```bash
# 1. Sauvegarder votre travail
git add .
git commit -m "Sauvegarde avant mise à jour"

# 2. Récupérer les nouveautés
git fetch origin

# 3. Intégrer les mises à jour
git pull origin main

# 4. Vérifier l'état
git status
```

---

## Questions Fréquentes

### ❓ Quand dois-je mettre à jour ?

Votre formatrice vous le dira ! En général :
- Au début de chaque nouvelle séance
- Quand de nouvelles corrections sont publiées
- Quand des corrections de bugs sont apportées

### ❓ Vais-je perdre mon travail ?

**NON !** Le script sauvegarde d'abord tous vos fichiers avant de mettre à jour. Vos exercices, notes, et modifications sont en sécurité.

### ❓ Puis-je mettre à jour même si je n'ai pas fini les exercices ?

**OUI !** Mettez à jour quand même. Vos exercices en cours seront préservés, et vous pourrez continuer à travailler dessus.

### ❓ J'ai une erreur "impossible de contacter le serveur"

Vérifiez :
- Votre connexion Internet
- Que vous êtes bien dans le bon dossier du cours
- Contactez votre formatrice si le problème persiste

### ❓ Le script dit "Aucune modification locale à sauvegarder"

C'est normal ! Cela signifie que vous n'avez rien modifié depuis votre dernière mise à jour. Le script continue quand même pour récupérer les nouveautés.

### ❓ Comment voir ce qui a été mis à jour ?

Après la mise à jour, dans le terminal :
```bash
git log --oneline -5
```
Cela affiche les 5 dernières modifications.

---

## Aide et Support

### En cas de problème

1. **Lisez les messages du script** - Ils sont conçus pour vous guider
2. **Notez le message d'erreur exact** - Prenez une capture d'écran si possible
3. **Contactez votre formatrice** - Elle vous aidera à résoudre le problème

### Contact

**Formatrice** : Romy Alula
**Email** : support@resources.goumies-creative.com

---

## Conseils de Sécurité

✅ **Faites des commits réguliers** de votre travail (même sans mise à jour)
```bash
git add .
git commit -m "Séance 3 : Exercices sur les boucles terminés"
```

✅ **Mettez à jour régulièrement** - Plus vous attendez, plus il y a de risques de conflits

✅ **Gardez une copie locale** - De temps en temps, copiez tout le dossier sur une clé USB (paranoia saine !)

---

## Pour les Développeurs en Herbe

Si vous voulez comprendre Git plus en profondeur :

- [Git - Guide Simple](https://rogerdudler.github.io/git-guide/index.fr.html)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=fr_FR) - Tutoriel interactif
- [Documentation Git Officielle](https://git-scm.com/book/fr/v2)

---

**Dernière mise à jour** : Novembre 2025
**Version du script** : 1.0

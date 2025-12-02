# Séance 7 - Projet Cryptage César

## Objectifs de la Séance

À la fin de cette séance, vous serez capable de :
- Maîtriser la gestion des erreurs avec try/except/finally
- Connaître les exceptions courantes et créer vos propres exceptions
- Écrire des tests unitaires pour valider votre code
- Comprendre l'importance de la documentation et des docstrings
- Implémenter un algorithme de cryptage/décryptage César
- Structurer un projet Python professionnel avec tests
- Valider les entrées utilisateur de manière robuste

## Timing de la Séance (3 heures)

### 0h00 - 0h15 : Rappel et Objectifs
- Révision séance 6 (modules, pip, imports)
- Présentation du projet César
- Pourquoi la gestion d'erreurs est cruciale ?
- Questions/réponses

### 0h15 - 1h00 : Gestion des Erreurs
- Les exceptions : types courants et signification
- Structure try/except/finally
- Lever ses propres exceptions avec raise
- Exercice pratique : validation d'entrées utilisateur
- Debugging avec messages d'erreurs clairs

### 1h00 - 1h10 : PAUSE

### 1h10 - 1h50 : Tests Unitaires
- Introduction aux tests : pourquoi tester ?
- Module unittest de Python
- Écrire des tests simples avec assert
- Tests pour le cryptage César
- Exercice guidé : tester une fonction de validation

### 1h50 - 2h30 : Documentation et Projet César
- Docstrings : documenter fonctions et classes
- Commentaires utiles vs commentaires inutiles
- Algorithme de César : principe et implémentation
- Exercice avancé : crypteur César avec gestion d'erreurs

### 2h30 - 3h00 : Projet Complet et Bonnes Pratiques
- Assemblage du projet César complet
- Tests unitaires pour toutes les fonctions
- Récapitulatif des acquis
- Devoirs pour la séance 8 (Tic Tac Toe)

## Concepts Clés

### Gestion des Erreurs
- **Exception** : événement qui interrompt le flux normal du programme
- **try/except** : structure pour capturer et gérer les erreurs
- **finally** : bloc exécuté quoi qu'il arrive
- **raise** : lever une exception manuellement
- **Types courants** : ValueError, TypeError, KeyError, FileNotFoundError

### Tests Unitaires
- **Test unitaire** : vérifier qu'une fonction fait ce qu'elle doit faire
- **unittest** : module intégré pour écrire des tests
- **assert** : vérifier une condition (True/False)
- **Test-Driven Development (TDD)** : écrire les tests avant le code

### Documentation
- **Docstring** : chaîne de documentation pour fonctions/classes
- **Format Google** : style de docstring clair et structuré
- **Commentaires** : expliquer le "pourquoi", pas le "quoi"

### Algorithme de César
- **Chiffrement par décalage** : remplacer chaque lettre par une autre
- **Clé de chiffrement** : nombre de positions de décalage
- **Déchiffrement** : opération inverse avec la même clé

## Exercices Pratiques

Voir le dossier [`exercices/`](exercices/) pour tous les exercices de cette séance :
- `ex01-gestion-erreurs.py` : Validation robuste d'entrées utilisateur
- `ex02-tests-cesar.py` : Tests unitaires pour fonctions de cryptage
- `ex03-projet-cesar-complet.py` : Crypteur César complet avec interface

Toutes les solutions sont disponibles dans [`solutions/`](solutions/)

## Validation des Acquis

En fin de séance, vérifiez que vous savez :
- [ ] Utiliser try/except pour gérer les erreurs
- [ ] Identifier les types d'exceptions courantes
- [ ] Lever vos propres exceptions avec raise
- [ ] Écrire des tests unitaires avec unittest
- [ ] Utiliser assert pour valider des conditions
- [ ] Rédiger des docstrings claires et complètes
- [ ] Implémenter l'algorithme de cryptage César
- [ ] Valider les entrées utilisateur de manière robuste
- [ ] Structurer un projet avec tests et documentation

## Ressources Complémentaires

- [Documentation Python - Erreurs et Exceptions](https://docs.python.org/fr/3/tutorial/errors.html)
- [Documentation Python - unittest](https://docs.python.org/fr/3/library/unittest.html)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Cours - Fichiers de leçon](01-gestion-erreurs.md)
- [Chiffrement de César - Wikipedia](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage)

## Devoirs pour la Prochaine Séance

1. Compléter tous les exercices de la séance 7
2. Ajouter au moins 5 tests unitaires à votre projet César
3. Documenter toutes vos fonctions avec des docstrings
4. Créer une fonction de cryptage par substitution (plus avancé que César)
5. Faire au moins 3 commits avec messages descriptifs
6. Lire la documentation séance 8 (Tic Tac Toe)

---

**Conseil du jour :** "Un bon développeur écrit du code qui fonctionne. Un excellent développeur écrit du code qui fonctionne, qui est testé, documenté et qui gère les erreurs avec élégance. Visez l'excellence !"

# Séance 5 - POO Avancée : Héritage et Polymorphisme

## Objectifs de la Séance

À la fin de cette séance, vous serez capable de :
- Maîtriser l'héritage et créer des hiérarchies de classes
- Comprendre et appliquer le polymorphisme
- Utiliser `super()` pour appeler les méthodes parentes
- Implémenter des properties (@property) pour getters/setters
- Utiliser les méthodes de classe (@classmethod) et statiques (@staticmethod)
- Comprendre les relations entre classes (composition vs héritage)

## Timing de la Séance (3 heures)

### 0h00 - 0h15 : Rappel et Objectifs
- Révision séance 4 (classes, objets, self)
- Partage des missions inter-séances
- Présentation des objectifs de la POO avancée

### 0h15 - 0h45 : Héritage - Concept et Syntaxe
- Métaphore de l'arbre généalogique
- Syntaxe de base de l'héritage
- Démonstrations Animal -> Chien/Chat

### 0h45 - 1h10 : Pratique Héritage
- Exercice guidé : hiérarchie Animaux
- Découverte de super()

### 1h10 - 1h20 : PAUSE

### 1h20 - 1h50 : Polymorphisme et Override
- Concept du polymorphisme
- Override de méthodes
- Exercice : Véhicules

### 1h50 - 2h30 : Properties et Décorateurs
- @property pour getters/setters
- @classmethod et @staticmethod
- Exercice : CompteBancaire avec properties

### 2h30 - 3h00 : Projet Final et Conclusion
- Mini-projet : hiérarchie complète
- Récapitulatif des acquis
- Devoirs séance 6

## Concepts Clés

### Héritage
- **Classe parente (mère, base)** : classe dont on hérite
- **Classe enfant (dérivée)** : classe qui hérite
- **super()** : appeler méthodes de la classe parente
- **Réutilisation** : éviter duplication de code

### Polymorphisme
- **Override (surcharge)** : redéfinir une méthode héritée
- **Duck typing** : "Si ça marche comme un canard..."
- **Interface commune** : même méthode, comportements différents

### Décorateurs
- **@property** : getter pythonique
- **@nom.setter** : setter avec validation
- **@classmethod** : méthode opérant sur la classe
- **@staticmethod** : fonction utilitaire sans self/cls

## Exercices Pratiques

Voir le dossier [`exercices/`](exercices/) pour tous les exercices :
- `ex01-heritage-animaux.py` : Hiérarchie Animal -> Chien/Chat
- `ex02-heritage-vehicules.py` : Système de véhicules complet
- `ex03-properties-compte.py` : CompteBancaire avec validation

Toutes les solutions sont disponibles dans [`solutions/`](solutions/)

## Validation des Acquis

En fin de séance, vérifiez que vous savez :
- [ ] Créer une classe qui hérite d'une autre
- [ ] Utiliser super() pour appeler le constructeur parent
- [ ] Redéfinir (override) une méthode héritée
- [ ] Comprendre le polymorphisme
- [ ] Implémenter des properties avec validation
- [ ] Différencier méthodes d'instance, de classe et statiques
- [ ] Choisir entre héritage et composition

## Ressources Complémentaires

- [Documentation Python - Héritage](https://docs.python.org/fr/3/tutorial/classes.html#inheritance)
- [Cours - Fichiers de leçon](01-heritage.md)
- [Python OOP Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- [Real Python - Inheritance and Composition](https://realpython.com/inheritance-composition-python/)

## Devoirs pour la Prochaine Séance

1. Créer une hiérarchie Employee hérite de Personne avec salaire, poste
2. Créer hiérarchie Forme2D -> Rectangle/Cercle avec calculer_aire()
3. Implémenter classe Temperature avec @property et validation
4. Faire au moins 3 commits sur GitHub (branche seance5-poo-avancee)
5. Lire la documentation séance 6 (modules et librairies)

---

**Conseil du jour :** "L'héritage est comme un arbre généalogique de code - chaque enfant hérite des capacités des parents, tout en développant les siennes !"

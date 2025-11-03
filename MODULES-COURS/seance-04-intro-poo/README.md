# Séance 4 - Introduction à la Programmation Orientée Objet (POO)

## Objectifs de la Séance

À la fin de cette séance, vous serez capable de :
- Comprendre les concepts fondamentaux de la POO (classe, objet, encapsulation)
- Créer vos premières classes avec attributs et méthodes
- Utiliser l'instanciation pour créer des objets
- Maîtriser le mot-clé `self` et son rôle
- Implémenter les méthodes spéciales `__init__` et `__str__`
- Créer des classes pratiques (Personne, Voiture, CompteBancaire)

## Timing de la Séance (3 heures)

### 0h00 - 0h15 : Rappel et Objectifs
- Révision séance 3 (boucles, algorithmes)
- Pourquoi la POO ? Cas d'usage concrets
- Présentation des objectifs
- Questions/réponses

### 0h15 - 1h00 : Concepts POO et Première Classe
- Paradigme orienté objet vs procédural
- Classes et objets : la métaphore du moule à gâteaux
- Création d'une première classe simple
- Attributs et méthodes
- Exercice guidé : classe Personne

### 1h00 - 1h10 : PAUSE

### 1h10 - 1h50 : Self et Méthodes Spéciales
- Comprendre `self` en profondeur
- Méthode `__init__` : le constructeur
- Méthode `__str__` : représentation lisible
- Exercice pratique : classe Voiture

### 1h50 - 2h30 : Encapsulation et Bonnes Pratiques
- Protection des attributs (convention _attribut)
- Méthodes getter et setter
- Validation des données
- Exercice avancé : classe CompteBancaire

### 2h30 - 3h00 : Projet Pratique et Conclusion
- Mini-projet : système de gestion d'étudiants
- Récapitulatif des acquis
- Devoirs pour la séance 5 (héritage)

## Concepts Clés

### POO Fondamentaux
- **Classe** : modèle/moule qui définit la structure et le comportement
- **Objet** : instance concrète créée à partir d'une classe
- **Attributs** : variables qui stockent l'état d'un objet
- **Méthodes** : fonctions qui définissent le comportement d'un objet
- **Encapsulation** : regrouper données et méthodes dans une même entité

### Self - Le Mot Magique
- **self** : référence à l'instance courante
- **self.attribut** : accéder aux attributs de l'objet
- **self dans méthodes** : toujours premier paramètre

### Méthodes Spéciales
- **__init__()** : constructeur appelé lors de la création
- **__str__()** : représentation sous forme de chaîne
- **__repr__()** : représentation technique (debugging)

## Exercices Pratiques

Voir le dossier [`exercices/`](exercices/) pour tous les exercices de cette séance :
- `ex01-classe-personne.py` : Création d'une classe Personne basique
- `ex02-classe-voiture.py` : Classe Voiture avec méthodes
- `ex03-projet-compte-bancaire.py` : Système bancaire complet

Toutes les solutions sont disponibles dans [`solutions/`](solutions/)

## Validation des Acquis

En fin de séance, vérifiez que vous savez :
- [ ] Expliquer les concepts de classe et d'objet
- [ ] Créer une classe avec attributs et méthodes
- [ ] Utiliser correctement `self` dans vos méthodes
- [ ] Implémenter `__init__` pour initialiser vos objets
- [ ] Implémenter `__str__` pour un affichage lisible
- [ ] Créer plusieurs instances d'une même classe
- [ ] Accéder et modifier les attributs d'un objet
- [ ] Appliquer l'encapsulation pour protéger vos données

## Ressources Complémentaires

- [Documentation Python - Classes](https://docs.python.org/fr/3/tutorial/classes.html)
- [Cours - Fichiers de leçon](01-concepts-poo.md)
- [Python OOP Tutorial](https://www.w3schools.com/python/python_classes.asp)
- [Real Python - OOP in Python](https://realpython.com/python3-object-oriented-programming/)

## Devoirs pour la Prochaine Séance

1. Compléter tous les exercices de la séance 4
2. Créer une classe `Livre` avec titre, auteur, année, et méthode d'affichage
3. Créer une classe `Rectangle` avec calcul d'aire et périmètre
4. Faire au moins 3 commits avec messages descriptifs (feat: add Personne class)
5. Lire la documentation séance 5 (héritage et polymorphisme)

---

**Conseil du jour :** "La POO n'est pas une complication, c'est une organisation. Vous pensez déjà en objets dans la vie réelle - maintenant vous allez coder comme vous pensez !"

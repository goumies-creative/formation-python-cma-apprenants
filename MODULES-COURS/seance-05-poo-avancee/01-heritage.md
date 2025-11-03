# L'Héritage en Python

## Objectifs

- Comprendre le concept d'héritage
- Créer des hiérarchies de classes
- Utiliser super() pour appeler les méthodes parentes
- Maîtriser l'override de méthodes

## La Métaphore de l'Arbre Généalogique

L'héritage en POO fonctionne exactement comme dans une famille :
- Un enfant **hérite** des caractéristiques de ses parents
- Il peut **ajouter** ses propres caractéristiques
- Il peut **modifier** certaines caractéristiques héritées

```
        Animal (parent)
         /    \
      Chien   Chat (enfants)
```

## Syntaxe de Base

### Créer une classe parente

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom

    def manger(self):
        print(f"{self.nom} mange")

    def dormir(self):
        print(f"{self.nom} dort")
```

### Créer une classe enfant

```python
class Chien(Animal):  # Hérite d'Animal
    def aboyer(self):
        print(f"{self.nom} fait: Ouaf!")

# Utilisation
rex = Chien("Rex")
rex.manger()  # ✅ Méthode héritée d'Animal
rex.aboyer()  # ✅ Méthode propre à Chien
```

## Utiliser super()

### Appeler le constructeur parent

```python
class Vehicule:
    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee

class Voiture(Vehicule):
    def __init__(self, marque, annee, nb_portes):
        super().__init__(marque, annee)  # Appel parent
        self.nb_portes = nb_portes

voiture = Voiture("Renault", 2020, 5)
```

## Override (Surcharge)

### Redéfinir une méthode héritée

```python
class Animal:
    def faire_son(self):
        print("Son générique")

class Chien(Animal):
    def faire_son(self):  # OVERRIDE
        print("Ouaf!")

class Chat(Animal):
    def faire_son(self):  # OVERRIDE
        print("Miaou!")
```

## Checklist de Maîtrise

- [ ] Je comprends l'héritage comme un arbre généalogique
- [ ] Je sais créer une classe qui hérite (syntaxe avec parenthèses)
- [ ] J'utilise super() pour appeler le parent
- [ ] Je peux redéfinir (override) des méthodes

**L'héritage permet de réutiliser et d'organiser votre code efficacement !**

# Le Polymorphisme en Python

## Objectifs

- Comprendre le concept de polymorphisme
- Maîtriser l'override (surcharge) de méthodes
- Utiliser le polymorphisme pour un code flexible

## Qu'est-ce que le Polymorphisme ?

**Polymorphisme** = "plusieurs formes"

Le même code peut fonctionner avec différents types d'objets, chacun répondant à sa manière.

### Métaphore : Le Chef d'Orchestre

Un chef d'orchestre donne le signal "jouer". Chaque musicien **répond différemment** :
- Le violoniste joue du violon
- Le pianiste joue du piano
- Le batteur frappe la batterie

**Même signal, comportements différents = Polymorphisme**

## Override (Surcharge de Méthodes)

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

class Vache(Animal):
    def faire_son(self):  # OVERRIDE
        print("Meuh!")
```

### Polymorphisme en action

```python
# Liste d'animaux différents
animaux = [
    Chien("Rex"),
    Chat("Felix"),
    Vache("Marguerite")
]

# Même code, comportements différents !
for animal in animaux:
    animal.faire_son()  # Chacun répond à sa façon

# Affiche :
# Ouaf!
# Miaou!
# Meuh!
```

## Exemple Pratique : Formes Géométriques

```python
class Forme:
    def calculer_aire(self):
        raise NotImplementedError("À implémenter dans la classe enfant")

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_aire(self):
        return self.longueur * self.largeur

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_aire(self):
        return 3.14159 * self.rayon ** 2

# Polymorphisme
formes = [
    Rectangle(5, 3),
    Cercle(4),
    Rectangle(10, 2)
]

for forme in formes:
    print(f"Aire : {forme.calculer_aire()}")
# Même appel, calculs différents !
```

## Duck Typing en Python

> "Si ça marche comme un canard et ça fait coin-coin comme un canard, alors c'est un canard"

En Python, on ne vérifie pas le **type**, on vérifie le **comportement**.

```python
class Canard:
    def faire_coin(self):
        print("Coin coin!")

class Robot:
    def faire_coin(self):
        print("Coin coin électronique!")

# Pas besoin d'héritage commun !
def faire_coiner(chose):
    chose.faire_coin()  # On s'en fiche du type

canard = Canard()
robot = Robot()

faire_coiner(canard)  # Coin coin!
faire_coiner(robot)   # Coin coin électronique!
```

## Override avec Extension

On peut **appeler** la méthode parente ET ajouter du comportement :

```python
class Vehicule:
    def demarrer(self):
        print("Le véhicule démarre")

class VoitureElectrique(Vehicule):
    def demarrer(self):
        print("Vérification de la batterie...")
        super().demarrer()  # Appel de la méthode parente
        print("Mode silencieux activé")

voiture = VoitureElectrique()
voiture.demarrer()
# Affiche :
# Vérification de la batterie...
# Le véhicule démarre
# Mode silencieux activé
```

## Avantages du Polymorphisme

| Avantage | Explication |
|----------|-------------|
| **Flexibilité** | Même code fonctionne avec différents types |
| **Extensibilité** | Facile d'ajouter de nouveaux types |
| **Lisibilité** | Code plus clair et organisé |
| **Maintenabilité** | Modifications localisées |

## Patterns Courants

### Pattern 1 : Traitement uniforme

```python
def traiter_tous(objets):
    for obj in objets:
        obj.traiter()  # Chacun se traite à sa façon
```

### Pattern 2 : Interface commune

```python
class Payable:
    def payer(self):
        raise NotImplementedError()

class CarteBancaire(Payable):
    def payer(self):
        print("Paiement par carte")

class PayPal(Payable):
    def payer(self):
        print("Paiement via PayPal")
```

## Pièges Courants

### Oublier super() dans override

```python
# ⚠️ Risqué : perd le comportement parent
class Enfant(Parent):
    def methode(self):
        # Nouveau code sans appeler parent
        pass

# ✅ Mieux : combine les deux
class Enfant(Parent):
    def methode(self):
        super().methode()  # Garde comportement parent
        # Ajoute nouveau comportement
```

## Checklist de Maîtrise

- [ ] Je comprends le polymorphisme (même interface, comportements différents)
- [ ] Je sais redéfinir (override) une méthode
- [ ] Je peux combiner override et super()
- [ ] Je comprends le duck typing Python

**Le polymorphisme rend votre code flexible et évolutif - c'est la magie de la POO !**

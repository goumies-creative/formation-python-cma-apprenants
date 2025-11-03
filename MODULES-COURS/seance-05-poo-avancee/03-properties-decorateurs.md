# Properties et Décorateurs en Python

## Objectifs

- Comprendre et utiliser @property pour getters/setters
- Maîtriser @classmethod pour méthodes de classe
- Utiliser @staticmethod pour fonctions utilitaires
- Créer des classes avec validation élégante

## Le Problème : Accès Direct aux Attributs

```python
class CompteBancaire:
    def __init__(self, solde):
        self.solde = solde

compte = CompteBancaire(1000)
compte.solde = -5000  # ❌ Pas de validation !
```

## La Solution : @property

### Getter avec @property

```python
class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde  # Convention : _ = protégé

    @property
    def solde(self):  # Getter
        return self._solde

compte = CompteBancaire(1000)
print(compte.solde)  # Accès comme un attribut !
# compte.solde = 500  # ❌ Erreur : pas de setter
```

### Setter avec @property

```python
class CompteBancaire:
    def __init__(self, solde):
        self._solde = solde

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, valeur):
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._solde = valeur

# Utilisation
compte = CompteBancaire(1000)
print(compte.solde)  # 1000
compte.solde = 1500  # ✅ OK
# compte.solde = -100  # ❌ ValueError
```

### Deleter (optionnel)

```python
class MaClasse:
    def __init__(self, valeur):
        self._valeur = valeur

    @property
    def valeur(self):
        return self._valeur

    @valeur.setter
    def valeur(self, val):
        self._valeur = val

    @valeur.deleter
    def valeur(self):
        print("Suppression de la valeur")
        del self._valeur

obj = MaClasse(10)
del obj.valeur  # Appelle le deleter
```

## Exemple Complet : Température

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        if valeur < -273.15:
            raise ValueError("En dessous du zéro absolu !")
        self._celsius = valeur

    @property
    def fahrenheit(self):
        """Lecture seule calculée"""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valeur):
        self.celsius = (valeur - 32) * 5/9

# Utilisation
temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.fahrenheit = 86    # Convertit automatiquement
print(temp.celsius)     # 30.0
```

## @classmethod - Méthodes de Classe

### Opérer sur la classe elle-même

```python
class Personne:
    population = 0  # Attribut de classe

    def __init__(self, nom):
        self.nom = nom
        Personne.population += 1

    @classmethod
    def obtenir_population(cls):
        return cls.population

    @classmethod
    def creer_anonyme(cls):
        """Factory method"""
        return cls("Anonyme")

# Utilisation
p1 = Personne("Alice")
p2 = Personne("Bob")
print(Personne.obtenir_population())  # 2

p3 = Personne.creer_anonyme()  # Factory
print(p3.nom)  # Anonyme
```

### Factory Methods (Pattern)

```python
class Date:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    @classmethod
    def from_string(cls, date_str):
        """Crée Date depuis string 'JJ-MM-AAAA'"""
        jour, mois, annee = map(int, date_str.split('-'))
        return cls(jour, mois, annee)

    @classmethod
    def aujourd_hui(cls):
        """Crée Date avec date actuelle"""
        from datetime import date
        today = date.today()
        return cls(today.day, today.month, today.year)

# Utilisation
d1 = Date(15, 3, 2024)
d2 = Date.from_string("15-03-2024")
d3 = Date.aujourd_hui()
```

## @staticmethod - Méthodes Statiques

### Fonctions utilitaires sans self/cls

```python
class MathUtils:
    @staticmethod
    def est_pair(nombre):
        return nombre % 2 == 0

    @staticmethod
    def est_premier(nombre):
        if nombre < 2:
            return False
        for i in range(2, int(nombre ** 0.5) + 1):
            if nombre % i == 0:
                return False
        return True

# Utilisation (pas besoin d'instance)
print(MathUtils.est_pair(4))      # True
print(MathUtils.est_premier(17))  # True
```

## Tableau Comparatif

| Type de méthode | Décorateur | 1er paramètre | Accès | Usage |
|----------------|------------|---------------|-------|-------|
| **Instance** | (aucun) | `self` | Attributs d'instance | Opérer sur l'objet |
| **Classe** | `@classmethod` | `cls` | Attributs de classe | Factory, compteurs |
| **Statique** | `@staticmethod` | (aucun) | Rien de la classe | Fonctions utilitaires |

## Exemple Complet : Gestionnaire de Produits

```python
class Produit:
    _id_counter = 0  # Compteur partagé

    def __init__(self, nom, prix):
        Produit._id_counter += 1
        self._id = Produit._id_counter
        self._nom = nom
        self._prix = prix

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not valeur:
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = valeur

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, valeur):
        if valeur < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        self._prix = valeur

    @property
    def prix_ttc(self):
        """Lecture seule calculée"""
        return self._prix * 1.20

    @classmethod
    def obtenir_nombre_produits(cls):
        return cls._id_counter

    @classmethod
    def creer_gratuit(cls, nom):
        """Factory pour produit gratuit"""
        return cls(nom, 0)

    @staticmethod
    def appliquer_remise(prix, pourcentage):
        """Utilitaire de calcul"""
        return prix * (1 - pourcentage / 100)

    def __str__(self):
        return f"Produit #{self._id}: {self._nom} - {self._prix}€ (TTC: {self.prix_ttc:.2f}€)"

# Utilisation
p1 = Produit("Clavier", 50)
p2 = Produit("Souris", 25)
p3 = Produit.creer_gratuit("Guide")

print(p1)
print(f"Prix TTC : {p1.prix_ttc}€")
print(f"Nombre de produits : {Produit.obtenir_nombre_produits()}")
print(f"Prix après remise : {Produit.appliquer_remise(50, 20)}€")
```

## Bonnes Pratiques

### Quand utiliser @property ?

✅ **OUI :**
- Validation de données
- Calculs dérivés (comme prix_ttc)
- Migration d'attributs publics vers protégés
- Compatibilité avec code existant

❌ **NON :**
- Calculs lourds (préférer méthode)
- Opérations avec effets de bord
- Simple stockage sans logique

### Conventions Python

```python
class MaClasse:
    attribut_public = "accessible partout"
    _attribut_protege = "convention : usage interne"
    __attribut_prive = "name mangling (éviter sauf besoin)"
```

## Checklist de Maîtrise

- [ ] Je comprends @property pour getters/setters
- [ ] Je sais valider avec des setters
- [ ] Je maîtrise @classmethod pour factory methods
- [ ] Je sais quand utiliser @staticmethod
- [ ] Je respecte les conventions _ et __

**Les properties et décorateurs rendent votre code pythonique et professionnel !**

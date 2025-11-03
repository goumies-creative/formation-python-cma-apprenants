# Méthodes Spéciales en Python

## Objectifs

- Maîtriser la méthode `__init__` (constructeur)
- Utiliser `__str__` pour un affichage lisible
- Découvrir `__repr__` pour le debugging
- Comprendre les autres méthodes spéciales courantes

## Qu'est-ce qu'une Méthode Spéciale ?

Les **méthodes spéciales** (ou méthodes magiques) sont des méthodes avec **double underscore** (`__nom__`) qui permettent à vos objets d'interagir avec les fonctionnalités intégrées de Python.

```python
class Personne:
    def __init__(self, nom):      # Méthode spéciale
        self.nom = nom

    def __str__(self):            # Méthode spéciale
        return f"Personne: {self.nom}"

    def dire_bonjour(self):       # Méthode normale
        print(f"Bonjour, je suis {self.nom}")
```

## La Méthode __init__

### Le Constructeur

`__init__` est appelé **automatiquement** lors de la création d'un objet.

```python
class Voiture:
    def __init__(self, marque, modele):
        print("🚗 Construction d'une voiture...")
        self.marque = marque
        self.modele = modele
        self.km = 0

# Lors de la création, __init__ est appelé automatiquement
ma_voiture = Voiture("Renault", "Clio")
# Affiche: 🚗 Construction d'une voiture...
```

### Paramètres Optionnels

```python
class Produit:
    def __init__(self, nom, prix, stock=0, categorie="Général"):
        """
        Constructeur avec paramètres par défaut

        Args:
            nom: Nom du produit (obligatoire)
            prix: Prix en euros (obligatoire)
            stock: Quantité en stock (optionnel, défaut=0)
            categorie: Catégorie du produit (optionnel, défaut="Général")
        """
        self.nom = nom
        self.prix = prix
        self.stock = stock
        self.categorie = categorie

# Différentes façons d'instancier
p1 = Produit("Ordinateur", 1200)                        # Stock=0, Catégorie="Général"
p2 = Produit("Ordinateur", 1200, 5)                     # Stock=5, Catégorie="Général"
p3 = Produit("Ordinateur", 1200, 5, "Informatique")     # Tout spécifié
p4 = Produit("Ordinateur", 1200, categorie="High-tech") # Paramètre nommé
```

### Validation dans __init__

```python
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        # Validation du titulaire
        if not isinstance(titulaire, str) or len(titulaire) == 0:
            raise ValueError("Le titulaire doit être une chaîne non vide")

        # Validation du solde
        if not isinstance(solde_initial, (int, float)):
            raise TypeError("Le solde doit être un nombre")
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif")

        self.titulaire = titulaire
        self.solde = solde_initial
        print(f"✅ Compte créé pour {titulaire} avec {solde_initial}€")

# Utilisation
try:
    compte1 = CompteBancaire("Alice", 1000)     # ✅ OK
    compte2 = CompteBancaire("", 500)           # ❌ Erreur
except ValueError as e:
    print(f"Erreur: {e}")
```

## La Méthode __str__

### Affichage Lisible

`__str__` est appelé par `print()` et `str()` pour obtenir une représentation **lisible pour l'utilisateur**.

```python
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

    def __str__(self):
        """Représentation lisible pour l'utilisateur"""
        return f"📖 '{self.titre}' de {self.auteur} ({self.annee})"

# Utilisation
livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
print(livre)  # 📖 'Le Petit Prince' de Antoine de Saint-Exupéry (1943)

# Sans __str__, on obtient :
# <__main__.Livre object at 0x7f8b3c4a5d90>
```

### Exemples Avancés

```python
class Etudiant:
    def __init__(self, nom, prenom, notes=None):
        self.nom = nom
        self.prenom = prenom
        self.notes = notes if notes else []

    def __str__(self):
        """Affichage détaillé avec moyenne"""
        if self.notes:
            moyenne = sum(self.notes) / len(self.notes)
            return f"{self.prenom} {self.nom} - Moyenne: {moyenne:.2f}/20"
        else:
            return f"{self.prenom} {self.nom} - Aucune note"

etudiant1 = Etudiant("Dupont", "Alice", [15, 18, 16])
etudiant2 = Etudiant("Martin", "Bob")

print(etudiant1)  # Alice Dupont - Moyenne: 16.33/20
print(etudiant2)  # Bob Martin - Aucune note
```

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        """Affichage avec calculs"""
        aire = self.longueur * self.largeur
        perimetre = 2 * (self.longueur + self.largeur)
        return f"Rectangle {self.longueur}x{self.largeur} (Aire: {aire}, Périmètre: {perimetre})"

rect = Rectangle(5, 3)
print(rect)  # Rectangle 5x3 (Aire: 15, Périmètre: 16)
```

## La Méthode __repr__

### Représentation Technique

`__repr__` est appelé par `repr()` et dans l'interpréteur interactif. Elle doit retourner une représentation **non ambiguë** de l'objet.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Pour l'utilisateur"""
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        """Pour le développeur"""
        return f"Point(x={self.x}, y={self.y})"

# Utilisation
point = Point(3, 5)
print(str(point))   # Point(3, 5)
print(repr(point))  # Point(x=3, y=5)

# Dans l'interpréteur
# >>> point
# Point(x=3, y=5)  # Utilise __repr__
```

### Best Practice : __repr__ Reproductible

```python
class Produit:
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def __repr__(self):
        """Représentation qui peut recréer l'objet"""
        return f"Produit(nom='{self.nom}', prix={self.prix}, stock={self.stock})"

    def __str__(self):
        """Représentation lisible"""
        return f"{self.nom} - {self.prix}€ (Stock: {self.stock})"

# Utilisation
produit = Produit("Clavier", 49.99, 12)
print(produit)        # Clavier - 49.99€ (Stock: 12)
print(repr(produit))  # Produit(nom='Clavier', prix=49.99, stock=12)

# On peut copier-coller la sortie de repr() pour recréer l'objet
nouveau_produit = Produit(nom='Clavier', prix=49.99, stock=12)
```

## Autres Méthodes Spéciales Courantes

### __len__ : Longueur d'un Objet

```python
class Playlist:
    def __init__(self, nom):
        self.nom = nom
        self.chansons = []

    def ajouter(self, chanson):
        self.chansons.append(chanson)

    def __len__(self):
        """Permet d'utiliser len() sur l'objet"""
        return len(self.chansons)

    def __str__(self):
        return f"Playlist '{self.nom}' ({len(self)} chansons)"

# Utilisation
playlist = Playlist("Mes favoris")
playlist.ajouter("Bohemian Rhapsody")
playlist.ajouter("Imagine")
playlist.ajouter("Hotel California")

print(len(playlist))  # 3 (grâce à __len__)
print(playlist)       # Playlist 'Mes favoris' (3 chansons)
```

### __eq__ : Comparaison d'Égalité

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Permet d'utiliser == sur nos objets"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"({self.x}, {self.y})"

# Utilisation
p1 = Point(3, 5)
p2 = Point(3, 5)
p3 = Point(1, 2)

print(p1 == p2)  # True (grâce à __eq__)
print(p1 == p3)  # False
```

### __add__ : Opérateur +

```python
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Permet d'utiliser + sur nos objets"""
        if isinstance(other, Vecteur):
            return Vecteur(self.x + other.x, self.y + other.y)
        raise TypeError("L'opération + nécessite un Vecteur")

    def __str__(self):
        return f"Vecteur({self.x}, {self.y})"

# Utilisation
v1 = Vecteur(3, 5)
v2 = Vecteur(1, 2)
v3 = v1 + v2  # Utilise __add__

print(v3)  # Vecteur(4, 7)
```

## Exercice Pratique Complet

### Classe Article de Blog

```python
from datetime import datetime

class Article:
    def __init__(self, titre, auteur, contenu):
        self.titre = titre
        self.auteur = auteur
        self.contenu = contenu
        self.date_creation = datetime.now()
        self.nb_vues = 0

    def __str__(self):
        """Affichage utilisateur"""
        date_formatee = self.date_creation.strftime("%d/%m/%Y %H:%M")
        apercu = self.contenu[:50] + "..." if len(self.contenu) > 50 else self.contenu
        return f"""
📝 {self.titre}
   Par {self.auteur} le {date_formatee}
   {apercu}
   👁️  {self.nb_vues} vues
        """.strip()

    def __repr__(self):
        """Représentation technique"""
        return f"Article(titre='{self.titre}', auteur='{self.auteur}', contenu='...')"

    def __len__(self):
        """Longueur du contenu"""
        return len(self.contenu)

    def lire(self):
        """Simule la lecture de l'article"""
        self.nb_vues += 1
        print(f"\n{'='*60}")
        print(f"{self.titre}".center(60))
        print(f"Par {self.auteur}".center(60))
        print('='*60)
        print(self.contenu)
        print('='*60)

# Test
article = Article(
    "Introduction à la POO",
    "Alice Dupont",
    "La programmation orientée objet est un paradigme de programmation qui organise le code autour d'objets."
)

print(article)
print(f"\nLongueur: {len(article)} caractères")
article.lire()
article.lire()
print(f"\nNombre de vues: {article.nb_vues}")
```

## Résumé des Méthodes Spéciales

| Méthode | Utilisation | Appelée par |
|---------|-------------|-------------|
| `__init__` | Constructeur | `obj = Classe()` |
| `__str__` | Représentation lisible | `print(obj)`, `str(obj)` |
| `__repr__` | Représentation technique | `repr(obj)`, console |
| `__len__` | Longueur | `len(obj)` |
| `__eq__` | Égalité | `obj1 == obj2` |
| `__lt__` | Inférieur à | `obj1 < obj2` |
| `__add__` | Addition | `obj1 + obj2` |
| `__getitem__` | Accès par index | `obj[index]` |
| `__contains__` | Test d'appartenance | `x in obj` |

## Pièges Courants

### __str__ qui ne retourne pas une chaîne
```python
# ❌ Erreur
class MaClasse:
    def __str__(self):
        return 123  # Doit retourner str !

# ✅ Correct
class MaClasse:
    def __str__(self):
        return "123"
```

### Oublier de retourner quelque chose
```python
# ❌ Erreur
class Point:
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        # Oubli du return !

# ✅ Correct
class Point:
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

## Checklist de Maîtrise

- [ ] Je comprends le rôle de `__init__`
- [ ] Je valide les données dans le constructeur
- [ ] Je sais utiliser `__str__` pour un affichage lisible
- [ ] Je comprends la différence entre `__str__` et `__repr__`
- [ ] Je connais les méthodes spéciales courantes (`__len__`, `__eq__`, etc.)
- [ ] Je sais quand implémenter chaque méthode spéciale

**Les méthodes spéciales rendent vos objets aussi intuitifs que les types intégrés de Python !**

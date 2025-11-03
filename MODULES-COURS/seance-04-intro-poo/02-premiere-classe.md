# Créer Votre Première Classe

## Objectifs

- Créer une classe avec attributs et méthodes
- Comprendre et utiliser `self`
- Instancier des objets
- Accéder aux attributs et appeler des méthodes

## Syntaxe de Base

### Structure Minimale

```python
class Personne:
    """Documentation de la classe"""
    pass  # Classe vide pour l'instant

# Création d'une instance
personne1 = Personne()
```

### Ajouter des Attributs

```python
class Personne:
    def __init__(self, nom, age):
        """Constructeur : initialise les attributs"""
        self.nom = nom
        self.age = age

# Création avec attributs
alice = Personne("Alice", 25)
bob = Personne("Bob", 30)

print(alice.nom)  # Alice
print(bob.age)    # 30
```

## Le Mot-Clé self

### Qu'est-ce que self ?

**self** représente **l'instance courante** de la classe. C'est la référence à l'objet lui-même.

```python
class Chien:
    def __init__(self, nom):
        self.nom = nom  # self.nom = attribut de CET objet

    def aboyer(self):
        print(f"{self.nom} fait: Ouaf!")  # self.nom accède au nom de CET objet

# Deux chiens différents
rex = Chien("Rex")
max = Chien("Max")

rex.aboyer()  # Rex fait: Ouaf!
max.aboyer()  # Max fait: Ouaf!
```

### Analogie : Le Badge d'Identité

Imaginez que `self` est comme un badge qui dit **"C'est MOI"**.

```python
class Etudiant:
    def __init__(self, nom, note):
        self.nom = nom      # MON nom
        self.note = note    # MA note

    def afficher_resultat(self):
        # Quand j'affiche, j'utilise MON nom et MA note
        print(f"{self.nom} a obtenu {self.note}/20")

student1 = Etudiant("Alice", 18)
student2 = Etudiant("Bob", 15)

student1.afficher_resultat()  # Alice utilise SON badge
student2.afficher_resultat()  # Bob utilise SON badge
```

## Ajouter des Méthodes

### Méthodes d'Action

```python
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        """Ajoute de l'argent au compte"""
        self.solde += montant
        print(f"Dépôt de {montant}€")

    def retirer(self, montant):
        """Retire de l'argent du compte"""
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant}€")
        else:
            print("❌ Solde insuffisant")

    def afficher_solde(self):
        """Affiche le solde actuel"""
        print(f"💰 Solde de {self.titulaire}: {self.solde}€")

# Utilisation
compte = CompteBancaire("Alice", 1000)
compte.afficher_solde()  # 💰 Solde de Alice: 1000€
compte.deposer(500)      # Dépôt de 500€
compte.afficher_solde()  # 💰 Solde de Alice: 1500€
compte.retirer(200)      # Retrait de 200€
compte.afficher_solde()  # 💰 Solde de Alice: 1300€
```

### Méthodes avec Retour de Valeur

```python
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_aire(self):
        """Retourne l'aire du rectangle"""
        return self.longueur * self.largeur

    def calculer_perimetre(self):
        """Retourne le périmètre du rectangle"""
        return 2 * (self.longueur + self.largeur)

    def est_carre(self):
        """Vérifie si le rectangle est un carré"""
        return self.longueur == self.largeur

# Utilisation
rect = Rectangle(5, 3)
print(f"Aire: {rect.calculer_aire()} m²")           # Aire: 15 m²
print(f"Périmètre: {rect.calculer_perimetre()} m")  # Périmètre: 16 m
print(f"Est un carré: {rect.est_carre()}")          # Est un carré: False

carre = Rectangle(4, 4)
print(f"Est un carré: {carre.est_carre()}")         # Est un carré: True
```

## Attributs par Défaut

```python
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = 0              # Valeur par défaut
        self.reservoir = 50      # Valeur par défaut
        self.en_marche = False   # Valeur par défaut

    def demarrer(self):
        if not self.en_marche:
            self.en_marche = True
            print(f"🚗 {self.marque} {self.modele} démarrée")
        else:
            print("La voiture est déjà démarrée")

    def rouler(self, distance):
        if self.en_marche:
            self.km += distance
            consommation = distance * 0.05
            self.reservoir -= consommation
            print(f"Vous avez parcouru {distance} km")
        else:
            print("❌ Démarrez d'abord la voiture")

# Utilisation
ma_voiture = Voiture("Renault", "Clio", 2020)
print(f"Kilométrage initial: {ma_voiture.km} km")  # 0 km
ma_voiture.demarrer()
ma_voiture.rouler(100)
print(f"Kilométrage actuel: {ma_voiture.km} km")   # 100 km
```

## Exercice Pratique Guidé

### Exercice 1 : Classe Étudiant

```python
class Etudiant:
    def __init__(self, nom, prenom, classe):
        self.nom = nom
        self.prenom = prenom
        self.classe = classe
        self.notes = []  # Liste vide au départ

    def ajouter_note(self, matiere, note):
        """Ajoute une note"""
        if 0 <= note <= 20:
            self.notes.append({"matiere": matiere, "note": note})
            print(f"✅ Note ajoutée: {matiere} = {note}/20")
        else:
            print("❌ La note doit être entre 0 et 20")

    def calculer_moyenne(self):
        """Calcule la moyenne générale"""
        if len(self.notes) == 0:
            return 0
        total = sum(note["note"] for note in self.notes)
        return round(total / len(self.notes), 2)

    def afficher_bulletin(self):
        """Affiche le bulletin complet"""
        print(f"\n📋 BULLETIN DE {self.prenom} {self.nom} - Classe {self.classe}")
        print("=" * 50)
        for item in self.notes:
            print(f"{item['matiere']:.<30} {item['note']}/20")
        print("=" * 50)
        print(f"Moyenne générale: {self.calculer_moyenne()}/20")

# Test complet
etudiant = Etudiant("Dupont", "Alice", "Terminale S")
etudiant.ajouter_note("Mathématiques", 18)
etudiant.ajouter_note("Physique", 15)
etudiant.ajouter_note("Français", 16)
etudiant.afficher_bulletin()
```

### Exercice 2 : Classe Chronomètre

```python
import time

class Chronometre:
    def __init__(self):
        self.temps_depart = 0
        self.temps_arret = 0
        self.en_cours = False

    def demarrer(self):
        """Démarre le chronomètre"""
        if not self.en_cours:
            self.temps_depart = time.time()
            self.en_cours = True
            print("⏱️  Chronomètre démarré")
        else:
            print("Le chronomètre est déjà en cours")

    def arreter(self):
        """Arrête le chronomètre"""
        if self.en_cours:
            self.temps_arret = time.time()
            self.en_cours = False
            print("⏹️  Chronomètre arrêté")
        else:
            print("Le chronomètre n'est pas démarré")

    def obtenir_temps(self):
        """Retourne le temps écoulé"""
        if self.en_cours:
            temps_ecoule = time.time() - self.temps_depart
        else:
            temps_ecoule = self.temps_arret - self.temps_depart
        return round(temps_ecoule, 2)

    def afficher_temps(self):
        """Affiche le temps écoulé"""
        temps = self.obtenir_temps()
        print(f"⏱️  Temps écoulé: {temps} secondes")

# Test
chrono = Chronometre()
chrono.demarrer()
time.sleep(2)  # Attend 2 secondes
chrono.afficher_temps()
chrono.arreter()
```

## Bonnes Pratiques

### 1. Noms de Classes en PascalCase
```python
# ✅ Correct
class CompteBancaire:
    pass

class GestionnaireUtilisateurs:
    pass

# ❌ Incorrect
class compte_bancaire:  # snake_case (pour fonctions)
    pass

class gestionnaireUtilisateurs:  # camelCase (JavaScript)
    pass
```

### 2. Docstrings pour Documentation
```python
class Produit:
    """
    Représente un produit dans un inventaire.

    Attributes:
        nom (str): Nom du produit
        prix (float): Prix en euros
        stock (int): Quantité en stock
    """
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def vendre(self, quantite):
        """
        Vend une quantité du produit.

        Args:
            quantite (int): Nombre d'unités à vendre

        Returns:
            bool: True si vente réussie, False sinon
        """
        if quantite <= self.stock:
            self.stock -= quantite
            return True
        return False
```

### 3. Validation des Données
```python
class Personne:
    def __init__(self, nom, age):
        # Validation dans le constructeur
        if not isinstance(nom, str) or len(nom) == 0:
            raise ValueError("Le nom doit être une chaîne non vide")
        if not isinstance(age, int) or age < 0:
            raise ValueError("L'âge doit être un entier positif")

        self.nom = nom
        self.age = age

# Utilisation
try:
    p1 = Personne("Alice", 25)     # ✅ OK
    p2 = Personne("", 30)          # ❌ Erreur
except ValueError as e:
    print(f"Erreur: {e}")
```

## Pièges Courants

### Oublier self dans les méthodes
```python
# ❌ Erreur
class MaClasse:
    def __init__(self, valeur):
        valeur = valeur  # Manque self !

    def afficher(self):
        print(valeur)  # Manque self ! (NameError)

# ✅ Correct
class MaClasse:
    def __init__(self, valeur):
        self.valeur = valeur

    def afficher(self):
        print(self.valeur)
```

### Modifier les paramètres du constructeur
```python
# ❌ Confusion
class Personne:
    def __init__(self, nom, age):
        nom = nom.upper()  # Modifie le paramètre, pas l'attribut !
        age = age

# ✅ Correct
class Personne:
    def __init__(self, nom, age):
        self.nom = nom.upper()  # Modifie l'attribut
        self.age = age
```

### Appel de méthode sans self
```python
class Calculatrice:
    def __init__(self):
        self.resultat = 0

    def additionner(self, a, b):
        return a + b

    def calculer_double(self, nombre):
        # ❌ Erreur
        resultat = additionner(nombre, nombre)  # NameError

        # ✅ Correct
        resultat = self.additionner(nombre, nombre)
        return resultat
```

## Checklist de Maîtrise

- [ ] Je sais créer une classe avec `class NomClasse:`
- [ ] Je comprends le rôle de `__init__`
- [ ] J'utilise toujours `self` pour les attributs et méthodes
- [ ] Je peux créer plusieurs instances indépendantes
- [ ] Je sais ajouter des méthodes d'action
- [ ] Je sais créer des méthodes avec retour de valeur
- [ ] Je valide les données dans le constructeur
- [ ] J'utilise PascalCase pour nommer mes classes

**Chaque classe que vous créez est un nouveau "type" que vous inventez - c'est le pouvoir de la POO !**

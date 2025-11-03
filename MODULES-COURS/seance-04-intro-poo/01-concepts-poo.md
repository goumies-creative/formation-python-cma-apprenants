# Concepts de la Programmation Orientée Objet

## Objectifs

- Comprendre le paradigme orienté objet
- Différencier programmation procédurale et orientée objet
- Maîtriser les concepts de classe et d'objet
- Appréhender l'encapsulation

## Pourquoi la POO ?

### Le Problème avec la Programmation Procédurale

```python
# Code procédural : données et fonctions séparées
voiture1_marque = "Renault"
voiture1_modele = "Clio"
voiture1_annee = 2020
voiture1_km = 45000

voiture2_marque = "Peugeot"
voiture2_modele = "208"
voiture2_annee = 2021
voiture2_km = 12000

def afficher_voiture(marque, modele, annee, km):
    print(f"{marque} {modele} ({annee}) - {km} km")

def rouler(distance):
    # Quelle voiture ? Comment gérer ça ?
    pass

afficher_voiture(voiture1_marque, voiture1_modele, voiture1_annee, voiture1_km)
```

**Problèmes :**
- Trop de variables séparées
- Difficile à maintenir
- Pas de lien clair entre données et comportements
- Complexité croît rapidement

### La Solution POO

```python
# Code orienté objet : données et comportements liés
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = 0

    def afficher(self):
        print(f"{self.marque} {self.modele} ({self.annee}) - {self.km} km")

    def rouler(self, distance):
        self.km += distance
        print(f"Vous avez parcouru {distance} km")

# Utilisation simple et claire
voiture1 = Voiture("Renault", "Clio", 2020)
voiture2 = Voiture("Peugeot", "208", 2021)

voiture1.afficher()  # Renault Clio (2020) - 0 km
voiture1.rouler(150)  # Vous avez parcouru 150 km
voiture1.afficher()  # Renault Clio (2020) - 150 km
```

**Avantages :**
- Code organisé et structuré
- Données et comportements regroupés
- Facile à maintenir et étendre
- Réutilisable

## Métaphore : Le Moule à Gâteaux

### La Classe = Le Moule
Imaginez un moule à gâteaux. Le moule lui-même n'est pas un gâteau, c'est **le modèle** qui définit la forme.

```python
class Gateau:
    """Le moule (la classe) définit la structure"""
    def __init__(self, parfum, poids):
        self.parfum = parfum
        self.poids = poids

    def cuire(self, minutes):
        print(f"Cuisson du gâteau {self.parfum} pendant {minutes} min")
```

### L'Objet = Le Gâteau Concret
Chaque fois que vous utilisez le moule, vous créez un gâteau différent (un **objet**).

```python
# Utilisation du moule pour créer des gâteaux
gateau_chocolat = Gateau("chocolat", 500)
gateau_vanille = Gateau("vanille", 450)
gateau_fraise = Gateau("fraise", 480)

# Chaque gâteau est unique
gateau_chocolat.cuire(30)  # Cuisson du gâteau chocolat pendant 30 min
gateau_vanille.cuire(25)   # Cuisson du gâteau vanille pendant 25 min
```

## Les 4 Concepts Fondamentaux

### 1. Classe
**Définition :** Modèle abstrait qui définit la structure et le comportement.

```python
class Personne:
    """Ceci est une classe - le modèle"""
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans")
```

### 2. Objet (Instance)
**Définition :** Réalisation concrète créée à partir d'une classe.

```python
# Création d'objets (instances)
alice = Personne("Alice", 25)
bob = Personne("Bob", 30)

# Ce sont deux objets différents
alice.se_presenter()  # Bonjour, je m'appelle Alice et j'ai 25 ans
bob.se_presenter()    # Bonjour, je m'appelle Bob et j'ai 30 ans
```

### 3. Attributs
**Définition :** Variables qui stockent l'état d'un objet.

```python
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire  # Attribut
        self.solde = solde          # Attribut
        self.operations = []        # Attribut (liste)

compte = CompteBancaire("Alice", 1000)
print(compte.titulaire)  # Alice
print(compte.solde)      # 1000
```

### 4. Méthodes
**Définition :** Fonctions qui définissent le comportement d'un objet.

```python
class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):  # Méthode
        self.solde += montant
        print(f"Dépôt de {montant}€. Nouveau solde : {self.solde}€")

    def retirer(self, montant):  # Méthode
        if montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant}€. Nouveau solde : {self.solde}€")
        else:
            print("Solde insuffisant")

compte = CompteBancaire("Alice", 1000)
compte.deposer(500)   # Dépôt de 500€. Nouveau solde : 1500€
compte.retirer(200)   # Retrait de 200€. Nouveau solde : 1300€
```

## Encapsulation

### Principe
**Regrouper** les données (attributs) et les comportements (méthodes) qui opèrent sur ces données dans une même entité (classe).

### Exemple Concret : Thermostat

```python
class Thermostat:
    def __init__(self, temperature_cible):
        self.temperature_cible = temperature_cible
        self._temperature_actuelle = 20  # Attribut "protégé"

    def augmenter(self, degres):
        """Méthode pour modifier de façon contrôlée"""
        self._temperature_actuelle += degres
        self._verifier_limites()

    def diminuer(self, degres):
        """Méthode pour modifier de façon contrôlée"""
        self._temperature_actuelle -= degres
        self._verifier_limites()

    def _verifier_limites(self):
        """Méthode privée (convention _)"""
        if self._temperature_actuelle > 30:
            self._temperature_actuelle = 30
            print("Température maximale atteinte (30°C)")
        elif self._temperature_actuelle < 10:
            self._temperature_actuelle = 10
            print("Température minimale atteinte (10°C)")

    def afficher_temperature(self):
        print(f"Température actuelle : {self._temperature_actuelle}°C")
        print(f"Température cible : {self.temperature_cible}°C")

# Utilisation
thermostat = Thermostat(22)
thermostat.afficher_temperature()
thermostat.augmenter(5)
thermostat.augmenter(10)  # Sera limité à 30°C
```

## Comparaison Paradigmes

### Procédural
```python
# Données
nom_produit = "Ordinateur"
prix_produit = 1200
stock_produit = 5

# Fonctions séparées
def afficher_produit(nom, prix, stock):
    print(f"{nom} - {prix}€ (Stock: {stock})")

def vendre_produit(quantite):
    global stock_produit
    if quantite <= stock_produit:
        stock_produit -= quantite
    else:
        print("Stock insuffisant")
```

### Orienté Objet
```python
class Produit:
    """Données et comportements regroupés"""
    def __init__(self, nom, prix, stock):
        self.nom = nom
        self.prix = prix
        self.stock = stock

    def afficher(self):
        print(f"{self.nom} - {self.prix}€ (Stock: {self.stock})")

    def vendre(self, quantite):
        if quantite <= self.stock:
            self.stock -= quantite
            print(f"{quantite} unité(s) vendue(s)")
        else:
            print("Stock insuffisant")

# Plus clair, plus maintenable
ordi = Produit("Ordinateur", 1200, 5)
ordi.afficher()
ordi.vendre(2)
ordi.afficher()
```

## Exercice Pratique : Création d'une Classe Simple

### Exercice 1 : Classe Livre
```python
class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages
        self.page_actuelle = 0

    def afficher_info(self):
        print(f"📖 '{self.titre}' par {self.auteur}")
        print(f"   Pages : {self.pages}")
        print(f"   Page actuelle : {self.page_actuelle}")

    def lire(self, nb_pages):
        if self.page_actuelle + nb_pages <= self.pages:
            self.page_actuelle += nb_pages
            print(f"Vous avez lu {nb_pages} pages")
        else:
            print("Pas assez de pages restantes")

    def est_termine(self):
        return self.page_actuelle >= self.pages

# Test
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
mon_livre.afficher_info()
mon_livre.lire(30)
mon_livre.afficher_info()
```

## Pièges Courants

### Oublier self
```python
# ❌ Erreur
class MaClasse:
    def ma_methode():  # Manque self !
        print("Hello")

# ✅ Correct
class MaClasse:
    def ma_methode(self):
        print("Hello")
```

### Confondre classe et instance
```python
# ❌ Erreur
class Chien:
    nom = "Rex"  # Attribut de classe (partagé)

chien1 = Chien()
chien2 = Chien()
chien1.nom = "Max"
# Les deux chiens ont des noms différents maintenant

# ✅ Correct
class Chien:
    def __init__(self, nom):
        self.nom = nom  # Attribut d'instance (unique)

chien1 = Chien("Max")
chien2 = Chien("Rex")
```

### Modifier directement les attributs
```python
# ⚠️ Pas idéal (pas de validation)
compte.solde = -1000  # Solde négatif accepté !

# ✅ Mieux (avec validation)
class CompteBancaire:
    def __init__(self, solde):
        self.solde = solde

    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
        else:
            print("Solde insuffisant")
```

## Checklist de Maîtrise

- [ ] Je comprends la différence entre classe et objet
- [ ] Je sais créer une classe simple
- [ ] Je comprends le rôle de `self`
- [ ] Je peux créer plusieurs instances d'une classe
- [ ] Je comprends l'encapsulation et ses avantages
- [ ] Je sais quand utiliser la POO vs le procédural

**La POO n'est pas une option, c'est une nécessité pour structurer vos projets professionnels !**

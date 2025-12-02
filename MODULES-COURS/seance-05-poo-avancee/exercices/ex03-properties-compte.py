"""
Exercice 3 : CompteBancaire avec Properties et Validation
Objectif : Utiliser @property pour getters/setters avec validation
"""

print("=== EXERCICE 3 : COMPTE BANCAIRE AVEC PROPERTIES ===\n")

# TODO: Créer une classe CompteBancaire avec :
# - Attribut _solde (protégé, commence par _)
# - Attribut _taux_interet (protégé)
# - Méthode __init__(solde_initial, taux_interet)
# - Constructeur alternatif avec @classmethod
#
# - @property solde (getter) qui retourne self._solde
# - @solde.setter qui :
#   * Valide que le solde >= 0
#   * Lève ValueError si négatif
#   * Sinon, modifie self._solde
#
# - @property taux_interet (getter)
# - @taux_interet.setter qui :
#   * Valide que le taux est entre 0 et 100
#   * Lève ValueError sinon
#
# - @property interets_annuels (getter LECTURE SEULE)
#   * Calcule et retourne solde * taux / 100
#   * Pas de setter !
#
# - Méthode deposer(montant) qui utilise le setter
# - Méthode retirer(montant) qui utilise le setter
# - Méthode __str__()

# Votre code ici :
class CompteBancaire:
    def __init__(self, solde_initial, taux_interet):
        self._solde = 0
        self._taux_interet = 0
        self.solde = solde_initial  # Utilise le setter
        self.taux_interet = taux_interet  # Utilise le setter

    @property
    def solde(self):
        return self._solde

    @solde.setter
    def solde(self, valeur):
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif.")
        self._solde = valeur

    @property
    def taux_interet(self):
        return self._taux_interet

    @taux_interet.setter
    def taux_interet(self, valeur):
        if not (0 <= valeur <= 100):
            raise ValueError("Le taux d'intérêt doit être entre 0 et 100.")
        self._taux_interet = valeur

    @property
    def interets_annuels(self):
        return self._solde * self._taux_interet / 100

    def deposer(self, montant):
        if montant < 0:
            raise ValueError("Le montant à déposer doit être positif.")
        self.solde += montant  # Utilise le setter

    def retirer(self, montant):
        if montant < 0:
            raise ValueError("Le montant à retirer doit être positif.")
        if montant > self._solde:
            raise ValueError("Fonds insuffisants pour ce retrait.")
        self.solde -= montant  # Utilise le setter

    def __str__(self):
        return (f"CompteBancaire(solde={self._solde}€, "
                f"taux_interet={self._taux_interet}%, "
                f"interets_annuels={self.interets_annuels}€)")

# Tests
if __name__ == "__main__":
    print("--- Test Création ---")
    compte = CompteBancaire(1000, 2.5)
    print(f"Solde : {compte.solde}€")
    print(f"Taux : {compte.taux_interet}%")
    print(f"Intérêts annuels : {compte.interets_annuels}€")

    print("\n--- Test Dépôt ---")
    compte.deposer(500)
    print(f"Nouveau solde : {compte.solde}€")
    print(f"Nouveaux intérêts : {compte.interets_annuels}€")

    print("\n--- Test Retrait ---")
    compte.retirer(200)
    print(f"Solde après retrait : {compte.solde}€")

    print("\n--- Test Validation Solde ---")
    try:
        compte.solde = -100
    except ValueError as e:
        print(f"✅ Erreur attendue : {e}")

    print("\n--- Test Validation Taux ---")
    try:
        compte.taux_interet = 150
    except ValueError as e:
        print(f"✅ Erreur attendue : {e}")

    print("\n--- Test Property Lecture Seule ---")
    try:
        compte.interets_annuels = 100  # Ne devrait pas marcher
    except AttributeError as e:
        print(f"✅ Erreur attendue : Property en lecture seule")

    print("\n--- Affichage Final ---")
    print(compte)

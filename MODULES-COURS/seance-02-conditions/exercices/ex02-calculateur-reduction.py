"""
Exercice 2 : Calculateur de Réduction
Objectif : Appliquer des réductions selon différents critères
"""

print("=== EXERCICE 2 : CALCULATEUR DE RÉDUCTION ===")

def calculer_reduction(montant_achat, est_membre, jour_semaine, heure_achat):
    """
    Calcule la réduction applicable selon plusieurs critères
    """
    reduction = 0
    raison = "Aucune réduction"
    
    # Critère 1 : Montant d'achat
    if montant_achat > 200:
        reduction = 0.20  # 20%
        raison = "Réduction fidélité (achat > 200€)"
    elif montant_achat > 100:
        reduction = 0.10  # 10%
        raison = "Réduction fidélité (achat > 100€)"
    elif montant_achat > 50:
        reduction = 0.05  # 5%
        raison = "Réduction fidélité (achat > 50€)"
    
    # Critère 2 : Membre du programme
    if est_membre:
        if reduction < 0.15:  # La réduction membre ne dépasse pas 15%
            reduction = 0.15
            raison = "Réduction membre (15%)"
        else:
            raison += " + bonus membre"
    
    # Critère 3 : Jour de la semaine (mercredi)
    if jour_semaine.lower() == "mercredi":
        if reduction < 0.25:  # Maximum 25% le mercredi
            ancienne_reduction = reduction
            reduction = 0.25
            raison = f"Promotion mercredi (25% au lieu de {ancienne_reduction*100:.0f}%)"
    
    # Critère 4 : Heure creuse (14h-16h)
    if 14 <= heure_achat < 16:
        reduction_supplementaire = 0.05
        reduction += reduction_supplementaire
        if reduction > 0.30:  # Maximum 30%
            reduction = 0.30
        raison += f" + heure creuse ({reduction_supplementaire*100:.0f}%)"
    
    # Maximum 30% de réduction totale
    if reduction > 0.30:
        reduction = 0.30
        raison += " (plafond 30% atteint)"
    
    return reduction, raison

def main():
    print("���️  CALCULATEUR DE RÉDUCTIONS MULTICRITÈRES")
    print("=" * 55)
    
    try:
        # Saisie des informations
        montant = float(input("Montant de l'achat (€) : "))
        membre = input("Êtes-vous membre ? (oui/non) : ").lower() == "oui"
        jour = input("Jour de la semaine : ")
        heure = int(input("Heure de l'achat (0-23) : "))
        
        # Validation
        if montant < 0:
            print("❌ Le montant ne peut pas être négatif")
            return
        
        if not (0 <= heure <= 23):
            print("❌ L'heure doit être entre 0 et 23")
            return
        
        # Calcul
        reduction, raison = calculer_reduction(montant, membre, jour, heure)
        montant_reduit = montant * (1 - reduction)
        economie = montant - montant_reduit
        
        # Affichage détaillé
        print("\n" + "��� DÉTAIL DE LA COMMANDE".center(55, "="))
        print(f"Montant initial : {montant:.2f}€")
        print(f"Réduction appliquée : {reduction*100:.1f}%")
        print(f"Motif : {raison}")
        print(f"Économie réalisée : {economie:.2f}€")
        print(f"Montant final : {montant_reduit:.2f}€")
        
        # Informations supplémentaires
        print("\n" + "��� CONDITIONS DE RÉDUCTION".center(55, "-"))
        print("• Achat > 50€ : 5% de réduction")
        print("• Achat > 100€ : 10% de réduction")
        print("• Achat > 200€ : 20% de réduction")
        print("• Membre : 15% de réduction")
        print("• Mercredi : 25% de réduction maximum")
        print("• Heure creuse (14h-16h) : +5% de réduction")
        print("• Plafond total : 30% de réduction maximum")
        
    except ValueError:
        print("❌ Erreur : Veuillez entrer des valeurs valides")

# Lancement
if __name__ == "__main__":
    main()

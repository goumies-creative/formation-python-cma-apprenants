"""
Exercice 1 : Calculateur d'IMC avec Conseils
Objectif : Utiliser les conditions pour donner des conseils santé
"""

print("=== EXERCICE 1 : CALCULATEUR D'IMC ===")

def calculer_imc(poids, taille):
    """Calcule l'IMC et retourne la catégorie"""
    imc = poids / (taille ** 2)
    return imc

def analyser_imc(imc):
    """Analyse l'IMC et retourne catégorie et conseils"""
    if imc < 16.5:
        categorie = "Dénutrition"
        conseil = "Consultez un médecin rapidement"
    elif imc < 18.5:
        categorie = "Maigreur"
        conseil = "Essayez de prendre un peu de poids avec une alimentation équilibrée"
    elif imc < 25:
        categorie = "Corpulence normale"
        conseil = "Parfait ! Continuez vos bonnes habitudes"
    elif imc < 30:
        categorie = "Surpoids"
        conseil = "Un peu d'exercice et une alimentation équilibrée vous aideront"
    elif imc < 35:
        categorie = "Obésité modérée"
        conseil = "Consultez un nutritionniste pour un accompagnement"
    elif imc < 40:
        categorie = "Obésité sévère"
        conseil = "Il est important de consulter un professionnel de santé"
    else:
        categorie = "Obésité morbide"
        conseil = "Consultez un médecin urgemment"
    
    return categorie, conseil

def main():
    print("CALCULATEUR D'INDICE DE MASSE CORPORELLE")
    print("=" * 50)
    
    try:
        # Saisie utilisateur
        poids = float(input("Entrez votre poids en kg : "))
        taille = float(input("Entrez votre taille en mètres : "))
        
        # Validation des entrées
        if poids <= 0 or taille <= 0:
            print("❌ Erreur : Le poids et la taille doivent être positifs")
            return
        
        if taille > 3:  # Probablement en cm au lieu de mètres
            print("⚠️  Attention : La taille est probablement en cm, conversion en mètres...")
            taille = taille / 100
        
        # Calcul
        imc = calculer_imc(poids, taille)
        categorie, conseil = analyser_imc(imc)
        
        # Affichage résultats
        print("\n" + "RÉSULTATS".center(50, "="))
        print(f"Poids : {poids} kg")
        print(f"Taille : {taille} m")
        print(f"IMC : {imc:.1f}")
        print(f"Catégorie : {categorie}")
        print(f"Conseil : {conseil}")
        
        # Détails supplémentaires
        print("\n" + "INFORMATIONS COMPLÉMENTAIRES".center(50, "-"))
        print("Échelle IMC :")
        print("- < 18.5 : Maigreur")
        print("- 18.5-25 : Normal")
        print("- 25-30 : Surpoids") 
        print("- 30-35 : Obésité modérée")
        print("- 35-40 : Obésité sévère")
        print("- > 40 : Obésité morbide")
        
    except ValueError:
        print("❌ Erreur : Veuillez entrer des nombres valides")
    except ZeroDivisionError:
        print("❌ Erreur : La taille ne peut pas être zéro")

# Lancement
if __name__ == "__main__":
    main()

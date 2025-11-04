"""
Exercice 4 : Projet - Validation d'Email
Objectif : Créer un système complet de validation d'email
"""

print("=== EXERCICE 4 : VALIDATEUR D'EMAIL ===")

def valider_email(email):
    """
    Valide une adresse email selon plusieurs critères
    Retourne True si valide, False sinon avec message d'erreur
    """
    
    # Critères de validation
    if not email:
        return False, "L'email ne peut pas être vide"
    
    # Doit contenir un @
    if "@" not in email:
        return False, "L'email doit contenir un @"
    
    # Séparation nom de domaine et partie locale
    parties = email.split("@")
    if len(parties) != 2:
        return False, "Format d'email invalide"
    
    partie_locale, domaine = parties
    
    # Vérification partie locale
    if not partie_locale:
        return False, "La partie avant @ ne peut pas être vide"
    
    if len(partie_locale) > 64:
        return False, "La partie avant @ est trop longue (max 64 caractères)"
    
    # Vérification domaine
    if not domaine:
        return False, "Le domaine ne peut pas être vide"
    
    if "." not in domaine:
        return False, "Le domaine doit contenir un point"
    
    # Vérification extension
    extension = domaine.split(".")[-1]
    extensions_valides = ["com", "fr", "org", "net", "io", "dev"]
    
    if extension not in extensions_valides:
        return False, f"Extension '{extension}' non reconnue"
    
    # Si tout est bon
    return True, "Email valide !"

# Programme principal
def main():
    print("VALIDATEUR D'ADRESSE EMAIL")
    print("=" * 40)
    
    while True:
        email = input("\nEntrez une adresse email (ou 'quit' pour quitter) : ")
        
        if email.lower() == 'quit':
            print("Merci d'avoir utilisé le validateur !")
            break
        
        # Validation
        est_valide, message = valider_email(email)
        
        # Affichage résultat
        if est_valide:
            print(f"✅ {message}")
            
            # Analyse supplémentaire
            nom_utilisateur = email.split("@")[0]
            domaine = email.split("@")[1]
            
            print(f"   Nom d'utilisateur : {nom_utilisateur}")
            print(f"   Domaine : {domaine}")
            print(f"   Email complet : {email}")
            
        else:
            print(f"❌ {message}")
        
        print("-" * 40)

# Lancement du programme
if __name__ == "__main__":
    main()

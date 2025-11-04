"""
Exercice 1 : Générateur de Tables de Multiplication
Objectif : Maîtriser les boucles for et le formatage
"""

print("=== EXERCICE 1 : TABLES DE MULTIPLICATION ===")

def afficher_table(nombre, debut=1, fin=10):
    """Affiche la table de multiplication d'un nombre"""
    print(f"\nTable de multiplication de {nombre}")
    print("=" * 30)
    
    for i in range(debut, fin + 2):
        resultat = nombre * i
        print(f"{nombre:2d} × {i:2d} = {resultat:3d}")
    
    print("=" * 30)

def afficher_toutes_tables(debut=1, fin=10):
    """Affiche toutes les tables de multiplication"""
    print(f"\nTOUTES LES TABLES DE {debut} À {fin}")
    print("=" * 50)
    
    for table in range(debut, fin + 1):
        print(f"\nTable de {table}:")
        print("-" * 20)
        for multiplicateur in range(1, 11):
            resultat = table * multiplicateur
            print(f"{table:2d} × {multiplicateur:2d} = {resultat:3d}")

def table_personnalisee():
    """Demande à l'utilisateur quelle table il veut voir"""
    try:
        nombre = int(input("\nEntrez le nombre pour la table : "))
        debut = int(input("Début de la table (défaut 1) : ") or "1")
        fin = int(input("Fin de la table (défaut 10) : ") or "10")
        
        if debut > fin:
            print("❌ Erreur : Le début ne peut pas être après la fin")
            return
        
        afficher_table(nombre, debut, fin)
        
    except ValueError:
        print("❌ Veuillez entrer des nombres valides")

def main():
    print("GÉNÉRATEUR DE TABLES DE MULTIPLICATION")
    print("=" * 45)
    
    while True:
        print("\nOptions disponibles :")
        print("1. Table spécifique")
        print("2. Toutes les tables de 1 à 10")
        print("3. Tables personnalisées")
        print("4. Quitter")
        
        choix = input("\nVotre choix (1-4) : ")
        
        if choix == "1":
            try:
                nombre = int(input("Quelle table voulez-vous ? "))
                afficher_table(nombre)
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")
                
        elif choix == "2":
            afficher_toutes_tables()
            
        elif choix == "3":
            table_personnalisee()
            
        elif choix == "4":
            print("Merci d'avoir utilisé le générateur !")
            break
            
        else:
            print("❌ Choix invalide. Veuillez choisir 1, 2, 3 ou 4.")

# Lancement
if __name__ == "__main__":
    main()

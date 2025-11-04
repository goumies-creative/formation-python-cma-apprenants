"""
Exercice 2 : Détecteur de Nombres Premiers
Objectif : Utiliser les boucles pour résoudre un problème mathématique
"""

print("=== EXERCICE 2 : NOMBRES PREMIERS ===")

def est_premier(nombre):
    """
    Vérifie si un nombre est premier
    Un nombre premier est divisible seulement par 1 et lui-même
    """
    if nombre < 2:
        return False
    
    # Vérifie les diviseurs de 2 à racine carrée du nombre
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    
    return True

def trouver_premiers(limite):
    """Trouve tous les nombres premiers jusqu'à une limite"""
    premiers = []
    
    for nombre in range(2, limite + 1):
        if est_premier(nombre):
            premiers.append(nombre)
    
    return premiers

def decomposer_facteurs_premiers(nombre):
    """Décompose un nombre en facteurs premiers"""
    if nombre < 2:
        return []
    
    facteurs = []
    diviseur = 2
    temp = nombre
    
    while temp > 1:
        if temp % diviseur == 0:
            facteurs.append(diviseur)
            temp = temp // diviseur
        else:
            diviseur += 1
    
    return facteurs

def main():
    print("ANALYSE DES NOMBRES PREMIERS")
    print("=" * 40)
    
    while True:
        print("\nOptions :")
        print("1. Vérifier si un nombre est premier")
        print("2. Lister les nombres premiers jusqu'à N")
        print("3. Décomposer en facteurs premiers")
        print("4. Quitter")
        
        choix = input("\nVotre choix (1-4) : ")
        
        if choix == "1":
            try:
                n = int(input("Entrez un nombre : "))
                if est_premier(n):
                    print(f"✅ {n} est un nombre premier !")
                else:
                    print(f"❌ {n} n'est pas un nombre premier")
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")
                
        elif choix == "2":
            try:
                limite = int(input("Limite maximum : "))
                if limite < 2:
                    print("❌ La limite doit être au moins 2")
                    continue
                    
                premiers = trouver_premiers(limite)
                print(f"\nNombres premiers jusqu'à {limite} :")
                
                # Affichage en colonnes
                for i in range(0, len(premiers), 10):
                    ligne = premiers[i:i+10]
                    print(" ".join(f"{p:4d}" for p in ligne))
                
                print(f"\nTotal : {len(premiers)} nombres premiers")
                
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")
                
        elif choix == "3":
            try:
                n = int(input("Nombre à décomposer : "))
                if n < 2:
                    print("❌ Le nombre doit être au moins 2")
                    continue
                    
                facteurs = decomposer_facteurs_premiers(n)
                if facteurs:
                    # Regrouper les facteurs multiples
                    from collections import Counter
                    compteur = Counter(facteurs)
                    
                    decomposition = " × ".join(
                        f"{facteur}^{puissance}" if puissance > 1 else str(facteur)
                        for facteur, puissance in compteur.items()
                    )
                    
                    print(f"{n} = {decomposition}")
                else:
                    print(f"{n} est premier !")
                    
            except ValueError:
                print("❌ Veuillez entrer un nombre valide")
                
        elif choix == "4":
            print("Au revoir !")
            break
            
        else:
            print("❌ Choix invalide")

# Lancement
if __name__ == "__main__":
    main()

def calculer_tva(prix, taux=0.20):
    return prix * (1 + taux)

def est_pair(n):
    return n % 2 == 0

print(f"__name__ = {__name__}")
# Code exécuté SEULEMENT si lancé directement
if __name__ == "__main__":
    print("Test du module")
    print(calculer_tva(100))  # 120.0
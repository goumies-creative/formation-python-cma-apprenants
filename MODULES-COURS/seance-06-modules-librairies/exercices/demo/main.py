import utils

# Utiliser les fonctions du module
prix_ttc = utils.calculer_tva(50)
print(prix_ttc)  # 60.0

if utils.est_pair(10):
    print("10 est pair")

# Ou avec from...import
from utils import calculer_tva
prix_ttc = calculer_tva(50)  # Sans préfixe

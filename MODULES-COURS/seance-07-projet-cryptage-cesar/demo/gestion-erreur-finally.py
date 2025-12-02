try:
    # Code qui PEUT échouer
    resultat = 10 / 0
except ZeroDivisionError:
    # Exécuté SI erreur
    print("Division par zéro impossible")
else:
    # Exécuté SI PAS d'erreur
    print("Tout s'est bien passé")
finally:
    # Exécuté TOUJOURS
    print("Nettoyage")
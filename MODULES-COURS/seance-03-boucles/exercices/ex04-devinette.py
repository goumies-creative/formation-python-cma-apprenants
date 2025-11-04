nombre_secret = 7
devinette = 0

while devinette != nombre_secret:
    devinette = int(input("devinettez le nombre (1-10) : "))
    
    if devinette < nombre_secret:
        print("Trop petit !")
    elif devinette > nombre_secret:
        print("Trop grand !")
    else:
        print("Gagné ! 🎉")
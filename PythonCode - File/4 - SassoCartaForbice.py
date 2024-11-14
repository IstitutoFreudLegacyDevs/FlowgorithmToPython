import random
random.seed()   #Prepare random number generator

print("Scegli fra Carta, Forbice e Sasso")
scelta = input()
while scelta != "carta" and scelta != "forbice" and scelta != "sasso" and scelta != "esci":
    print("Input invalido")
    scelta = input()
while scelta != "esci":
    numero = int(random.random() * 3)
    if numero == 0:
        computer = "carta"
    else:
        if numero == 1:
            computer = "forbice"
        else:
            computer = "sasso"
    if scelta == "carta" and computer == "sasso" or scelta == "forbice" and computer == "carta" or scelta == "sasso" and computer == "forbice":
        print(computer)
        print("Hai vinto!")
    else:
        if scelta == "carta" and computer == "carta" or scelta == "forbice" and computer == "forbice" or scelta == "sasso" and computer == "sasso":
            print(computer)
            print("Hai pareggiato!")
        else:
            print(computer)
            print("Hai perso!")
    scelta = input()
    while scelta != "carta" and scelta != "forbice" and scelta != "sasso" and scelta != "esci":
        print("Input invalido")
        scelta = input()

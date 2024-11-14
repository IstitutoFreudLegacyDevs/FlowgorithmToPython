print("Inserisci un numero")
numero = int(input())
if numero > 0:
    print("Il numero è positivo, maggiore di zero!")
else:
    if numero == 0:
        print("Il numero è zero!")
    else:
        print("Il numero è negativo, minore di zero!")
if numero % 2 == 0:
    print("Il numero è pari!")
else:
    print("Il numero è dispari!")

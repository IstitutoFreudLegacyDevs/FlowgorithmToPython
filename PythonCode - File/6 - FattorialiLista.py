lista = [0] * (3)
fattoriali = [0] * (3)

print("dammi una lista di valori dei quali vuoi il fattoriale")
for i in range(0, 2 + 1, 1):
    lista[i] = int(input())
for i in range(0, 2 + 1, 1):
    risultato = 1
    for k in range(1, lista[i] + 1, 1):
        risultato = risultato * k
    fattoriali[i] = risultato
    print(fattoriali[i])

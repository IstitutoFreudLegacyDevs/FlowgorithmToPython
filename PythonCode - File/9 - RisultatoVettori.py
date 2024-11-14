risultato = 1
print("Inserisci il numero di cui desideri sapere il fattoriale")
numero = int(input())
for i in range(1, numero + 1, 1):
    risultato = risultato * i
print("Il fattoriale del numero è:")
print(risultato)

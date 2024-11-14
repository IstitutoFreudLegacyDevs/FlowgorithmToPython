print("A quale PIN vuoi attaccare il potenziometro")
analogPIN = input()
print("Digita TRUE per modalità OUTPUT, FALSE per INPUT")
pinmode = (input().lower() == 'true')

# DICHIARAZIONI DI RICHIESTA INPUT MAX 3 VOLTE
chiestocount = 0
maxvoltechiesto = 3

while chiestocount < maxvoltechiesto:
    print("Digita il numero di livelli tra 10 e 1023")
    livelli = int(input())
    print("La lettura del potenziometro è:")
    print(livelli)
    
    chiestocount += 1

# DOPO 3 VOLTE ESCE DAL CICLO
if chiestocount >= maxvoltechiesto:
    print("")

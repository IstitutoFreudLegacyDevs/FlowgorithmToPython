ledstate = False
print("Inserisci il pin dove attaccare il led")
lED = int(input())
print("Digita TRUE per modalità INPUT o FALSE per l'OUTPUT")
pinmode = (input().lower() == 'true')

# DICHIARAZIONI PER PRINTARE ledstate MASSIMO 6 VOLTE
printcount = 0
printmassimi = 6

while printcount < printmassimi:
    ledstate = True
    print(ledstate)
    ledstate = False
    print(ledstate)
    printcount += 1

# DOPO 6 PRINT ESCE DAL CICLO
if printcount >= printmassimi:
    print("")

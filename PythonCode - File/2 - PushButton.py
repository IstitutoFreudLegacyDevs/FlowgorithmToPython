ledstate = False
buttonstate = False
print("A quale PIN vuoi attaccare il led?")
lED = int(input())
print("Seleziona la modalità del PIN, seleziona TRUE per OUTPUT")
pinmode1 = (input().lower() == 'true')
print("A quale PIN vuoi attaccare il pushbutton?")
pushbutton = int(input())
print("A quale modalità del PIN del pushbutton, seleziona TRUE per OUTPUT")
pinmode1 = (input().lower() == 'true')

# DICHIARAZIONI PER RICHIESTA MASSIMA DI 3 VOLTE D'INSERIMENTO INPUT
volteinputchiesto = 0
voltemassimeperrichiestainput = 3

while volteinputchiesto < voltemassimeperrichiestainput:
    print("Digita TRUE se il pushbutton è schiacciato")
    buttonstate = (input().lower() == 'true')
    
    if buttonstate == True:
        ledstate = True
        print(ledstate)
    else:
        ledstate = False
        print(ledstate)
    
    volteinputchiesto += 1

# DOPO TRE RICHIESTE ESCE DAL CICLO
if volteinputchiesto >= voltemassimeperrichiestainput:
    print("")

ledPins = [0] * (5)
ledStates = [False] * (5)
pinmode = [False] * (5)

ledcount = 5
for i in range(0, ledcount - 1 + 1, 1):
    print("Dimmi i PIN al quale attaccare i LED")
    ledPins[i] = int(input())
    ledStates[i] = False
for i in range(0, ledcount - 1 + 1, 1):
    print("Dimmi la modalità dei PIN")
    pinmode[i] = (input().lower() == 'true')

print("Dimmi il livello corrispondente del potenziometro")
livelli = int(input())
ledlevel = float(livelli * ledcount) / 1023
print("Il livello è: ")
print(ledlevel)
for thisLed in range(0, ledcount - 1 + 1, 1):
    if thisLed < ledlevel:
        ledStates[thisLed] = True
    else:
        ledStates[thisLed] = False
    print(ledStates[thisLed])

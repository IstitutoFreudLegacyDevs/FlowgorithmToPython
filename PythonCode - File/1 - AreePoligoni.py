print("Ciao, sono un calcolatore di aree, digita q per il quadrato, t per il triangolo ")
scelta = input()
if scelta == "q":
    print("Calcolo l'area del quadrato, dammi il lato")
    l = float(input())
    while l <= 0:
        print("Scemo dammi un lato positivo!")
        l = float(input())
    a = l ** 2
else:
    if scelta == "t":
        print("Calcolo l'area del triangolo, dammi il lato")
        b = float(input())
        while b <= 0:
            print("Scemo dammi una base positivo!")
            b = float(input())
        print("dammi l'altezza")
        h = float(input())
        while h <= 0:
            print("Scemo dammi un'altezza positiva!")
            h = float(input())
        a = b * h / 2
    else:
        print("hai scelto male! ritenta")
        a = 0
print("l'area della figura e:")
print(a)

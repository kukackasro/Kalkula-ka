print("Vítejte v kalkulačce, jestli chcete program ukončit napištw konec do operace.")
while True:
    cislo1 = float(input("Zadej první číslo:"))
    cislo2 = float(input("Zadej druhé číslo:"))
    operace = input("Zadej operaci +, -, *, /, **,//")
    if operace == "+":
        print(cislo1 + cislo2)
    elif operace == "-":
        print(cislo1 - cislo2)
    elif operace == "*":
        print(cislo1 * cislo2 )
    elif (cislo1 == 0 or cislo2 == 0) and operace == "/":
        print("Nulou nelze delit")
    elif operace == "/":
        print(cislo1 / cislo2)
    elif operace == "**":
        print(cislo1 ** cislo2)
    elif operace == '//':
        print( cislo1 // cislo2) 
    elif operace == "konec":
        print("Díky za použití kalkulačky")
        break
    else:
        print("Proč tam něco píšeš")
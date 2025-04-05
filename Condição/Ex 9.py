print("ex 9")

numero = int  (input("digite um numero:"))

if numero > 0 and numero < 25:
    print('Está no intervalo 1')
elif numero >25 and numero <50:
    print ("Está no intervalo 2")
elif numero >50 and numero <75:
    print ("Está no intervalo 3")
elif numero >75 and numero <100:
    print ("Está no intervalo 4")
else:
    print("fora de intervalo")
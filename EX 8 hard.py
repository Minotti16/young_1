base = int(input('digite a base: '))
expoente = int(input('digite um expoente: '))

for i in range(1,expoente):
    base ^= base
    print(base, end= ' ')
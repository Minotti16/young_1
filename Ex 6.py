print('ex 6')

numero = int  (input('digite um numero: '))
numero2 = int  (input('digite um numero: '))
numero3 = int  (input('digite um numero: '))

if numero > numero2 and numero3:
    print ('O numero 1 é maior')
elif numero2 > numero and numero3:
    print('O numero 2 é maior')
elif numero3 > numero and numero2:
    print('O numero 3 é maior')
if numero2 == numero < numero3:
    print("O numero 1 e 2 são igual")
elif numero == numero3 < numero2:
    print("O numero 1 e 3 são igual")
elif numero2 == numero3 < numero:
    print("O numero 2 e 3 são igual")
elif numero2 == numero3 and numero:
    print('Todos são igual')

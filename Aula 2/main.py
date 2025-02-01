print('ex 1')
numero = int  (input('digite um numero: '))

if numero % 2 == 0:
    print('é par')
else:
    print('é ímpar')
print ('fim')

print('ex 2')
numero = int  (input('digite um numero: '))

if numero > 0:
    print('positivo')
elif numero < 0:
    print('negativo')
else:
    print("zero")    

print('ex 3')
numero = int  (input('digite um numero: '))
numero1 = int  (input('digite um numero: '))

if numero > numero1:
    print("o primeiro numero é maior")
elif numero < numero1:
     print("o segundo numero é maior")
else:
    print('são iguais')

print('ex 4')

nota = int(input('digite um numero de 0 a 10: '))

if nota > 6:
    print('Aprovado')
else:
    print("Reprovado")

print('ex 5')

dia = int(input('digite um numero de 1 a 7: '))

if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda-feira")
elif dia == 3:
    print("terça-feira")
elif dia == 4:
    print("quarta-feira")
elif dia == 5:
    print("quinta-feira")
elif dia == 6:
    print("sexta-feira")
elif dia == 7:
    print("sabádo-feira")
else:
    print('dia inválido')


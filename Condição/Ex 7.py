print('ex 7')

import random

numero_random = random.randint(1,10)

numeroPalpite = 0
while(numeroPalpite != numero_random):
    numeroPalpite = int  (input("digite um numero de 1 , 10:"))
if numeroPalpite == numero_random:
    print ('Parabéns! Você acertou')
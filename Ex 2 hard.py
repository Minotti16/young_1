import random

num = random.randint(1,100)

num_palpite = 0
while num_palpite != num:
    num_palpite = int(input('digite um número'))
    if num_palpite > num:
      print('muito alto')
    elif num_palpite < num:
       print('muito baixo')
    else:
        print('Parabéns você acertou o número')
        break
       
 
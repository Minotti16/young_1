while True:
    frase = input('Digite uma frase: ')
    caractere = input ('Digite o carractere que deseja contar: ')
    if len(caractere) != 1:
        print('Digite apenas um caractere: ')
        continue
    else:
        cont = frase.count(caractere)
        print(f' O caractere {caractere}, aparece {cont} vezes')
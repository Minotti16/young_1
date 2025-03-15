def fatorial():
    num = int(input('Digite um numero para fatorar '))

    for i in range(num -1,0,-1):
        num = num * i
        print(num)




while True:
    fatorial()
    resposta = input('Deseja fatorar mais um número?')
    if resposta != 's':
        print('Encerrando o programa...')
        break

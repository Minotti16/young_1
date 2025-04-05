import Calculadora

def menu():
    while True:
        print('**********************')
        print('         Calculadora  ')
        print('**********************')
        print('1 - Somar')
        print('2 - Subitrair ')
        print('3 - Multiplicar')
        print('4 - Dividir')
        print('5 - Sair')
        print('**********************')
        opcao = int(input('Opção desejada: '))
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
        if opcao == 1:
            print(Calculadora.somar(a,b))
            pause = input(' ')
        elif opcao == 2:
            print(Calculadora.subitrair(a,b))
            pause = input(' ')
        elif opcao == 3:
            print(Calculadora.multiplicar(a,b))
            pause = input(' ')
        elif opcao == 4:
            print(Calculadora.divisão(a,b))
            pause = input(' ')
        elif opcao == 5:
            break
        else:
            menu()

menu()
class Calculadora():
    def __init__(self):
        self.a = int(input('Digite um número: '))
        self.b = int(input('Digite um outro número: '))

    def calular(self):
        self.somar = print(self.a + self.b)
        self.subtrair = print(self.a - self.b)
        self.multiplicar = print(self.a * self.b)
        self.dividir = print(self.a / self.b)

m = Calculadora()    

def menu():
    while True:
        print('**********************')
        print('   Calculadora  ')
        print('**********************')
        print('1 - Somar')
        print('2 - Subitrair ')
        print('3 - Multiplicar')
        print('4 - Dividir')
        print('5 - Sair')
        print('**********************')
        opcao = int(input('Opção desejada: '))
        if opcao == 1:
            print(f"{m.somar}")
            pause = input(' ')
        elif opcao == 2:
            print(f"{m.subtrair}")
            pause = input(' ')
        elif opcao == 3:
            print(f"{m.multiplicar}")
            pause = input(' ')
        elif opcao == 4:
            print(f"{m.dividir}")
            pause = input(' ')
        elif opcao == 5:
            break
        else:
            menu()

menu()
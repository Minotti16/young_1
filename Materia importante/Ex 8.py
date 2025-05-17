class Calculadora():
    def __init__(self):
        self.a = int(input('Digite um número: '))
        self.b = int(input('Digite um outro número: '))

    def adiçao(self):
        return self.a + self.b
    def subtração(self):
       return self.a - self.b
    def multiplicação(self):
        return self.a * self.b
    def divisão(self):
        return self.a / self.b

m = Calculadora() 

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
            print(f"{m.adiçao()}")
            pause = input(' ')
        elif opcao == 2:
            print(f"{m.subtração()}")
            pause = input(' ')
        elif opcao == 3:
            print(f"{m.multiplicação()}")
            pause = input(' ')
        elif opcao == 4:
            print(f"{m.divisão()}")
            pause = input(' ')
        elif opcao == 5:
            break
        else:
            continue
        
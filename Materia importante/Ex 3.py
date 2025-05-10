class Carro():
    def __init__(self):
        self.marca = input('Digite uma marca: ')
        self.velocidade = int(input("Digite um número: "))

    def acelerar(self):
        return self.velocidade +valor
    def freiar(self):
        return self.velocidade -valor

valor = 30    
v = Carro()
v.acelerar()
v.freiar()
print(f'{v.marca} acelerou. velocidade atual é:{v.acelerar()}')
print(f'{v.marca} freirou. velocidade atual é:{v.freiar()}')



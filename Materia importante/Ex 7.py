class CachorroComComportamento():
    def __init__(self):
        self.nome = input('Digite um nome: ')
        self.raça = input('Digite uma raça: ')

    def latir(self):
        print('Au au!')

c = CachorroComComportamento()
c.latir()
print(f'{c.nome}')
print(f'{c.raça}' )

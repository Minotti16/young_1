class CachorroComComportamento():
    def __init__(self):
        self.nome = input('Digite um nome: ')
        self.raça = input('Digite uma raça: ')

    def latir(self):
        return 'Au au!'

c = CachorroComComportamento()
print(f'O {c.nome} da raça {c.raça} disse {c.latir()}')


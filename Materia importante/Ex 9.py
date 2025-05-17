class ProdutoComDesconto():
    def __init__(self):
        self.nome = input('Digite um nome: ')
        self.preço = float(input('Digite um preço: '))

    def desconto(self):
        return f'O {self.nome} de {self.preço} foi para {self.preço * 0.25}'
    
preçofinal = ProdutoComDesconto()
print(preçofinal.desconto())
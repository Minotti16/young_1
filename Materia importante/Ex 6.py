class Livro():
    def __init__(self):
        self.titulo = input('Digite um titulo: ')
        self.autor = input('Digite um nome: ')
        self.paginas = int(input('Digite uma quantidade de paginas: '))

    def imprimir(self):
        print(self.titulo)
        print(self.autor)
        print(self.paginas)
    
L = Livro()
L.imprimir()
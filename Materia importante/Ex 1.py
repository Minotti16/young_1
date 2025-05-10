class Pessoa():
    def __init__(self):
        self.nome = input('Digite seu nome: ')
        self.idade = input('Digite sua idade: ')

    def Apresentar(self):
        return f"Olá, meu nome é {self.nome}e tenho {self.idade} anos"
    
pessoal = Pessoa()
print(pessoal.Apresentar())

    
  



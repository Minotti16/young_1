class Aluno():
    def __init__(self):
        self.nome = input('Digite um nome: ')
        self.nota1 = int(input('Digite um número: '))
        self.nota2 = int(input('Digite um outro número: '))
    
    def media(self):
        if self.nota1 + self.nota2/2 > 6:
            print(f'{self.nome} foi Aprovado')
        else:
            print(f'{self.nome} foi Reprovado')

Aluno1 = Aluno()
print(Aluno1.media())

    

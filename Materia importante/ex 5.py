class Aluno():
    def __init__(self):
        self.nome = input('Digite um nome: ')
        self.nota1 = int(input('Digite um número: '))
        self.nota2 = int(input('Digite um outro número: '))

    def media(self):
        return self.nota1 + self.nota2/2 == media

media = Aluno()

def Nota():
    if media >= 6:
        print("O Aluno passou de serie")
    else:
        print('O Aluno reprovou')
    
Nota()
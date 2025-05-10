class Aluno():
    def __init__(self):
        self.nome = input('Digite um nome: ')
        self.nota1 = float(input('Digite um número'))
        self.nota2 = float(input('Digite um outro número'))

    def media(self):
        return self.nota1 + self.nota2/2 == média

média = Aluno()
if média >= 6:
    print("O Aluno passou de serie")
else:
    print('O Aluno reprovou')
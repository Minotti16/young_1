class Retangulo():
    def __init__(self):
        self.largura = int(input("Digite um número: "))
        self.altura = int(input("Digite um outro número: "))

    def area(self):
        return self.largura * self.altura

area1 = Retangulo()
print(area1.area())      



        
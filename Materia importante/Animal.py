class AnimalSelvagem():
    def mover(self):
        print('Estou Correndo')
    
    def come(self):
        print('Comendo')

class AnimalDomestico():
    def mover(self):
        print('Estou andando')

    def getDono(self):
        return self.dono

class Cachorro(AnimalSelvagem, AnimalDomestico):
    def __init__(self, dono):
        self.dono = dono
    
    def late(self):
        print("AuAu! ")

c = Cachorro("Luis")
print(c.getDono())
c.come() 
c.late()
c.mover()

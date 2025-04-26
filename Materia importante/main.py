class Casa():

    imobiliaria = 'Ctrl Imóveis'

    def __init__(self, rua, bairro, CEP):
        self.rua = rua
        self.bairro = bairro
        self.CEP = CEP

    def getImobiliaria(self):
        return self.imobiliaria
    
    def getRua(self):
        return self.rua
    
    def getBairro(self):
        return self.bairro
    
    def getCEP(self):
        return self.CEP
    
    def setImobiliaria(self,i):
        self.imobiliaria = i

    def setRua(self,r):
        self.rua = r
    
    def setBairro(self,b):
        self.bairro = b

    def setCEP(self, c):
        self.CEP = c


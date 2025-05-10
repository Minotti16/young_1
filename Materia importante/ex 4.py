class ContaBancaria():
    def __init__(self):
      self.titular = input('Digite um nome: ')
      self.saldo = int(input('Digite um número: '))

    def depositar(self):
         return self.saldo + mais
    def sacar(self):
        return self.saldo - menos
    
mais = 9000
menos = 4500
ver = ContaBancaria()
ver.depositar()
ver.sacar()
print(f"O {ver.titular} depositou R$:{ver.depositar()}, e você sacou R${ver.sacar()}")

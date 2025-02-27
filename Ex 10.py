print("ex 10")
import random
input("digite um nome:")

numero_random = random.randint(1000, 9999)
acesso = int  (input("digite a senha:"))

if acesso != numero_random:
    print("Acesso Negado")
else:
    print("Acesso concedido")
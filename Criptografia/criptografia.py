import cryptography
import os
from cryptography.fernet import Fernet

frase = input('Digite uma frase ')

def criptografar():
    
    casca = Fernet.generate_key()
    fernet = Fernet(casca)
    

    frase_criptografado = fernet.encrypt(frase.encode())
    print(f'Palavra criptografada: {frase_criptografado}')

    frase_descriptografado = fernet.decrypt(frase_criptografado).decode()
    print(f"Texto descriptografado: {frase_descriptografado}")
  

criptografar()

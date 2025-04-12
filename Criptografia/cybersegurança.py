import cryptography
import os
from cryptography.fernet import Fernet
import getpass

ciências = Fernet.generate_key()
fernet = Fernet(ciências)

def cybersegurança():
    senha = input('digite a senha ')
    senha = 'ciêcias'

    with open('Pasta_segreda', 'w',encoding='utf-8') as arquivo:
        arquivo.write('Você é um otário')


    if senha == 'ciências':
          with open ('Pasta_segreda', 'r',encoding='utf-8') as arquivo:
            Pasta = arquivo.read()
            pasta_original = fernet.decrypt('Pasta_segreda').decode("utf-8")
    else:
        Pasta_criptografar = fernet.encrypt('Pasta_segreda'.encode())
        with open ('Pasta_segreda', 'wb',) as arquivo:
            arquivo.write(Pasta_criptografar)

cybersegurança()
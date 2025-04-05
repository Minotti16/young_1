from cryptography.fernet import Fernet

# Gerar uma chave (geração de chave somente uma vez)
chave = Fernet.generate_key()
fernet = Fernet(chave)

# Texto que será criptografado
texto = "Mensagem secreta"

# Criptografando o texto
texto_criptografado = fernet.encrypt(texto.encode())
print(f"Texto criptografado: {texto_criptografado}")

# Descriptografando o texto
texto_descriptografado = fernet.decrypt(texto_criptografado).decode()
print(f"Texto descriptografado: {texto_descriptografado}")

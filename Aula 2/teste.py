from cryptography.fernet import Fernet

# 1. Gere uma chave e salve-a (faça isso só uma vez e guarde a chave com segurança)
key = Fernet.generate_key()
with open("chave.key", "wb") as chave_arquivo:
    chave_arquivo.write(key)

# 2. Carregue a chave
with open("chave.key", "rb") as chave_arquivo:
    key = chave_arquivo.read()

fernet = Fernet(key)

# 3. Leia o conteúdo do arquivo original
with open("arquivo.txt", "rb") as file:
    dados = file.read()

# 4. Criptografe os dados
dados_criptografados = fernet.encrypt(dados)

# 5. Salve os dados criptografados (pode sobrescrever o original ou salvar em outro arquivo)
with open("arquivo_criptografado.txt", "wb") as file:
    file.write(dados_criptografados)

print("Arquivo criptografado com sucesso!")

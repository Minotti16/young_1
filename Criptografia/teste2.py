def criptografar(mensagem, chave):
    resultado = ''
    for char in mensagem:
        if char.isalpha():
            deslocamento = chave % 26  # Garante que a chave fique dentro dos limites do alfabeto
            novo_char = chr(((ord(char.lower()) - 97 + deslocamento) % 26) + 97)
            if char.isupper():
                resultado += novo_char.upper()
            else:
                resultado += novo_char
        else:
            resultado += char  # Mantém caracteres não alfabéticos inalterados
    return resultado

def descriptografar(mensagem, chave):
    return criptografar(mensagem, -chave)

# Exemplo de uso
mensagem_original = "Exemplo de mensagem secreta!"
chave = 3

mensagem_criptografada = criptografar(mensagem_original, chave)
print("Mensagem criptografada:", mensagem_criptografada)

mensagem_descriptografada = descriptografar(mensagem_criptografada, chave)
print("Mensagem descriptografada:", mensagem_descriptografada)





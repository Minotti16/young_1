def saudacoes(nome):
    import random
    frases = ['Bom dia! Meu nome é' + nome + '. Como vai você?', 'Olá!', 'oi, tudo']
    print(frases[random.randint(0,2)])


def receberTexto():
    texto = 'Cliente:'+ input('Cliente:')
    palavraProibido = ['caralho']
    for p in palavraProibido:
        if p in texto:
            print('Não vem não! Me respeite!')
            return(receberTexto())
        return texto
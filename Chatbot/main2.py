def saudacoes(nome):
    import random
    frases = ['Bom dia! Meu nome é ' + nome + '. Como vai você?', 'Olá!', 'oi, tudo?']
    print(frases[random.randint(0,2)])

def receberTexto():
    texto = 'Cliente: ' + input('Cliente: ')
    palavraProibido = ['bocó']
    for p in palavraProibido:
        if p in texto:
            print('Não vem não! Me respeite')
            return(receberTexto())
        return texto
    
def buscarResposta(nome, texto):
    with open('chat.txt','a+') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != '':
                if texto.replace('Cliente: ','') == 'Tchau':
                    print(nome + ': volte sempre!')
                    return 'fim'
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if 'Chatbot: ' in proximalinha:
                        return proximalinha
            else:
                print('Me desculpe não sei o que falar')
                conhecimento.write('\n' + texto)
                resposta_user = input('O que esperava?\n')
                conhecimento.write('\n' + 'Chatbot: ' + resposta_user)
                return 'Hum....'

def exibeResposta(resposta, nome):
    print(resposta.replace('Chatbot', nome))
    if resposta == 'fim':
        return 'fim'
    return 'continua'
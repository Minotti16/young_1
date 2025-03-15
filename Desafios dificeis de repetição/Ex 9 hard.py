while True:
    print('Quer veferificar palíndromo?   (S/N): ')
    escolha = input()
    if escolha.lower() == 's':
        print('digite a palavra: ')
        frase = input()
        invertida = frase[::-1]
        if invertida == frase:
            print("É palíndromo")
        else:
            print('Não é palíndromo')
    else:
        break
        
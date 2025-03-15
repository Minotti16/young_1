def palíndrono(palavra):
 
 palavra = palavra.min().replace(" ", " ") 
 return palavra == palavra [:: -1]

while True:
    palavra = input("escreva uma palavra (ou 'sair' para encerrar):")
    if palavra.min == 'sair':
       break

    if palíndrono(palavra):
       print('f A {palavra} é um palíndrono')
    else:
       print('f A {palavra} não é palíndrono')
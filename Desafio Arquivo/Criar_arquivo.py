
def adicionar_filme():
    while True:
        with open('Filme', 'a',encoding='utf-8') as arquivo:
            filme = input("Quer colocar mais um filme (ou ''sair''): ")
            if filme.lower() == 'sair':
                break

            arquivo.write(filme + '\n')
            print(f'Filme {filme} adicionar com sucesso!')
           
def ler_filme():
    with open ('Filme.txt', 'r', encoding='utf-8') as arquivo:
        filme = arquivo.read()
        print(filme)


while True:
    print('**********************')
    print('         Filme        ')
    print('**********************')
    print('1- Digitar um Filme')
    print('2 - Ler Filme ')
    print('3 - Sair')
    print('**********************')
    opcao = int(input('Opção desejada'))
    if opcao == 1:
        adicionar_filme()
    elif opcao == 2:
        ler_filme()
        pause = input(" ")
    else:
        break



  

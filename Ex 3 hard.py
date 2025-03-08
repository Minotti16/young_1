notas = []
resposta = ''
i = 1

while resposta != 'n':
    nota = float(input(f'Digite nota {i}:  '))

    notas.append(nota)
    resposta = input("Deseja digitar mais uma nota?  (s/n): ")
    i = i+1

total = sum(notas)/ len(notas) 

if total >= 7:
    print(f'Aprovado com nota {total} :')
elif total <= 4:
    print(f"Reprovado com nota {total}")
else:
    print (f'Recuperação com nota{total}')
    

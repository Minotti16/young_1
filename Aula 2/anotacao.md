# AULA 2
## COMANDOS BÁSICOS
- print: comando para mostrar informação no terminal
- input: comando para entrar informação através do terminal

## O QUE É CONDICIONAIS ??
É o "if else"

Condicionais é uma estrutura de programação que 
se uma condição for verdadeira eu faço uma
determinada ação, do contrário se for
falsa faço outra

ex: 
```python
a = 4
b = 2

if a == b:
    print('oi')
else:
    print('tchau')
```

### Condicionais composto
Estrutura com multiplas condições

ex: 
```python
a = 4
b = 2

if a > b:
    print('oi')
elif a < b:
    print('tchau')
else:
    print('saude')
```


# Operadores de Comparação (Relacionais) e Operadores Lógicos em Python

## Operadores de Comparação (Relacionais)

Em Python, utilizamos os **operadores de comparação (ou relacionais)** para comparar valores e verificar se uma condição é verdadeira ou falsa. Os principais são:

1. **`==` (igual a)**  
   - Verifica se dois valores são iguais.  
   - **Exemplo**: `5 == 5` resulta em `True`; `5 == 3` resulta em `False`.

2. **`!=` (diferente de)**  
   - Verifica se dois valores são diferentes.  
   - **Exemplo**: `5 != 3` resulta em `True`; `5 != 5` resulta em `False`.

3. **`>` (maior que)**  
   - Verifica se o valor à esquerda é maior do que o valor à direita.  
   - **Exemplo**: `7 > 3` resulta em `True`; `3 > 7` resulta em `False`.

4. **`<` (menor que)**  
   - Verifica se o valor à esquerda é menor do que o valor à direita.  
   - **Exemplo**: `3 < 7` resulta em `True`; `7 < 3` resulta em `False`.

5. **`>=` (maior ou igual a)**  
   - Verifica se o valor à esquerda é maior ou igual ao valor à direita.  
   - **Exemplo**: `5 >= 5` resulta em `True`; `4 >= 5` resulta em `False`.

6. **`<=` (menor ou igual a)**  
   - Verifica se o valor à esquerda é menor ou igual ao valor à direita.  
   - **Exemplo**: `4 <= 5` resulta em `True`; `6 <= 5` resulta em `False`.

---

## Operadores Lógicos

Os **operadores lógicos** são usados para combinar expressões booleanas ou inverter o valor lógico de uma expressão. Em Python, temos:

1. **`and` (E)**  
   - Retorna `True` se **ambas** as expressões forem verdadeiras. Caso contrário, retorna `False`.  
   - **Exemplo**:  
     - `True and True` → `True`  
     - `True and False` → `False`  
     - `(2 > 1) and (3 > 2)` → `True`

2. **`or` (OU)**  
   - Retorna `True` se **pelo menos uma** das expressões for verdadeira. Se ambas forem falsas, retorna `False`.  
   - **Exemplo**:  
     - `True or False` → `True`  
     - `False or False` → `False`  
     - `(2 > 1) or (2 > 3)` → `True`

3. **`not` (NÃO)**  
   - Inverte o valor lógico de uma expressão.  
   - **Exemplo**:  
     - `not True` → `False`  
     - `not False` → `True`  
     - `not (3 > 2)` → `False`  

---

## Exemplos de Uso Combinado

Podemos combinar operadores de comparação e lógicos em **expressões mais complexas**. Por exemplo:

```python
idade = 20

# Verificando se a idade está entre 18 e 25
if idade >= 18 and idade <= 25:
    print("Você tem entre 18 e 25 anos.")
else:
    print("Você não está na faixa de 18 a 25 anos.")
```

# Lista de Exercícios de Python sobre Condicionais

## 1. Par ou Ímpar
**Enunciado**:  
- Peça ao usuário que digite um número inteiro.  
- Verifique se o número é par ou ímpar.  
- Mostre uma mensagem indicando o resultado.

---

## 2. Positivo, Negativo ou Zero
**Enunciado**:  
- Receba um número inteiro do usuário.  
- Verifique se esse número é positivo, negativo ou zero.  
- Exiba a mensagem correspondente.

---

## 3. Comparação de Dois Números
**Enunciado**:  
- Peça para o usuário inserir dois números.  
- Compare os números e mostre qual deles é maior, ou se são iguais.

---

## 4. Nota Aprovado/Reprovado
**Enunciado**:  
- Peça ao usuário que digite uma nota (0 a 10).  
- Se a nota for maior ou igual a 6, exiba "Aprovado". Caso contrário, exiba "Reprovado".  
- Caso a nota esteja fora do intervalo [0, 10], mostre uma mensagem de erro.

---

## 5. Dia da Semana
**Enunciado**:  
- Solicite um número de 1 a 7.  
- Cada número representa um dia da semana (1 = segunda-feira, 2 = terça-feira, etc.).  
- Exiba o nome do dia correspondente ou mostre "Dia inválido" se o número não estiver entre 1 e 7.

---

## 6. Maior de Três Números
**Enunciado**:  
- Leia três números do usuário.  
- Verifique qual deles é o maior e exiba na tela.  
- Se houver empate, exiba qual(is) número(s) está(ão) empatado(s) e que são os maiores.

---

## 7. Jogo de Adivinhação Simples
**Enunciado**:  
- Defina um número secreto em seu código, por exemplo, 7.  
- Peça ao usuário que tente adivinhar qual é o número secreto.  
- Se o palpite for maior que o número secreto, mostre "Muito alto!". Se for menor, "Muito baixo!". Se for igual, "Acertou!".

---

## 8. Verificação de Idade
**Enunciado**:  
- Receba do usuário sua idade.  
- Se a idade for menor que 18, exiba "Menor de idade".  
- Se a idade for entre 18 e 64, exiba "Adulto".  
- Se a idade for 65 ou mais, exiba "Idoso".

---

## 9. Classificação de Intervalos
**Enunciado**:  
- Peça ao usuário que digite um número.  
- Verifique e mostre em qual dos intervalos o número se encaixa:  
  - [0, 25]  
  - (25, 50]  
  - (50, 75]  
  - (75, 100]  
- Caso o número esteja fora de 0 a 100, exiba "Fora de intervalo".

---

## 10. Verificador de Login Simplificado
**Enunciado**:  
- Peça ao usuário que digite um nome de usuário e uma senha.  
- Compare com valores pré-definidos no código (por exemplo, usuário = "admin" e senha = "1234").  
- Se estiver correto, exiba "Acesso concedido". Caso contrário, "Acesso negado".

---

## 11. Desconto Progressivo
**Enunciado**:  
- Receba do usuário o valor de uma compra.  
- Se o valor for até R\$100, não conceda desconto.  
- Se estiver entre R\$101 e R\$200, conceda 10% de desconto.  
- Se for acima de R\$200, conceda 20% de desconto.  
- Mostre o valor final após o desconto.

---

## 12. Conversor de Notas para Conceitos
**Enunciado**:  
- Peça ao usuário que digite uma nota (0 a 10).  
- Converta a nota em conceito, seguindo alguma regra, por exemplo:  
  - 0 a 4: Conceito D  
  - 5 a 6: Conceito C  
  - 7 a 8: Conceito B  
  - 9 a 10: Conceito A  
- Exiba o conceito correspondente ou indique que a nota é inválida se não estiver no intervalo.

---

## 13. Identificação de Vogais e Consoantes
**Enunciado**:  
- Receba uma letra do usuário.  
- Verifique se a letra é uma vogal (a, e, i, o, u) ou consoante.  
- Considere apenas letras minúsculas para simplificar, ou trate as duas possibilidades (maiúsculas e minúsculas).

---

## 14. Verificar Divisibilidade
**Enunciado**:  
- Solicite um número inteiro.  
- Verifique se ele é divisível por 2, 3 e 5, mostrando mensagens diferentes para cada caso:  
  - "É divisível por 2" ou "Não é divisível por 2".  
  - "É divisível por 3" ou "Não é divisível por 3".  
  - "É divisível por 5" ou "Não é divisível por 5".

---

## 15. Triângulo Válido
**Enunciado**:  
- Receba três valores (comprimentos de lados).  
- Verifique se podem formar um triângulo (cada lado deve ser menor que a soma dos outros dois).  
- Se formarem um triângulo, verifique se é equilátero, isósceles ou escaleno.  
- Exiba o resultado.

---

## 16. Validação de Horário
**Enunciado**:  
- Peça ao usuário que informe um horário no formato "HH:MM".  
- Verifique se esse horário é válido (por exemplo, hora de 0 a 23 e minuto de 0 a 59).  
- Exiba "Horário válido" ou "Horário inválido".

---

## 17. Verificação de Aprovação em Duas Provas
**Enunciado**:  
- Solicite as notas de duas provas (0 a 10).  
- Verifique se o aluno foi aprovado:  
  - Se a média das notas for >= 6, "Aprovado".  
  - Senão, "Reprovado".  
- Se qualquer das notas estiver fora do intervalo, exiba "Nota inválida".

---

## 18. Sistema de Pagamento
**Enunciado**:  
- Peça o valor de uma compra e a forma de pagamento (1 = à vista, 2 = parcelado).  
- Se for à vista, conceda 5% de desconto.  
- Se for parcelado em 2x, o preço permanece igual.  
- Se for parcelado em mais vezes, acrescente 10% de juros.  
- Exiba o valor final.

---

## 19. Verificar se a Letra é Maiúscula ou Minúscula
**Enunciado**:  
- Peça ao usuário que informe uma letra.  
- Verifique se é maiúscula, minúscula ou se o caractere não é uma letra do alfabeto.  
- Exiba a mensagem correspondente.

---

## 20. Menu Interativo
**Enunciado**:  
- Mostre um menu com 3 opções:  
  1. Fazer algo (ex: "Exibir mensagem")  
  2. Fazer outra coisa (ex: "Calcular soma")  
  3. Sair  
- Peça ao usuário que selecione uma opção (1, 2 ou 3).  
- Use if/elif/else para executar a ação desejada.  
- Se for uma opção inválida, exiba uma mensagem de erro.  
- Continue pedindo a opção até o usuário escolher sair.


# Exercícios de Estrutura Condicional e Repetição (Nível Difícil)

## 1. Desafio do Fatorial Inverso
Escreva um programa que calcule o fatorial de um número inserido pelo usuário. O programa deve perguntar se o usuário quer calcular o fatorial de outro número. Se a resposta for sim, o programa deve calcular o fatorial do novo número. Se a resposta for não, o programa deve encerrar.

## 2. Jogo de Adivinhação
Crie um jogo de adivinhação onde o computador escolhe um número aleatório entre 1 e 100. O usuário deve tentar adivinhar o número, e o programa deve informar se o chute foi maior ou menor que o número sorteado. O jogo deve repetir até o usuário acertar.

## 3. Calculadora de Média com Repetição
Solicite ao usuário várias notas de alunos. O programa deve calcular a média de cada aluno e determinar se ele foi aprovado (média >= 7), reprovado (média < 4) ou de recuperação (média entre 4 e 7). O programa deve perguntar se o usuário deseja continuar inserindo notas ou se quer finalizar.

## 4. Contagem Regressiva para o Ano Novo
Implemente uma contagem regressiva para o Ano Novo. O programa deve exibir a quantidade de segundos restantes e continuar até atingir zero. Ao atingir zero, o programa exibe "Feliz Ano Novo!" e pergunta ao usuário se deseja reiniciar a contagem.

## 5. Sequência de Fibonacci até um Número Limite
Peça ao usuário um número limite. O programa deve gerar a sequência de Fibonacci até atingir ou ultrapassar esse número e, a cada número gerado, deve perguntar se o usuário deseja continuar ou encerrar o programa.

Verificação de Palíndromo
Peça ao usuário para inserir uma palavra. O programa deve verificar se a palavra é um palíndromo (se pode ser lida da mesma forma de trás para frente). O programa deve repetir até o usuário digitar "sair".

Contagem de Caracteres
Solicite ao usuário para inserir uma frase. O programa deve contar quantas vezes um determinado caractere (informado pelo usuário) aparece na frase. Após a contagem, o programa deve perguntar se o usuário deseja contar outro caractere ou encerrar o programa.
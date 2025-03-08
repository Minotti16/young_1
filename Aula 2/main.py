

def calcular_fatorial(numero):
  """Calcula o fatorial de um número."""
  if numero < 0:
    return "Fatorial não definido para números negativos"
  elif numero == 0:
    return 1
  else:
    fatorial = 1
    for i in range(1, numero + 1):
      fatorial *= i
    return fatorial

while True:
  try:
    numero = int(input("Digite um número inteiro não negativo: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
  except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")

  continuar = input("Deseja calcular o fatorial de outro número? (sim/não): ").lower()
  if continuar != 'sim':
    break

print("Programa encerrado.")
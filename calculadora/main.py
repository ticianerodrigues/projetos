# Criar uma calculador
# O Usuário deve escolher uma das operações
# O Usuário deve inserir 2 valores
# O Programa exibe o resultado de acordo com a operação escolida e os valores diferentes

operacao = ""

while operacao != "sair":

  numero1 = int(input("Digite o primeiro valor: "))
  operacao = input("Digite o operador: ")
  numero2 = int(input("Digite o segundo valor: "))

  if operacao == "+":
    resultado = numero1 + numero2

  elif operacao == "-":
    resultado = numero1 - numero2

  elif operacao == "*":
    resultado = numero1 * numero2

  elif operacao == "/":
    resultado = numero1 / numero2

  else:
    resultado = "Operação inválida"
  
  print(str(numero1) + operacao + str(numero2) + "=" + str(resultado))

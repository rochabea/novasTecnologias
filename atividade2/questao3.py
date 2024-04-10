#questao 3
#Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
expressao_parentese = input("Digite uma expressão com parênteses para ser validada: ")
x = 0
pilha = []

while x < len(expressao_parentese):
  if expressao_parentese[x] == "(":
    pilha.append("(")
  if expressao_parentese[x] == ")":
    if len(pilha) > 0:
      topo = pilha.pop(-1)
    else:
      pilha.append(")")
      break
  x = x + 1
if len(pilha) == 0:
  print("Fechado da forma correta")
else:
  print("Fechado da forma incorreta")
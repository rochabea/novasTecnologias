"""
9. Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
escolhida. Repita até que a opção saída seja escolhida.
"""
a = int(input('Insira um valor para a variavel a: '))
b = int(input('Insira um valor para a variavel b: '))

print('Escolha a opção da operação desejada: \nSoma: +\nSubtração: -\nMultiplicação: *\nDivisão: /\nPara sair digite: "break"')
variavel = input('Digite a opção desejada: ')
match(variavel):
  case '+':
    resultado = a + b
  case '-':
    resultado = a -b
  case '*':
    resultado = a * b
  case '/':
    resultado = a/b
  case _:
    print('Operação fora do menu')

print(f'O resultado da operação {variavel} foi {resultado}')
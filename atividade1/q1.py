"""
1. Escreva um aplicativo que solicita ao usuário inserir dois inteiros, obtém do
usuário esses números e imprime sua soma, produto, diferença e divisão. 
"""

valor1 = int(input('Insira um valor: '))
valor2 = int(input('Insira um segundo valor: '))

soma = valor1 + valor2
produto = valor1 * valor2
diferenca = valor1 - valor2
divisao = valor1//valor2

print(f'O valor da soma de {valor1} + {valor2} é igual a {soma}')
print(f'O valor do produto de {valor1} * {valor2} é igual a {produto}')
print(f'O valor da diferença de {valor1} - {valor2} é igual a {diferenca}')
print(f'O valor da divisão de {valor1} / {valor2} é igual a {divisao}')
"""
Escreva um programa que gere um dicionário, em que cada chave seja um
caractere, e seu valor seja o número desse caractere encontrado em uma
frase lida.
"""

palavra = input("Digite uma palavra: ")
p = {}
for letra in palavra:
    p[letra] = p.get(letra, 0) + 1
print(p)
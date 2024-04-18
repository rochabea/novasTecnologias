"""
Escreva um programa que compare duas listas. Considere a primeira lista
como a versão inicial e a segunda como a versão após alterações.
Utilizando operações com conjuntos, seu programa deverá imprimir a lista
de modificações entre essas duas versões, listando:
 ◦ os elementos que não mudaram
 ◦ os novos elementos
 ◦ os elementos que foram removidos
"""
original = {'pera', 'uva', 'maça'}
lista = {'pera', 'uva', 'maça'}
print(f"A lista inicial é: {lista}")
#lista.add('manga')
elemento = input("digite o elemento para ser incluido na lista: ")
lista.add(elemento)
print(f"A lista apos a adição de um elemento: {lista}")
remover = input("Deseja remover algum item? se Sim, digite SIM: ")
if remover.upper() == 'SIM':
    item = input("Digite o item a ser removido: ")
    lista.remove(item)
else:
    print(lista)

s1 = set(lista)
s2 = set(original)

print("--------------------------------------------------------")
print("Elementos que não mudaram", original)
print("Novos elementos: ", lista - original)
print("Elemento removido: ", item)


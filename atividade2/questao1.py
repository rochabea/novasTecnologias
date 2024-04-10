#questão 1
#lista
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
print(lista)

#a) maior numero da lista
maior = max(lista)
print(f"O maior número da lista é {maior}")

#b) imprimir o menor elemento da lista
menor = min(lista)
print(f"O menor número da lista é {menor}")

#c) imprimir os número pares
pares = []
for valor in lista:
  if valor % 2 == 0:
    pares.append(valor)
print(f"Os números pares dessa lista são {pares}")

#d) imprima o número de ocorrências do primeiro elemento da lista;
quantidade = lista.count(12)
print(f"A quantidade de vezes que o número {lista[0]} aparece é ", quantidade)

#e) imprima a média dos elementos;
media = sum(lista)/len(lista)
print(f"A média da soma dos números da lista é igual a {media}")

#f) imprima a soma dos elementos de valor negativo
#verificando os numeros negativos e a soma desse numeros
#lista_ordenada = print(sorted(lista))
#print((-52) + (-17) + (-2))

#soma dos numeros negativos usando for 
soma_negativos = 0
for n in lista:
  if n < 0:
    soma_negativos += n
print(f"A soma dos elementos negativos é igual a {soma_negativos}")
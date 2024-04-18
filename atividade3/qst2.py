lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

conjunto_1 = set(lista1)
conjunto_2 = set(lista2)

print("a) Valores comuns às duas listas:", conjunto_1 & conjunto_2)
print("b) Valores que só existem na primeira:", conjunto_1 - conjunto_2)
print("c) Valores que só existem na segunda:", conjunto_2 - conjunto_1)
print("d) Elementos não repetidos nas duas listas:", conjunto_1 ^ conjunto_2)
print("e) Primeira lista, sem os elementos repetidos na segunda:", conjunto_1 - conjunto_2)
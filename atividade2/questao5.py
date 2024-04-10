#questao 5
V = [9,8,7,12,0,13,21]

pares = []
for numero in V:
  if numero % 2 == 0:
    pares.append(numero)
print(f"A lista com os números pares é: {pares}")

impares = []
for numero in V:
  if numero % 2 != 0:
    impares.append(numero)
print(f"A lista com os números ímpares é: {impares}")
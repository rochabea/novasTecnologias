"""
14. Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu
fatorial.

"""
numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(f'O resultado de {numero} fatorial é igual a {resultado}')
"""
13. O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n
fatorial”) e é definido como segue:
n! = n · (n – 1) · (n – 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n! =
1 (para n = 0)
Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120.

"""
numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)
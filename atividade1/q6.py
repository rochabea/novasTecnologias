"""
Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do
segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.
"""
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

#calculo da variavel delta de acordo com a formula
delta = (b ** 2) - 4 * a * c

print("\n**************************\n")

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f"x1': {x1}\n x2'': {x2}")
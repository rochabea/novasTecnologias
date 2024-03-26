"""
8. Escreva um programa que converta uma temperatura digitada em "C” em “F”.
"""
celcius = float(input('digite a temperatura em celcius: '))

fahrenheit = ((9/5)* celcius) + 32

print(f'A temperatura {celcius} em celcius é igual a {fahrenheit} em fahrenheit')
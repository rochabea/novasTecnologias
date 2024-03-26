"""
7. Escreva um programa que leia a quantidade em segundos e imprima o
resultado em dias, horas, minutos e segundos.
"""
segundos = int(input('Digite os segundos: '))

minutos = segundos/60
hora = minutos/60
dia = hora/24

print(f'Dias: {dia}, horas: {hora}, minutos, {minutos} e segundos: {segundos}')
"""
10. Escreva um programa que leia um número e verifique se é ou não um número primo.
"""
num = int(input('Digite um número: '))

count = 0
i = 1

while i<=num:
    if num%i==0:
        count = count + 1
    i = i + 1

if count == 2:
    print(f'O número {num} é primo')
else:
    print(f'O numero {num} não é primo')
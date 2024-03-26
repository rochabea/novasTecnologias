"""
16. A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros
termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos
dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da
série de Fibonacci.
"""
n = int(input("Qual termo deseja encontrar da sequencia de fibonacci: "))
ultimo = 1
penultimo = 1
count = 0

if (n == 1) or (n == 2):
  print("1")
else:
  for count in range(2, n):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
  print(f'O valor da sequencia {n} é {termo}')
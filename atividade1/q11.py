"""
Coloque um número bem grande para ser executado no exemplo anterior,
você perceberá que demora bastante, consegue pensar num solução na
lógica para reduzir o tempo de procura?

"""
num = int(input('Digite um numero: '))
# Se o numero dado for maior do que 1:
if num > 1:
    # Itera de 2 até n // 2
    for i in range(2, (num//2)+1):
        # Se o numero for divisivel por qualquer outro numero entre 2 e n / 2, ele nao e primo
        if (num % i) == 0:
            print(num, "não é um numero primo")
            break
    else:
        print(num, "é um numero primo")
else:
    print(num, "não é um numero primo")
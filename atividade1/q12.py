def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

def primos_anteriores(n):
    print(f'Números primos até {n} :')
    for num in range(2, n + 1):
        if isPrime(num):
            print(num)


n = int(input('Digite um número: '))
primos_anteriores(n)
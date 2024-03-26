"""
17. Numa certa agência bancária, as contas são identificadas por números de
até seis dígitos seguidos de um dígito verificador, calculado conforme
exemplificado a seguir. Dado um número de conta n, exiba o número de
conta completo correspondente. Seja n = 7314 o número da conta.
Adicionamos os dígitos de n e obtemos a soma s = 4+1+3+7 = 15;
Calculamos o resto da divisão de s por 10 e obtemos o dígito d = 5. Número
de conta completo: 007314−5
"""
conta = int(input("Informe o número da conta sem o Digito Verificador: "))

while not (1 <= conta <= 999999):
    print("Conta Inválida. Reinforme o número da conta sem o Digito Verificador: ")
    conta = int(input())

soma = 0
aux = conta

while aux > 0:
    alg = aux % 10
    soma += alg
    aux //= 10

dig = soma % 10

print(f"Número da conta completa: {conta:06}-{dig}")
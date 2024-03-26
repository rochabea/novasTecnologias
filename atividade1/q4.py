"""
4. Escreva um aplicativo que insere um número consistindo em cinco dígitos
do usuário, separa o número em seus dígitos individuais e imprime os
dígitos separados uns dos outros por três espaços cada. Por exemplo, se o
usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.
"""
num = int(input("Digite um numero com 5 digitos"))
print(num)
msg = ""

msg = msg + " " + str(num//10000)

num=num%10000
msg = msg + " " + str(num//1000)

num=num%1000
msg = msg + " " + str(num//100)

num=num%100
msg = msg + " " + str(num//10)

num=num%10
msg = msg + " " + str(num//1)

print(msg)
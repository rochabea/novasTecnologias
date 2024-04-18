"""
Crie uma lista chamada sandwich_orders e a preencha com os nomes de
vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches . Percorra a lista de pedidos de sanduíches com um laço
e mostre uma mensagem para cada pedido, por exemplo, Preparei seu
sanduíche de atum. À medida que cada sanduíche for preparado, transfirao para a lista de sanduíches prontos. Depois que todos os sanduíches
estiverem prontos, mostre uma mensagem que liste cada sanduíche
preparado.
"""

sandwich_orders = ['sanduíche de atum', 'sanduíche de frango', 'sanduíche de carne', 'sanduíche vegetariano']
finished_sandwiches = []

#preparando sanduiches
for sanduiche in sandwich_orders:
    print(f"Preparando seu {sanduiche}")
    finished_sandwiches.append(sanduiche)

#mostrando os sanduiches preparados
print("\nSanduiches prontos:")
for sanduiche in finished_sandwiches:
    print(f"{sanduiche} pronto")
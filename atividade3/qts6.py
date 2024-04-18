"""
Crie vários dicionários, em que o nome de cada dicionário seja o nome de
um animal de estimação. Em cada dicionário, inclua o tipo do animal e o
nome do dono. Armazene esses dicionários em uma lista chamada pets .
Em seguida, percorra sua lista com um laço e, à medida que fizer isso,
apresente tudo que você sabe sobre cada animal de estimação.
"""
dict1 = {'raça do animal': 'pug', 'nome do dono': 'francisca'}
dict2 = {'raça do animal': 'buldogue', 'nome do dono': 'luis'}
dict3 = {'raça do animal': 'golden', 'nome do dono': 'felipe'}
dict4 = {'raça do animal': 'beagle', 'nome do dono': 'antonie'}

pets = [dict1, dict2, dict3, dict4]

for animais in pets:
    print("Informações do cachorro: ")
    for key, value in animais.items():
        print(f"{key.capitalize()}: {value.capitalize()}")


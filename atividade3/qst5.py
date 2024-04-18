beatriz = {'first_name':'beatriz', 'last_name':'araujo', 'age': 19, 'city':'vp'}
print("Dict da beatriz: ", beatriz)
print("\n")
elisangela = {'first_name':'elisangela', 'last_name':'rocha', 'age': 48, 'city':'taguatinga'}
print("Dict da elisangela: ",elisangela)
print("\n")
francisco = {'first_name':'chico', 'last_name':'gonzaga', 'age':52 , 'city':'piaui'}
print("Dict do francisco: ",francisco)
print("\n")
people = [beatriz, elisangela, francisco]
print("dict people: ", people)
print("\n")
for item in people:
    print("\n")
    print("Informações sobre cada pessoa: ")
    for key, value in item.items():
        print(f"{key.capitalize()}: {value}")
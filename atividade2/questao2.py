#questao 2
#parametros
#palavra a ser descoberta
palavra = "python"
#letras que o usuários chuttar/tentar
letras_usuarios = []
#quantidade de chances que o usuário vai ter
chances = 4
#incialmente vai ser falsa -> usuario tera que mudar essa condição
ganhou = False

while True:
  for letra in palavra:
    if letra.lower() in letras_usuarios:
      print(letra, end=" ")
    else:
      print("_", end=" ")
  print(f"\nVocê tema {chances} chances")
  tentativa = input("Escolha uma letra para adivinhar: ")
  letras_usuarios.append(tentativa.lower())
  if tentativa.lower() not in palavra.lower():
    chances -= 1

  ganhou = True
  for letra in palavra:
    if letra.lower()not in letras_usuarios:
      ganhou = False

  if chances == 0 or ganhou:
    break


if ganhou:
  print(f"Parabens, voce ganhou. A palavra era {palavra}")
else:
  print(f"Voce perdeu. A palavra era {palavra}")
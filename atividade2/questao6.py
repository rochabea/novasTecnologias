#questao 6
lugares_vagos = [10, 2, 1, 3, 0]

sala = int(input('Qual a sala você deseja acessar?'))
match sala:
  case 1:
    lugares_solicitados = int(input("Quantos lugares você deseja?"))
    disponivel = lugares_vagos[0]
    if disponivel >= lugares_solicitados:
      print("Será disponibilizado seu(s) ingresso(s)")
    else:
      print("Não tem lugares disponíveis para essa quantidade de ingresso")
    
    restante = int(lugares_vagos[0]) - lugares_solicitados
    if restante > -1:
      print(f"Ainda restam {restante} ingresso(s) para está sala de cinema")
  
  case 2:
    lugares_solicitados = int(input("Quantos lugares você deseja?"))
    disponivel = lugares_vagos[1]
    if disponivel >= lugares_solicitados:
      print("Será disponibilizado seu(s) ingresso(s)")
    else:
      print("Não tem lugares disponíveis para essa quantidade de ingresso")
    
    restante = int(lugares_vagos[1]) - lugares_solicitados
    if restante > -1:
      print(f"Ainda restam {restante} ingresso(s) para está sala de cinema")
  
  case 3:
    lugares_solicitados = int(input("Quantos lugares você deseja?"))
    disponivel = lugares_vagos[2]
    if disponivel >= lugares_solicitados:
      print("Será disponibilizado seu(s) ingresso(s)")
    else:
      print("Não tem lugares disponíveis para essa quantidade de ingresso")
    
    restante = int(lugares_vagos[2]) - lugares_solicitados
    if restante > -1:
      print(f"Ainda restam {restante} ingresso(s) para está sala de cinema")
  
  case 4:
    lugares_solicitados = int(input("Quantos lugares você deseja?"))
    disponivel = lugares_vagos[3]
    if disponivel >= lugares_solicitados:
      print("Será disponibilizado seu(s) ingresso(s)")
    else:
      print("Não tem lugares disponíveis para essa quantidade de ingresso")
    
    restante = int(lugares_vagos[3]) - lugares_solicitados
    if restante > -1:
      print(f"Ainda restam {restante} ingresso(s) para está sala de cinema")
  
  case 5:
    lugares_solicitados = int(input("Quantos lugares você deseja?"))
    disponivel = lugares_vagos[4]
    if disponivel >= lugares_solicitados:
      print("Será disponibilizado seu(s) ingresso(s)")
    else:
      print("Não tem lugares disponíveis para essa quantidade de ingresso")
    
    restante = int(lugares_vagos[4]) - lugares_solicitados
    if restante > -1:
      print(f"Ainda restam {restante} ingresso(s) para está sala de cinema")
import csv
import pandas as pd

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    agenda.append({'Nome': nome, 'Telefone': telefone, 'Email': email})
    print("Contato adicionado com sucesso!")

def listar_contatos(agenda):
    print("Lista de Contatos:")
    for contato in agenda:
        print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")

def pesquisar_contato(agenda):
    termo = input("Digite o nome ou parte do nome do contato: ")
    encontrados = [contato for contato in agenda if termo.lower() in contato['Nome'].lower()]
    if encontrados:
        print("Contatos encontrados:")
        for contato in encontrados:
            print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")
    else:
        print("Nenhum contato encontrado com esse nome.")

def salvar_agenda_csv(agenda):
    with open('agenda.csv', 'w', newline='') as arquivo_csv:
        campos = ['Nome', 'Telefone', 'Email']
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for contato in agenda:
            escritor_csv.writerow(contato)
    print("Agenda salva com sucesso!")

def importar_contatos_csv(agenda):
    arquivo = input("Digite o nome do arquivo CSV a ser importado (ex: contatos.csv): ")
    try:
        df = pd.read_csv(arquivo)
        for _, row in df.iterrows():
            agenda.append({'Nome': row['Nome'], 'Telefone': row['Telefone'], 'Email': row['Email']})
        print("Contatos importados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def menu():
    print("\n*** Agenda ***")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Pesquisar Contato")
    print("4. Salvar Agenda")
    print("5. Importar Contatos de CSV")
    print("6. Sair")

def main():
    agenda = []
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato(agenda)
        elif opcao == '2':
            listar_contatos(agenda)
        elif opcao == '3':
            pesquisar_contato(agenda)
        elif opcao == '4':
            salvar_agenda_csv(agenda)
        elif opcao == '5':
            importar_contatos_csv(agenda)
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

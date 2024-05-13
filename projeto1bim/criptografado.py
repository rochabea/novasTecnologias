import bcrypt

class InformaSenha:
    listaSenhas = []

    def forneceSenha(self):
        senha = input("Insira a senha para ser criptografada: ")
        return senha

    def criptografandoSenha(self, senha):
        tratandoSenha = senha.encode('utf-8')
        salt = bcrypt.gensalt()  # Gerando um salt aleatório
        hash_senha = bcrypt.hashpw(tratandoSenha, salt)  # Criando o hash bcrypt da senha
        return hash_senha

class VisualizaSenha:
    def visualizaSenha(self, hash_senha):
        resposta = input("Deseja ver a senha criptografada? Informe SIM caso queira, e NAO caso não deseje: ")
        if resposta.upper() == 'SIM':
            print(f"Senha criptografada: {hash_senha}")

class AtualizaSenha:
    def atualizarSenha(self, senha_atual, visualizador):
        inf = input("Deseja trocar de senha? Digite 'SIM' caso queira e 'NAO' caso não queira trocar de senha: ")
        if inf.upper() == 'SIM':
            novaSenha = input("Digite a nova senha: ")
            #InformaSenha.listaSenhas.append(f"{senha} | {novaSenha}")  # Adicionando nova senha à lista de senhas
            print("Senha atualizada com sucesso!")
            hash_nova_senha = senha_atual.criptografandoSenha(novaSenha)
            todas_senhas = input("Deseja visualizar todas as senhas já inseridas? Digite 'SIM' caso queira visualizar e 'NAO' caso não queira visualizar as senhas: ")
            if todas_senhas.upper() == 'SIM':
              InformaSenha.listaSenhas.append(f"{senha} | {novaSenha}")  # Visualizando a senha atualizada
            else:
              print("Seguiremos...")
        else:
            print("Senha mantida.")

class ArmazenarSenha:
    def armazenada(self):
        print("Senhas armazenadas:", InformaSenha.listaSenhas)

# Instanciando as classes
informaSenha = InformaSenha()
visualizaSenha = VisualizaSenha()
atualizandoSenha = AtualizaSenha()
senhaArmazenada = ArmazenarSenha()

# Obtendo a senha do usuário
senha = informaSenha.forneceSenha()

# Criptografando a senha
hash_senha = informaSenha.criptografandoSenha(senha)

# Visualizando a senha criptografada
visualizaSenha.visualizaSenha(hash_senha)

# Atualizando a senha pelo usuário
atualizandoSenha.atualizarSenha(informaSenha, visualizaSenha)

# Armazenando as senhas fornecidas
senhaArmazenada.armazenada()

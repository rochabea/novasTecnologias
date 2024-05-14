import bcrypt

class InformaSenha:
    listaSenhas = []
    listaSenhaCriptografada = []

    def __init__(self):
        self._senha = None
        self._hash_senha = None

    def forneceSenha(self):
        self._senha = input("Insira a senha para ser criptografada: ")
        return self._senha

    def criptografandoSenha(self, senha):
        tratandoSenha = senha.encode('utf-8')
        salt = bcrypt.gensalt()  # Gerando um salt aleatório
        self._hash_senha = bcrypt.hashpw(tratandoSenha, salt)  # Criando o hash bcrypt da senha
        return self._hash_senha

class VisualizaSenha:
    def __init__(self):
        pass

    def visualizaSenha(self, hash_senha):
        resposta = input("Deseja ver a senha criptografada? Informe SIM caso queira, e NAO caso não deseje: ")
        if resposta.upper() == 'SIM':
            print(f"Senha criptografada: {hash_senha}")

class AtualizaSenha:
    def __init__(self):
        pass

    def atualizarSenha(self, informaSenha):
        inf = input("Deseja trocar de senha? Digite 'SIM' caso queira e 'NAO' caso não queira trocar de senha: ")
        if inf.upper() == 'SIM':
            novaSenha = input("Digite a nova senha: ")
            hash_nova_senha = informaSenha.criptografandoSenha(novaSenha)
            todas_senhas = input("Deseja visualizar todas as senhas já inseridas? Digite 'SIM' caso queira visualizar e 'NAO' caso não queira visualizar as senhas: ")
            if todas_senhas.upper() == 'SIM':
                InformaSenha.listaSenhas.append(f"{informaSenha._senha} | {novaSenha}")  # Adicionando a senha atualizada à lista
                InformaSenha.listaSenhaCriptografada.append(f"{informaSenha._hash_senha} | {hash_nova_senha}")  # Adicionando a senha criptografada atualizada à lista
            else:
                print("Seguiremos...")
            print("Senha atualizada com sucesso!")
        else:
            print("Senha mantida.")

class ArmazenarSenha:
    def armazenada(self):
        print("Senhas armazenadas:", InformaSenha.listaSenhas)

    def armazenadaCriptografada(self):
        print("Senhas criptografadas armazenadas:", InformaSenha.listaSenhaCriptografada)

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
atualizandoSenha.atualizarSenha(informaSenha)

# Armazenando as senhas fornecidas
senhaArmazenada.armazenada()

# Armazenando as senhas criptografadas fornecidas
senhaArmazenada.armazenadaCriptografada()

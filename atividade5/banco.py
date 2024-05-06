class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self._numero_agencia = numero_agencia
        self._tipo_conta = tipo_conta
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        ContaBancaria
    
    def consultar_saldo(self):
        #retorna o saldo atual da conta
        pass

    def saca(self, valor):
        #retira um valor do saldo
        pass

    def deposita(self, valor):
        #adiciona valor no saldo
        pass

    def transfere_para(self):
        #transfere um vaolr do cliente para outro destino
        pass

    def obter_extrato(self):
        #retorna um extrato detalhando das transações realizadas na conta
        pass

    def alterar_titular(self, novo_titular):
        #altera o  nome do titualar da conta
        pass

    def fechar_conta(self):
        #fecha a conta bancária, transferindo o saldo restante para o titular
        pass

class Historico:
    def __init__(self):
        pass

    def imprime(self):
        #imprime as transações realizadas por cada cliente
        pass

class Cliente:
    def __init__(self):
        pass

    def dados_cliente(self):
        #retorna os dados do cliente
        pass

class ContaPoupanca(ContaBancaria):
    def __init__(self):
        return super().__init__()
    
    def calcular_juros_mensal(self):
        #calcula e aplica juros mensais ao saldo da conta poupança
        pass
    
class ContaCorrente(ContaBancaria):
    def __init__(self):
        return super().__init__()
    
    def utilizar_cheque_especial(self, valor):
        #permite que o titular utilize o cheque especial para cobrir um saldo insuficiente
        pass
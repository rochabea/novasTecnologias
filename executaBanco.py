from atividade5.banco import ContaBancaria
from atividade5.banco import Historico
from atividade5.banco import Cliente
from atividade5.banco import ContaPoupanca
from atividade5.banco import ContaCorrente


joao = Cliente("João", "Silva", "11111-1")
maria = Cliente("Maria", "Salgado", "22222-222")
conta_joao = ContaBancaria("123-4","Corrente", 1000.00, 500.00)
conta_maria = ContaBancaria("123-5","Corrente", 7000.00, 4000.00)

conta_joao.obter_extrato()
conta_joao.consultar_saldo()
print(conta_joao._saldo)
conta_joao.saca(500.00)
conta_joao.deposita(5.50)
conta_joao.transfere_para(conta_maria, 2500.00)
conta_joao.fechar_conta()

conta_joao._historico.imprime()


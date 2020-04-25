from BANCO.Conta_Poupanca import Poupanca
from BANCO.Conta_Corrente import Corrente
from sys import exit

while True:
    try:
        print('----------------MENU DE OPÇÕES---------------------')
        print('[1] Para conta Poupanca')
        print('[2] Para conta Corrente')
        print('[0] para sair do programa.')
        print('Qual das opções acima você deseja prosseguir?')
        while True:
            resp = int(input('>>'))
            if 0 <= resp <= 2:
                break
            print('Por favor digite apenas [1] para conta poupança, [2] para conta corrente ou [3] para sair '
                  'do programa.')
        if resp == 0: exit()
        if resp == 1:
            print('Deseja realizar qual opção? [1] Para depositar ou [2] Para sacar')
            while True:
                realizacao = int(input('>>'))
                if 1 <= realizacao <= 2:
                    break
                print('Por favor digite apenas [1] Para depositar ou [2] Para sacar')
            if realizacao == 1:
                agencia = str(input('Digite o numero da agência:'))
                conta = str(input('Digite o numero da conta:'))
                deposito = float(input('Digite o valor que você deseja depositar: R$'))
                cont = Poupanca(agencia, conta, 0)
                cont.depositar(deposito)
            else:
                agencia = str(input('Digite o numero da agência:'))
                conta = str(input('Digite o numero da conta:'))
                saque = float(input('Digite o valor que você deseja depositar: R$'))
                cont = Poupanca(agencia, conta, 0)
                cont.sacar(saque)
        else:
            print('Deseja realizar qual opção? [1] Para depositar e [2] Para sacar')
            while True:
                realizacao = int(input('>>'))
                if 1 <= realizacao <= 2:
                    break
                print('Por favor digite apenas [1] Para depositar ou [2] Para sacar')
            if realizacao == 1:
                agencia = str(input('Digite o numero da agência:'))
                conta = str(input('Digite o numero da conta:'))
                deposito = float(input('Digite o valor que você deseja depositar: R$'))
                cont = Corrente(agencia, conta, 0)
                cont.depositar(deposito)
            else:
                agencia = str(input('Digite o numero da agência:'))
                conta = str(input('Digite o numero da conta:'))
                saque = float(input('Digite o valor que você deseja depositar: R$'))
                cont = Corrente(agencia, conta, 0)
                cont.sacar(saque)
    except(ValueError,TypeError):
        print('Digito invalido....')
    break




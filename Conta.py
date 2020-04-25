from abc import ABC, abstractmethod
#class mae
class Conta(ABC):
    def __init__(self,agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")

        self._saldo = valor
    def depositar(self,valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor digitado tem que ser numerico !!!")

        self._saldo += valor
        self.detalhes()
        print(f'Valor depositado: R$ {valor}')
    def detalhes(self):
        print(f'Agencia : {self.agencia}')
        print(f'Conta : {self.conta}')
        print(f'Saldo : R${self.saldo} ')


    @abstractmethod
    def sacar(self,valor):
        pass




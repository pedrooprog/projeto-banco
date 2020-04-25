from BANCO.Conta  import Conta

class Poupanca(Conta):
    def sacar(self,valor):
        if self.saldo < valor:
            print("Saldo Insuficiente......")
            return
        self.saldo-=valor
        self.detalhes()




class Conta:
    def __init__ (self, titular, saldo, limite):
        self._titular = str(titular)
        self._saldo = float(saldo)
        self._limite = float(limite)

    def printExtrato(self):
        print("Saldo de R${} do titular {}".format(self._saldo, self._titular))

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        self._saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

minha_conta = Conta('Rafael', 1000, 5000)
minha_conta.printExtrato()

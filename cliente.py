class Cliente:
    def __init__(self, nome, assento):
        self._nome = nome
        self._assento = assento

    def infoCliente(self):
        print("Assento {} reservado para o cliente {}".format(self._assento, self._nome))

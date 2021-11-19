
class Conta :

    def __init__(self, numero, titular, saldo, limit=1000.00) :
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limit = limit
        print("Construindo Conta: {}".format(self))

    def extrato(self):
        print("Saldo de {} do titular : {}".format(self.__saldo, self.__titular))

    def depositar(self, valor) :
        self.__saldo += valor

    def __pode_sacar(self, valor) :
        novo_saldo = self.__saldo - valor
        if(novo_saldo > (self.__limit * -1)) :
            return True
        else :
            print("Opera abaixo do seu limite({})".format(self.__limit))
            return False

    def sacar(self, valor) :
        if ( self.__pode_sacar(valor) ) :
            self.__saldo -= valor
            return True
        else :
            return False

    def transferir(self, valor, conta_destino) :
        if self.sacar(valor) :
            conta_destino.depositar(valor)

    @staticmethod
    def codigo_banco() :
        return "001"

    @property
    def titular(self) :
        return self.__titular

    @property
    def saldo(self) :
        return self.__saldo

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
        return self


if ( __name__ == '__main__') :
    conta = Conta(1, 'Fernando', 1000.00, 1000.00)

    conta.depositar(50.01)
    conta.extrato()

    conta2 = Conta(2, 'Prof. Nico', 600.0)

    conta.transferir(3000.00, conta2)

    conta.extrato()
    conta2.extrato()

    print(Conta.codigo_banco())

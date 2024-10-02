class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def relatorio(self):
        print(f"Olá {self.__titular} seu saldo atual é {self.__saldo} e o seu limite atual é {self.__limite}")
    
    def grtlimite(self):
        return self.__limite
    
    def setlimite(self, valor):

        if valor < 0:
            print("informe um valor válido")
        else:
            self.__limite = valor

    def depoditar(self, valor):
        if valor <= 0:
            print("Informe um valor positivo: ")
        else:
            self.__saldo = self.__saldo + valor
    
    def sacar(self, valor):
        if valor <= 0 or valor > self.__saldo:
            print("Saldo insuficiente ou valor negativo solicitado")
        else:
            self.__saldo -= valor
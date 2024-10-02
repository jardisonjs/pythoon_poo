class Celular:
    def __init__(self, numero, saldo, plano, valorMinuto):
        self.__numero = numero
        self.__saldo = saldo
        self.__plano = plano
        self.__valorMinuto = valorMinuto

    def exibirDados(self):
        print(f"Olá seu número é: {self.__numero}\n seu saldo atual é: {self.__saldo}\n O plano que você esta usando é: {self.__plano} O valor da ligação é: {self.__valorMinuto}")


    def getNumero(self):
        return self.__numero
    
    def setNumero(self, valor):
        self.__numero = valor

    
    def exibirPlano(self):
        print(f"Olá seu plano atual é: {self.__plano}")

    def mudarPlano(self, novoPlano):
        self.__plano = novoPlano
        print(f"seu plano agora é: {novoPlano}")

    @property 
    def recarregar(self, valor):
        return self.__saldo

    @recarregar.setter 
    def recarregar(self, valor):
        if valor <= 0:
            print("Informe um valor positivo: ")
        else:
            self.__saldo = self.__saldo + valor

    def fazerChamada(self, duracaoMinutos):
        if duracaoMinutos <= 0:
            print("Você não completou uma ligação.")
        else:
            self.__valorMinuto = duracaoMinutos*1.50
    
    
    
            
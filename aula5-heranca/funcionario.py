class Funcionario:
    def __init__(self, nome, salario):
        #Estamos mudando a visibilidade de privado para protegido, dessa forma, as classes filhas poderão acessar os atributos da classe mãe
        self._nome = nome
        self._salario = salario

    def informacoes(self):
        print(f"Olá {self._nome} seu salario atual é {self._salario}")

#CRIANDO CLASSES FILHAS

class Engenheiro(Funcionario):# A classe Engenheir está herdando as características da classe Funcionario, que será sua classe mãe
    def bonusEngenheiro(self):
        self._salario = self._salario * 1.1#Estamos aumentando o salario em dez porcento

class Surperviso(Funcionario):
    def relatorio(self):
        print(f"O relatorio é o segueti seu {self._nome}, é anos luz ")
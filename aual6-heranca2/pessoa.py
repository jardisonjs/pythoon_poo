class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def info(self):
        print(f"nome: {self._nome} idade: {self._idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)# utilizando o construtor da classe mãe
        self._matricula = matricula

    def estudar(self):
        print(f"{self._nome}, está matriculada com o código: {self._matricula} e continua estudando normalmente")

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    def ensinar(self):
        print(f"{self._nome}, professor(a) da disciplina {self._disciplina}, está ensinando")   

        
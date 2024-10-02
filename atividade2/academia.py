class Aluno:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def exibirDados(self):
        print(f"nome do aluno: {self.nome}\n idade: {self.idade}\n peso: {self.peso}\n altura: {self.altura}")

    def calcularImc(self):
        imc = self.peso/ (self.altura*2)
        print(f"A massa corporal do aluno é: {imc}")

        
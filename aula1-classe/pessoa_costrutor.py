class Pessoa: 
    # criar o método construtor
    def __init__(self, nome, altura, idade):
        # estamos criando os atributos da classe utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valor dos atributos
        self.nome = nome
        self.altura = altura
        self.idade = idade

    #criando os métodos
    def exibirDados(self):
        print(f"Olá {self.nome}, sua altura {self.altura} e sua idade é {self.idade}")


#CRIANDO OS OBJETOS
p1 = Pessoa("Mohaded", 1.69,17)
p2 = Pessoa("Bia", 1.63,17)

p1.exibirDados()
p2.exibirDados()
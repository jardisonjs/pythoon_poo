class Pessoa:
    #atributos
    nome = "profeta"
    peso = 85
    escolaridade = "doutor em matematica"


    #metodos
    def falar(self, texto):
        print(f"tenho algo para te dizer: {texto}")

#CRIANDO OBJETOS
pessoa1 = Pessoa()
print(pessoa1.nome)
pessoa1.falar("silencio, que hoje é segunda-feira porra!!!!")
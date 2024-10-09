class Personagem:
    def __init__(self, nome, vida, rank):
        self._nome = nome
        self._vida = vida
        self._rank = rank

    def receberDano(self, dano):
        self._vida = self._vida-dano

    def detalhes(self):
        print(f"{self._nome} vida: {self._vida} rank: {self._rank}")

class Heroi(Personagem):    
    def __init__(self, nome, vida, rank, identidadeSRC, energia):
        super().__init__(nome, vida, rank)
        self._identidade = identidadeSRC
        self._energia = energia

    def executarHabilidade(self, tipoHabilidade):
        self._energia = self._energia-10

        print(f"Você utilizou {tipoHabilidade} energia: {(self._energia)}")

    def recarregarEN(self):
        self._energia = self._energia+5


    def verificarVida1(self):
        if self._vida < 0:
            print(f"{self._nome} está morto")
        else:
            print(f"{self._nome} está com {self._vida} de vida")
    
    def chamarAliado(self, chamarAliadoo, poderaliado):
        print(f"{self._nome} chamou seu amigo {chamarAliadoo} e ele utilizou o poder {poderaliado}")
    

class Vilao(Personagem):
    def __init__(self, nome, vida, rank, malicia):
        super().__init__(nome, vida, rank)
        self._malicia = malicia
        
    def desferiGOLPE(self, tipoGolpe):
        self._malicia = self._malicia - 10

        print(f"O vilão utilizou o golpe {tipoGolpe} malicia: {self._malicia}")

    def planejarArmadilha(self, tipoArmadilha):
        print(f"O {self._nome} está planejando a usar a armadilha {tipoArmadilha}")

    def verificarVida2(self):
        if self._vida < 0:
            print(f"{self._nome} está morto")
        else:
            print(f"{self._nome} está com {self._vida} de vida")

        
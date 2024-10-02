class Livro:
    def __init__(self, titulo, autor, anoPublicado):
        self.titulo = titulo
        self.autor = autor
        self.anoPubli = anoPublicado
    

    def exibirInformacoes(self):
        print(f"Olá, o titulo do livro é {self.titulo}, seu autor é {self.autor}, o ano que ele foi publicado foi {self.anoPubli}")

    
    def verificarLivro(self):
        tempPubli = 2024 - self.anoPubli
        
        if tempPubli > 50:
            print(f"Este livro é considerado um clássico.")
        else:
            print("Este livro ainda não é considerado um clássico")
            


        
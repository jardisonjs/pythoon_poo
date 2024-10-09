class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        print(f"{self._titulo} o autor é {self._autor}, o ano de publicação foi {self._anoPublicacao}, o número de paginas é: {self._numeroPagina}")

    def calcularitem(self, valor):
        print("escolha a opção ")

class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina > 300:
            print(f"Este livro é longo contendo mais de {self._numeroPagina}.")
    

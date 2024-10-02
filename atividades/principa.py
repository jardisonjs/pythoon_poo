from livro import Livro

tl = input("Informe o nome do livro: ")
aL =  input("Informe o nome do autor do livro: ")
anL = int(input("Informe o ano do livro: "))

l1 = Livro(tl,aL,anL )
l1.exibirInformacoes()
l1.verificarLivro()

l2 = Livro(tl,aL,anL)
l2.exibirInformacoes()
l2.verificarLivro()
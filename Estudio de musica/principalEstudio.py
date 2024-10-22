from estudio_poo import Estudio

A1 = int(input("Entrar(1) Sair(2): "))

if A1 == 1:

    print("Bem vindo a Robinho estudios 'muito abusada' ")

    art = Estudio()
    nome = input("Informe o nome do artista: ")
    genero = input("Informe o genêro do artista: ")
    preco = int(input("Informe o preço do artista: "))
    descricao = input("Informe a descrição: ")
  
    art.inserir(nome, genero, preco, descricao)

    art.consultar()
else:
    print("Você saiu da produtora")






  



  
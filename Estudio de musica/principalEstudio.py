from estudio_poo import Estudio
art = Estudio()

while True:
    print("Seja Bem-vindo ao Estudio Robinho 'A mais abusada' ")
    A1 = int(input("Cadastra(1),Consultar(2),Deletar(3),Consultar Artista(4),Atualizar(5),Sair(6) \n Escolha sua opção: "))

    if A1 == 1:
        
        nome = input("Informe o nome do artista: ")
        genero = input("Informe o genêro do artista: ")
        preco = int(input("Informe o preço do artista: "))
        descricao = input("Informe a descrição: ")
  
        art.inserir(nome, genero, preco, descricao)
    elif A1 == 2:
        art.consultar()
    elif A1 == 3:
        Id = int(input("Informe o Id do artista: "))
        art.deletar(Id)
    elif A1 == 4:
        Id = int(input("Informe o Id do artista específico: "))
        art.contInd(Id) 
    elif A1 == 5:
        Id = int(input("Informe o Id do artista: "))
        nome = input("Informe o novo nome do artista: ")
        
        art.atualizar(nome, Id)
    elif A1 == 6:
        print("Você saiu da produtora")
        break

        




  



  
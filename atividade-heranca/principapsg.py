from personagem import Personagem, Heroi, Vilao

personagem1 = Personagem("Falcão Dourado", 100, "iniciante")
personagem2 = Personagem("Senhor Trevas", 100, "lendario")
heroi1 = Heroi("Falcão Dourado", 100, "iniciante", "Cavaleiro Branco", 50)
vilao1 = Vilao("Senhor Trevas", 100, "lendario", 70)

personagem1.detalhes()
personagem2.detalhes()

heroi1.detalhes
heroi1.receberDano(30)
heroi1.recarregarEN()
heroi1.executarHabilidade("Super Força")
heroi1.chamarAliado("naruto", "rasengan")   


vilao1.detalhes
vilao1.receberDano(40)
vilao1.desferiGOLPE("Chama Negra")

heroi1.verificarVida1()
vilao1.verificarVida2()







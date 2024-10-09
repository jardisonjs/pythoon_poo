from funcionario import Funcionario, Engenheiro, Surperviso

f1 = Funcionario("Arieli", 7000)
engenheiro1 = Engenheiro("tomas",3000)
sp =Surperviso("tomas",3000)
f1.informacoes()

engenheiro1.bonusEngenheiro()
engenheiro1.informacoes()

sp.relatorio()


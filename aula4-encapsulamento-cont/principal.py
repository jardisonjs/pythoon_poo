from funcionario import Funcionario

funcionario1 = Funcionario("Ketlen", 3000)

print(funcionario1.getNome())

funcionario1.setNome("kaio")

print("Seu nome atual é", funcionario1.getNome())

print("seu salario atual é", funcionario1.salario)

funcionario1.salario = -500

print("Seu salario atual é: ", funcionario1.salario)
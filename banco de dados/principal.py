from funcionario_poo import Funcionario

f1 = Funcionario()

nome = input("informe o nome do funcionario: ")
salario = float(input("informe o salário do funcionario: "))
cargo = input("informe o cargo do funcionario: ")

f1.inserir(nome, salario, cargo)

f1.consultar()
from academia import Aluno

alu = input("Informe o seu nome: ")
id =  input("Informe sua idade: ")
ps = int(input("Informe o seu peso: "))
H = float(input("informe sua altura: "))

l1 = Aluno(alu,id,ps,H)
l1.exibirDados()
l1.calcularImc()


l2 = Aluno("mohamed", 17, 54, 1.70)
l2.exibirDados()
l2.calcularImc()

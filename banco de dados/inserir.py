import sqlite3

#passo1 - conexão com o banco
conexao = sqlite3.connect("departamento.db")

#Passo 2 - verificar se a tabela existe oyu não
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
#Passo3 - Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados
consulta = conexao.cursor()

#Passo4 - Executar o comando de criação da tabela
consulta.execute(tabela)

#INSERIR DADOS NA TABELA
#passo5 - solicitar dados do usuario
nome = input("informe o nome do funcionario: ")
salario = float(input("informe o salário do funcionario: "))
cargo = input("informe o cargo do funcionario: ")

#passo6 - Criando sql para inserir os dados na tabela
sql = "INSERT INTO funcionario VALUES(?,?,?,?)"# clocamos ? no luagr dos daddos reasi, para evitar possíveis ataques de sql injection. Isso é uma implementação da biblioteca sqlite3

#passo7 - Organizar os dados que irão substituir ? no coando sql
campos = (None, nome, salario, cargo)# Criando uma tlupa com os dados que irão subistituir ? Ao informar o valor "None", estamos dizendo que será atribuido o valor padrão do AUTOINCREMENT

#pPasso8 - Executar o comando sql e substituir '?' pelos campos 
consulta.execute(sql, campos)

#passo9 - Gravar os dados no banco 
conexao.commit()

print(consulta.rowcount, " linha(s) inseridas com sucesso")

#Passo10 - encerrar a conexão
conexao.close()

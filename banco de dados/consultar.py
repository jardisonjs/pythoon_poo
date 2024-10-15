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

#passo5 - Criando sql para consultar os dados na tabela
sql = "SELECT * FROM funcionario"

#pPasso6 - Executar o comando sql 
consulta.execute(sql)

#passo7 - Exibir dados de tabela
resultado = consulta.fetchall()#Fetchall() irá trazer todos os registros que existem na tabela do banco de dados
print(resultado)

for itens in resultado:
    print(f"Códigos: {itens[0]}, Nome:{itens[1]}")

#Passo8 - encerrar a conexão
conexao.close()

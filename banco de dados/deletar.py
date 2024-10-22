import sqlite3

#conexão
conexao = sqlite3.connect("departamento.db")

consultar = conexao.cursor()

tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
"""
consultar.execute(tabela)


codigo = int(input("Informe o código do funcionario: "))

sql = "DELETE FROM funcionario WHERE codigo = ?"

campos = (codigo,)

consultar.execute(sql, campos)

conexao.commit()

print(consultar.rowcount, " linha(s) deletada(s) com sucesso")

conexao.close()
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


nome = input("Informe o novo nomedo funcionario: ")
codigo = int(input("Informe o código do funcionario: "))

sql = "UPDATE funcionario SET nome = ? WHERE codigo = ?"

campos = (nome, codigo)

consultar.execute(sql, campos)

conexao.commit()

print(consultar.rowcount, " linha(s) atualizada (s) com sucesso")

conexao.close()
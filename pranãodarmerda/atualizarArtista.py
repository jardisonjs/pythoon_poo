import sqlite3

conexao = sqlite3.connect("estudioMusica_db.db")

tabela = """
CREATE TABLE IF NOT EXISTS artistas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    genero VARCHAR(100),
    preco FLOAT,
    descricao VARCHAR(100)
);
"""
consulta = conexao.cursor()

consulta.execute(tabela)

nome = input("Informe o novo nome do artista: ")
id = int(input("Informe o id do artista: "))


sql = "UPDATE funcionario SET nome = ? WHERE id = ?"

campos = (nome, id)

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, " linha(s) atualizada (s) com sucesso")

conexao.close()
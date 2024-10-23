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

nome = input("informe o nome do artista: ")
genero = input("informe o genero do artista: ")
preco = int(input("Informe o preço do artista: "))
descricao = input("informe a descrição do artista: ")

sql = "INSERT INTO artistas VALUES(?,?,?,?,?)"

campos = (None, nome, genero, preco, descricao)

consulta.execute(sql, campos)

conexao.commit()

print(consulta.rowcount, " linha(s) inseridas com sucesso")

conexao.close()

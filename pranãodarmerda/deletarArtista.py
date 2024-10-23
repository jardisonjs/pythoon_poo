import sqlite3

conexao = sqlite3.connect("estudioMusica_db.db")

consulta = conexao.cursor()

tabela = """
CREATE TABLE IF NOT EXISTS artistas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    genero VARCHAR(100),
    preco FLOAT,
    descricao VARCHAR(100)
);
"""

consulta.execute(tabela)

Id = int(input("informe o id do artista: "))

sql = "DELETE FROM artistas WHERE Id = ?"

campos = (Id,)

consulta.execute(sql, campos)

conexao.commit()

if consulta.rowcount == 0:
    print("esse id não existe-")
else:
    print(consulta.rowcount, " linha(s) deletada(s) com sucesso")
    
conexao.close()


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

sql = "SELECT * FROM artistas WHERE Id = ?"

campos = (Id,)

consulta.execute(sql, campos)

conexao.commit()

resultado = consulta.fetchall()
print(resultado)


for itens in resultado:
    print(f"Id:{itens[0]},\n Nome:{itens[1]} \n genero:{itens[2]} \n  preço:{itens[3]} \n  descrição:{itens[4]}")

conexao.close()


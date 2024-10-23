import sqlite3
class Estudio:
    def conexao(self):
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
        return conexao
    
    def inserir(self, nome, genero, preco, decricao):
        conexao = self.conexao()
       
        sql = "INSERT INTO artistas VALUES (?,?,?,?,?)"

        campos = (None, nome, genero, preco, decricao)

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, "Linha(s) inserido(s) com sucesso")

        conexao.close()

    def consultar(self,):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = "SELECT * FROM artistas"
        consulta.execute(sql)

        resultado = consulta.fetchall()

        for itens in resultado:
            print(f"Nome: {itens [1]}")
            print(f"genero: {itens [2]}")
            print(f"preco: {itens [3]}")
            print(f"descrição: {itens [4]}")
            print(f"-"*40) # criando um separador entre cada registro
            
        conexao.close()

    def contInd(self,Id):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = "SELECT * FROM artistas WHERE Id = ?"
        campos = (Id,)
        consulta.execute(sql, campos)

        resultado = consulta.fetchall()

        for itens in resultado:
            print(f"id: {itens [0]}")
            print(f"Nome: {itens [1]}")
            print(f"genero: {itens [2]}")
            print(f"preco: {itens [3]}")
            print(f"descrição: {itens [4]}")
            print(f"-"*40) # criando um separador entre cada registro
            
        conexao.close()

    def atualizar(self, nome, Id):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = "UPDATE artistas SET nome = ? WHERE Id = ?"

        campos = (nome, Id)
        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, " linha(s) atualizada (s) com sucesso")

        conexao.close()



    def deletar(self, Id):
        conexao = self.conexao()
        consulta = conexao.cursor()
        
        sql = "DELETE FROM artistas WHERE Id = ?"

        campos = (Id,)

        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, " linha(s) deletada(s) com sucesso")
    
        conexao.close()

        





        
               
from conta import Conta

minhaConta = Conta(321, "Epamenondas Soares", 2000, 500)

minhaConta.relatorio()

minhaConta.setlimite(8000)
minhaConta.relatorio()

print(f"o seu limite anual é {minhaConta.grtlimite()}")

minhaConta.depoditar(200)
minhaConta.relatorio()

minhaConta.sacar(150)
minhaConta.relatorio()
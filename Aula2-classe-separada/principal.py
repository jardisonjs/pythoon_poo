#Estamos acessando o arquivo pessoa e dentro desse arquivo estamos importando a classe 'Pessoa'
from pessoa import Pessoa

#Criando Objetos

p1 = Pessoa("Joana","Correr", "Rua dos alfinetes 2121")
p1.exibirHobby()
p1.mudarHobby("Natação")

#SOLICITANDO DADOS SO USUÁRIO
nomePessoa = input("informe o nome da pessoa: ")
hobbyPessoa = input("informe o hobby da pessoa: ")
endPessoa = input("Qual o endereço? ")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby()
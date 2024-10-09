from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Garibalde", 54)
aluno1 = Aluno("Mohamed", 17, 666777)
prof = Professor("Anacleto", 46, "profecia") 

pessoa1.info()

aluno1.info()
aluno1.estudar()

prof.info()
prof.ensinar()
class Pessoa:
    def __init__(self,matricula,nome,sexo,idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.idade = idade

pessoa1 = Pessoa("12345678", "kaua" ,"m", "15")
print(pessoa1.matricula,pessoa1.nome,pessoa1.sexo,pessoa1.idade)
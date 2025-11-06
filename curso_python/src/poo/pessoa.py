class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Ana", 25)
p1.nome = "Guilherme"
print(p1.nome, p1.idade)

p2 = Pessoa("Bia", 30)
print(p2.nome, p2.idade)

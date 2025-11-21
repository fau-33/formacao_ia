class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nome}, {self.email}"



lista_clientes = [
    Cliente("Flavio", "flavio@gmail.com"),
    Cliente("Pedro", "pedro@gmail.com"),
    Cliente("Jorge", "jorge@empresa.com"),
    Cliente("Maria", "maria@empresa.com"),
    Cliente("Luis", "luis@yahoo.com"),
]

r1 = filter(lambda c: "@empresa.com" in c.email, lista_clientes)
clientes_filtrados = list(r1)

for cliente in clientes_filtrados:
    print(cliente)
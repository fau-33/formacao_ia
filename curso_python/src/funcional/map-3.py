class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


lista_clientes = [
    Cliente("Flavio", "flavio@flavio.com"),
    Cliente("Pedro", "pedro@pedro.com"),
    Cliente("Jorge", "jorge@jorge.com"),
    Cliente("Maria", "maria@maria.com"),
    Cliente("Luis", "luis@luis.com"),
]

lista_emails = map(lambda cliente: cliente.email, lista_clientes)
print(list(lista_emails))

lista_nomes = map(lambda cliente: cliente.nome, lista_clientes)
print(list(lista_nomes))

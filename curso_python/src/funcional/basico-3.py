def remover_nome(nome):
    def remover_na_lista(lista):
        return [pessoa for pessoa in lista if pessoa != nome]
    return remover_na_lista

remover_flavio = remover_nome("Flavio")
remover_maria = remover_nome("Maria")

lista_1 = ["Flavio", "Maria", "Pedro", "Maria", "Jorge"]
lista_2 = ["Guilherme","Flavio", "Rebeca", "Chico", "Tereza", "Maria"]

print(remover_flavio(lista_1))
print(remover_maria(lista_1))

print(remover_flavio(lista_2))
print(remover_maria(lista_2))

print(remover_nome("Jorge")(lista_1))



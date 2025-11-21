lista_nomes = ["Flavio", "Pedro", "Jorge", "Maria", "Luis", "Ana"]
lista_idades = [25, 30, 35, 40, 45, 50]
lista_estados = ["SP", "RJ", "RS", "SC", "MG", "ES"]

r1 = zip(lista_nomes, lista_idades, lista_estados)
# print(dict(r1))
# print(list(r1))

for nome, idade, estado in r1:
    print(f"{nome} tem {idade} anos e mora em {estado}")
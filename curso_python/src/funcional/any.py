lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r1 = any(x % 2 == 0 for x in lista)

if r1:
    print("Tem pelo menos um número par")
else:
    print("Não tem números pares")
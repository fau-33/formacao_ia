print("Iterando uma LISTA:")
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for num in lista:
    print(num, end=" ")

for i, num in enumerate(lista):
    print(f"\nPosicao ({i}: {num})")

print("\n\nIterando uma TUPLA:")
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for num in tupla:
    print(num, end=" ")

print("\n\nIterando um SET:")
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10}

for num in conjunto:
    print(num, end=" ")

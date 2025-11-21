numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r1 = filter(lambda x: x % 2 == 0, numeros)
print(list(r1))

r2 = filter(lambda x: x < 100, numeros)
print(list(r2))

r3 = filter(lambda x: x > 100, numeros)
print(list(r3))


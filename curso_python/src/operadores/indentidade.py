# Tipicos Básicos - Imútaveis
a = 6
b = 5 + 1

print(id(a))
print(id(b))
print(a == b)  # True
print(a is b)  # True

# Tipicos Compostos - Mutáveis
x = [1, 2, 3]
y = [1, 2, 3]

print(id(x))
print(id(y))
print(x == y)  # True
print(x is y)  # False

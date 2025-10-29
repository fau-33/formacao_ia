texto = "Seja bem-vindo ao Python!"
print("Python" in texto)  # True

lista = [1, 2, 3]
print(2 in lista)  # True
print(7 not in lista)  # False

tupla = ("a", "b", "c")
print("b" in tupla)  # True
print("d" not in tupla)  # True

conjunto = {"banana", "maçã", "laranja", "pera"}
resultado = "maçã" in conjunto
print(resultado)  # True

dicionario = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

print("idade" in dicionario)  # True
print("profissão" not in dicionario)  # True
print("cidade" in dicionario)  # True
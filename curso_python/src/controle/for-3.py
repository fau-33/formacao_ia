funcionario = {
    "nome": "Guilherme",
    "salario": 789.89,
    "idade": 25,
    "cidade": "Sao Paulo",
    "ativo": True,
}

for chave in funcionario:
    print(chave)

for chave in funcionario.keys():
    print(chave, "=>", funcionario[chave])

for valor in funcionario.values():
    print(valor)

for chave, valor in funcionario.items():
    print(chave, "=>", valor)

funcionario = {"nome": "Guilherme", "cidade": "Sao Paulo", "ativo": True}

funcionario["ativo"] = False

print(funcionario)

funcionario.update({"ativo": True, "cidade": "Rio de Janeiro"})

print(funcionario)

cidade = funcionario.pop("cidade")

print(cidade)
print(funcionario)

funcionario.clear()

print(funcionario)

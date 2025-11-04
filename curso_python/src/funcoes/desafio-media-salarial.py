# Média salarial ponderada
# Pergunta ao usuario -> Tipo de cargo, quantidade de funcionarios,
# salario e colocar deseja continuar(s/n)
# ai quando coloca não fazer os calculos e quantidade de funcionarios
# função => aux. administrativo, quantidade = 5, salario = 1100
# função => atendente, quantidade = 16, salario = 2000
# função => gerente, quantidade = 3, salario = 5500
# função => diretor, quantidade = 1, salario = 12500
# media ponderada dos salarios o usuario que vai informar tipo de cargo,
# qtde de funcionarios e salario


def calcular_media_ponderada(soma_salarios_ponderados, total_funcionarios):
    if total_funcionarios > 0:
        return soma_salarios_ponderados / total_funcionarios
    return 0.0


soma_salarios_ponderados = 0.0

total_funcionarios = 0

print("--- Calculadora de Média Salarial Ponderada ---")
print("Insira os dados de cada cargo na empresa.")


while True:

    tipo_cargo = input("\nInforme o tipo de cargo (Ex: Aux. Administrativo): ")

    qtde_funcionario = input(
        f"Informe a quantidade de funcionários para '{tipo_cargo}': "
    )

    quantidade_funcionarios = int(qtde_funcionario)

    salario = input(f"Informe o salário base para '{tipo_cargo}': ")

    salario_base = float(salario)

    if quantidade_funcionarios <= 0 or salario_base <= 0:
        print("Qtde de funcionários e salário devem ser valores positivos.")
        continue

    peso_cargo = salario_base * quantidade_funcionarios

    soma_salarios_ponderados += peso_cargo
    total_funcionarios += quantidade_funcionarios

    while True:
        continuar = input(
            "\nDeseja continuar inserindo dados de cargos (s/n)? "
        ).lower()
        if continuar in ("s", "n"):
            break
        print("Resposta inválida.")

    if continuar == "n":
        break


print("\n--- Resultado do Cálculo ---")

if total_funcionarios > 0:

    media_ponderada = calcular_media_ponderada(
        soma_salarios_ponderados, total_funcionarios
    )

    print(f"Total de funcionários considerados: {total_funcionarios}")
    print(f"Soma dos salários ponderados: R$ {soma_salarios_ponderados:,.2f}")
    print("Média Salarial Ponderada da Empresa:")
    print(
        f"R$ {media_ponderada:,.2f}".replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

    print("-" * 45)
else:
    print("Não é possível calcular a média.")

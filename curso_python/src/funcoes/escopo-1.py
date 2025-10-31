# Escopo global
sobrenome = "Silva"


def exibir_nome():
    # Escopo local
    nome_completo = f"Guilherme {sobrenome}"
    print(nome_completo)


exibir_nome()

menu = [
    "Menu:",
    "----------------",
    "1. Opcao A",
    "2. Opcao B",
    "3. Sair",
]

opcao_selecionada = 0

# O loop continua até que 3 seja selecionado
while opcao_selecionada != 3:
    print("\n".join(menu))

    # Pede a opção e converte diretamente para inteiro
    opcao_selecionada = int(input("Informe a opcao desejada [1-3]: "))

    # --- Bloco de Ações (AGORA DENTRO DO LOOP) ---
    if opcao_selecionada == 1:

        nome = input("Informe o seu nome: ")
        print(f"O nome digitado foi: {nome}")

        input("Pressione enter para continuar...")
    elif opcao_selecionada == 2:

        email = input("Informe o seu email: ")
        print(f"O email digitado foi: {email}")

        input("Pressione enter para continuar...")
    elif opcao_selecionada == 3:
        print("Saindo...")
    else:

        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")


print("Fim")

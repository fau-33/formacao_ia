# Desafio Menu
# 1. Opção A
# 2. Opção B
# 3. Sair
# Informe a opção desejada[1-3]:
# quando fazer isso sempre limpar o terminal
# na opção A quando selcionado é pra pergunta
# ao usuario o seu nome e coloca ao contrario
# na opção B quando seleciondo vai pergunta
# o email e deve pega o dominio do email digitado
# sempre limpando a tela
# fazer criando funções


import os


# Função para limpar o terminal/tela
def limpar_tela():
    """Limpa a tela do terminal."""
    # Para Windows
    if os.name == "nt":
        os.system("cls")
    # Para Linux/Unix/macOS
    else:
        os.system("clear")


# Função para a Opção A: Inverter o nome
def opcao_a():
    """Pergunta o nome ao usuário e exibe ele invertido."""
    limpar_tela()
    print("### Opção A: Inverter Nome ###")
    nome = input("Informe o seu nome: ")

    nome_invertido = nome[::-1]
    print(f"\nO nome digitado foi: **{nome}**")
    print(f"O nome invertido é: **{nome_invertido}**")
    input("\nPressione ENTER para voltar ao menu...")


# Função para a Opção B: Pegar o domínio do e-mail
def opcao_b():
    """Pergunta o email e exibe o domínio."""
    limpar_tela()
    print("### Opção B: Pegar Domínio do E-mail ###")
    email = input("Informe o seu email: ")

    if "@" in email:

        dominio = email.split("@")[-1]
        print(f"\nO e-mail digitado foi: **{email}**")
        print(f"O domínio do e-mail é: **{dominio}**")
    else:
        print("\nO e-mail  formato válido (faltando '@').")

    input("\nPressione ENTER para voltar ao menu...")


# Função do Menu
def menu():
    """Exibe o menu e solicita a opção ao usuário, limpando a tela antes."""
    while True:
        limpar_tela()
        print("# Desafio Menu")
        print("----------------")
        print("1. Opção A (Inverter Nome)")
        print("2. Opção B (Dominio do E-mail)")
        print("3. Sair")
        print("----------------")

        try:

            opcao_selecionada = int(input("Informe a opção desejada [1-3]: "))

            if 1 <= opcao_selecionada <= 3:
                return opcao_selecionada
            else:
                print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")
                input("Pressione ENTER para tentar novamente...")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número.")
            input("Pressione ENTER para tentar novamente...")


# --- Lógica Principal ---
def main():
    """Função principal que executa o loop do menu."""
    opcao_selecionada = 0
    while opcao_selecionada != 3:
        opcao_selecionada = menu()

        if opcao_selecionada == 1:
            opcao_a()
        elif opcao_selecionada == 2:
            opcao_b()
        # Se for 3, o loop termina

    limpar_tela()  # Limpa a tela uma última vez
    print("Fim do programa. Obrigado!")


# Execução do programa
if __name__ == "__main__":
    main()

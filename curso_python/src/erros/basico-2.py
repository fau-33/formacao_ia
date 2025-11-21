def executar_divisao(tentativas=1):
    try:
        divisor = int(input("Digite um divisor: "))
        return 1000 / divisor
    except Exception as e:
        if tentativas >= 5:
            raise e
        print(f"Erro inesperado: {e}")
        print(f"Tentativas: ({tentativas}/5)")
        return executar_divisao(tentativas + 1)

resultado = executar_divisao()
print(f"O resultado da divisão é {resultado}")
try:
    divisor = input("Digite um divisor: ")
    resultado = 1000 / int(divisor)
    print(f"O resultado da divisão é {resultado}")

except ZeroDivisionError:
    print("Não é possível dividir por zero")
except Exception as e:
    print(f"Erro inesperado: {e}")
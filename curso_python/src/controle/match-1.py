n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operacao desejada (+, -, *, /): ")

resultado = 0

match operacao:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*" | "x":
        resultado = n1 * n2
    case "/":
        resultado = n1 / n2
    case _:
        print("Operação inválida")

print(f"O resultado eh {resultado}")

print("Fim")

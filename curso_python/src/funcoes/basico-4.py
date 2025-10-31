# Função COM parâmetros e COM retorno
def conta_com_gorjeta(valor_conta, percentual_gorjeta):
    valor_gorjeta = valor_conta * percentual_gorjeta
    return valor_conta + valor_gorjeta


print(conta_com_gorjeta(100, 0.15))

valor_total = conta_com_gorjeta(100, 0.1)
print(f"O valor total eh {valor_total}")  # 110

print(conta_com_gorjeta(690, 0.08))

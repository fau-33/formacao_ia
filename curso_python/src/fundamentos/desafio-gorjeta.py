# Solicite ao usuario o total de uma conta de restaurante
# e a porcentagem de gorjeta que ele gostaria de dar
# Calcule e mostre o valor total da conta incluindo a gorjeta


usuario_total = input("Digite o valor da conta: ")
total = float(usuario_total)

usuario_gorjeta = input("Digite a porcentagem de gorjeta (0-100): ")
gorjeta = float(usuario_gorjeta)

valor_gorjeta = total * gorjeta / 100

total_com_gorjeta = total * (1 + gorjeta / 100)

print(f"Valor da conta: R$ {total:.2f}")
print(f"Gorjeta ({gorjeta}%): R$ {valor_gorjeta:.2f}")
print(f"Total com gorjeta: R$ {total_com_gorjeta:.2f}")

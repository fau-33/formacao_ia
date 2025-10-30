# Escreva um programa que pergunte ao usuario a velocidade do carro
# caso ultrapasse 80km/h, exiba uma mensagem que foi multado
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h

velocidade_usuario = float(input("Digite a velocidade do carro: "))

if velocidade_usuario > 80:
    multa = (velocidade_usuario - 80) * 5
    print(f"Voce foi multado em R$ {multa:.2f}")
else:
    print("Voce nao foi multado")

    print("Fim")

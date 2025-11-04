def calcular_media(*notas):

    return sum(notas) / len(notas)


media = calcular_media(7, 5.5, 9.5, 8.8, 10, 9.9)
print(f"O valor da media eh {media:.1f}")

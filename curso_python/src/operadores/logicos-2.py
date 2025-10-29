entrada_1 = input("Trabalho de terca? [0-1] ")
entrada_2 = input("Trabalho de quinta? [0-1] ")

terca = bool(int(entrada_1))
quinta = bool(int(entrada_2))

comprar_tv_60 = terca and quinta # AND
comprar_tv_32 = terca != quinta # XOR
tomar_sorvete = terca or quinta # OR
ficar_em_casa = not tomar_sorvete  # NOT

print("Comprar TV 60'? ", comprar_tv_60)
print("Comprar TV 32'? ", comprar_tv_32)
print("Tomar sorvete? ", tomar_sorvete)
print("Ficar em casa? ", ficar_em_casa)


# Peça ao usuário que insira uma quantidade de quilômetros
# e converta para milhas
# lembre-se que 1 quilometro equivale a 1.61 milhas

distancia_quilometros = float(input("Digite a distancia (km): "))
RELACAO_KM_MILHAS = 0.621371

distancia_milhas = distancia_quilometros * RELACAO_KM_MILHAS

print(f"{distancia_quilometros} km = {distancia_milhas} milhas")

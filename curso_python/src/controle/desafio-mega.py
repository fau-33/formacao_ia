# Escreva em python que gere numeros da mega sena
# Primeiramente mande para o usuário informar quantidade
# números da aposta (entre 6 e 20) e depois gere
# uma lista com o tamanho solicitados com números não repetidos entre 1 e 60

import random

qtd = int(input("Quantidade de numeros da aposta (6 a 20): "))

# validação simples da quantidade
while qtd < 6 or qtd > 20:
    qtd = int(input("Valor inválido. Informe um número entre 6 e 20: "))

# gera números únicos entre 1 e 60
numeros = set()
while len(numeros) < qtd:
    numeros.add(random.randint(1, 60))

aposta = sorted(numeros)
print("Sua aposta:", aposta)

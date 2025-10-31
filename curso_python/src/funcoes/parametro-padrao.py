# Escreva em python que gere numeros da mega sena
# Primeiramente mande para o usuário informar quantidade
# números da aposta (entre 6 e 20) e depois gere
# uma lista com o tamanho solicitados com números não repetidos entre 1 e 60
# usando funcao com parâmetro padrao

import random

quantidade = int(input("Quantidade de numeros da aposta (6 a 20): "))


def gerar_aposta(quantidade=6):
    if quantidade < 6 or quantidade > 20:
        return "Aposta inválida"
    else:
        numeros = random.sample(range(1, 61), quantidade)
        return sorted(numeros)


aposta = gerar_aposta(quantidade)
print("Sua aposta:", aposta)

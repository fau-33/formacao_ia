def repetir(funcao, qtde = 2):
    for _ in range(qtde):
        funcao()
    


def bom_dia():
    print("Bom dia!")


repetir(bom_dia, 5)






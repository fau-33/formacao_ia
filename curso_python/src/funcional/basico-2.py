def somar(a):
    def finalizar_soma(b):
        return a + b
    return finalizar_soma

print(somar(10)(20))

SALARIO_BASE = 2356.88  
somar_com_salario_base = somar(SALARIO_BASE)

print(somar_com_salario_base(276.88))
print(somar_com_salario_base(444))


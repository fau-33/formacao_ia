x = "global"


def minha_funcao():
    # global x
    x = "local"
    print("Dentro da funcao", x)


print("Antes da funcao", x)
minha_funcao()
print("Depois da funcao", x)

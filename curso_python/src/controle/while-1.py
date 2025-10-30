valor = ""
contador = 1

while valor.lower() != "sair":
    valor = input("Informe um algo ou sair: ")
    print(f"{contador}. O valor digitado foi:", valor)
    contador += 1

print("Fim")

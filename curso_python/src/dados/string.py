primeiro_nome = "Guilherme"
sobrenome = "Silva"

nome_completo = primeiro_nome + " " + sobrenome

print(nome_completo)

# h = input("Informe a hora ? ")
# m = input("Informe os minutos ? ")
# s = input("Informe os segundos ? ")

# data_formatada = f"{h}:{m}:{s}"

# print(data_formatada.format(h, m, s))

texto = """ Este e um exemplo
de uma string 
que ocupa varias linhas"""

print(texto.upper())
print(texto.find("varias"))
print(texto.split())

listas_palavras = texto.split()
print(listas_palavras)
print("-".join(listas_palavras))

print(len(texto))

valor = "123456"
print(valor.isnumeric())

real = "123.45"
print(real.replace(".", "", 1).isnumeric())

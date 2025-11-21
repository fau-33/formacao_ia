numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in numeros:
    if n % 2 == 0:
        continue
    print(n, end=" ")

print("\n")

for n in numeros:
    if n == 5:
        break
    print(n, end=" ")

print("fim")

print("\n\n--- Exemplo 2 (Strings) ---")

# Exemplo com continue: Imprimir apenas as consoantes (pular vogais e espaços)
frase = "O Python eh legal"
print(f"Frase original: {frase}")
print("Apenas consoantes: ", end="")

for letra in frase:
    if letra.lower() in "aeiou ":
        continue
    print(letra, end="")

print("\n")

# Exemplo com break: Parar ao encontrar uma palavra "proibida" ou de parada
comandos = ["andar", "pular", "correr", "parar", "agachar"]
print(f"Lista de comandos: {comandos}")

for comando in comandos:
    if comando == "parar":
        print("Comando 'parar' encontrado! Encerrando execução.")
        break
    print(f"Executando: {comando}")



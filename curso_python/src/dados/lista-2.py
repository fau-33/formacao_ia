numeros = [1, 2, 3]

numeros.append(4)

print(numeros)  # Saida: [1, 2, 3, 4]

numeros.insert(1, 99)

print(numeros)  # Saida: [1, 99, 2, 3, 4]

numeros.remove(4)
numeros.remove(99)

print(numeros)  # Saida: [1, 2, 3]

# Pilha (stack) LIFO = Last In First Out
pilha_livros = ["MMM", "DDD", "Habitos atomicos"]
pilha_livros.append("Range")
print(pilha_livros)

print(f"Acabei de ler o livro {pilha_livros.pop()}")
print(f"Acabei de ler o livro {pilha_livros.pop()}")
print(f"Acabei de ler o livro {pilha_livros.pop()}")


print(len(pilha_livros))

# Fila (queue) FIFO = First In First Out
fila_kalzone = ["Guilherme", "Joao", "Maria"]
print(f"Qual o seu pedido {fila_kalzone.pop(0)}?")
print(f"Qual o seu pedido {fila_kalzone.pop(0)}?")
print(f"Qual o seu pedido {fila_kalzone.pop(0)}?")

print(len(fila_kalzone))

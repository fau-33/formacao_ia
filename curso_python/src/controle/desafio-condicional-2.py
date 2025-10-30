# Faça um programa que leia três números
# e mostre qual o maior e menor entre eles
# usando if - elif - else

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

# Encontrar o maior numero
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

# Encontrar o menor numero
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

print(f"O maior numero eh {maior}")
print(f"O menor numero eh {menor}")

print("Fim")

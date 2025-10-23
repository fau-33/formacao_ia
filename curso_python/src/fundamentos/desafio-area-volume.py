# Solicite ao usuario o raio de um circulo e calcule
# a area e o volume da esfera
# area = pi * raio ** 2
# volume = (4/3) * pi * raio ** 3

PI = 3.14159
usuario = input("Digite o raio do circulo: ")
raio = float(usuario)

area = PI * raio**2
volume = (4 / 3) * PI * raio**3

print(f"A area do circulo eh {area}")
print(f"O volume da esfera eh {volume}")

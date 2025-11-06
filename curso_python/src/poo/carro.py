class Carro:
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

    def buzinar(self, qtde=1):
        for i in range(qtde):
            print(f"{self.marca} {self.modelo}: Biiiiii!")


c1 = Carro("VW", "Gol")
c1.acelerar()
c1.acelerar()
c1.acelerar()
c1.buzinar()
print(c1.marca, c1.modelo, c1.velocidade)

c2 = Carro("Ford", "Fusion")
c2.acelerar()
c2.acelerar()
c2.acelerar()
c2.acelerar()
c2.frear()
c2.frear()

c2.buzinar(3)
print(c2.marca, c2.modelo, c2.velocidade)

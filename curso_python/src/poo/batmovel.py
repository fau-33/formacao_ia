class Carro:
    def dirigir(self):
        print("Você está dirigindo")

class Barco:
    def navegar(self):
        print("Você está navegando")

class Aviao:
    def voar(self):
        print("Você está voando")

class carroAnfibio(Carro, Barco):
    pass

class CarroVoador(Carro, Aviao):
    pass

class Batmóvel(Carro, Barco, Aviao):
    pass

carro = carroAnfibio()
carro.dirigir()
carro.navegar()

carro = CarroVoador()
carro.dirigir()
carro.voar()

carro = Batmóvel()
carro.dirigir()
carro.navegar()
carro.voar()
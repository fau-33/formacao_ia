class Calculadora:
    def __init__(self, valor_inicial = 0):
        self.__valor = valor_inicial
    
    def somar(self, valor):
        self.__valor += valor
        return self

    def subtrair(self, valor):
        self.__valor -= valor
        return self

    def multiplicar(self, valor):
        self.__valor *= valor
        return self

    def dividir(self, valor):
        self.__valor /= valor
        return self
        
    @property
    def valor(self):
        return self.__valor
    
    def __add__(self, other):
        return Calculadora(self.valor + other.valor)
    
    def __eq__(self, other):
        return self.__valor == other.__valor

    def __str__(self):
        return f"A calculadora tem um valor em memoria de {self.__valor}"

calc1 = Calculadora(100)
resultado = calc1.somar(50).subtrair(25).multiplicar(2).dividir(5).valor
print(resultado)

calc2 = Calculadora(100).multiplicar(3.1415)
print(calc2.valor)

calc3 = calc1 + calc2
print(calc3)

calc4 = calc1 + calc2
print(calc4 == calc3)
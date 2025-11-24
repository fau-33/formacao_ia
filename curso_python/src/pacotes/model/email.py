from utils.validador import Validador

class Email:
    def __init__(self, valor, atributo="Email"):
        self.__valor = Validador(valor, atributo).nao_nulo().email().valor
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def usuario(self):
        return self.__valor.split("@")[0]
    
    @property
    def dominio(self):
        return self.__valor.split("@")[1]
    
    def __str__(self):
        return self.__valor
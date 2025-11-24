class Validador:
    def __init__(self, valor, atributos, erros=[]):
        self.__valor = valor
        self.__atributos = atributos
        self.__erros = erros
    
    @property
    def valor(self):
      if self.__erros:
        raise ValueError(self.__erros)
      return self.__valor 
    
    def nao_nulo(self):
      if self.__valor == None:
        self.__erros.append(f"{self.__atributos} não pode ser nulo")
      return self
    
    def nao_vazio(self):
      if self.__valor == None:
        return self

      if not self.__valor or not self.__valor.strip():
        self.__erros.append(f"{self.__atributos} não pode ser vazio")
      return self
    
    def tamanho_minimo(self, minimo):
      if self.__valor == None:
        return self

      if len(self.__valor) < minimo:
        self.__erros.append(f"{self.__atributos} deve ter pelo menos {minimo} caracteres")
      return self
    
    def tamanho_maximo(self, maximo):
      if self.__valor == None:
        return self

      if len(self.__valor) > maximo:
        self.__erros.append(f"{self.__atributos} deve ter no máximo {maximo} caracteres")
      return self


    def quantidade_min_palavras(self, qtde):
      if self.__valor == None:
        return self

      if len(self.__valor.split()) < qtde:
        self.__erros.append(f"{self.__atributos} deve ter pelo menos {qtde} palavras")
      return self
    
    def email(self):
      if self.__valor == None:
        return self

      if '@' not in self.__valor:
        self.__erros.append(f"{self.__atributos} não é um email válido")
      return self
    
if __name__ == "__main__":
    v = Validador("teste", "atributo").nao_vazio().tamanho_minimo(6).valor
    print(v)
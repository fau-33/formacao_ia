class FuncionarioV1:
    def __init__(self, salario):
        self.__salario = salario
    
    # Getters
    def get_salario(self):
        return self.__salario 
    
    # Setters
    def set_salario(self, novo_salario):
        self.__salario = novo_salario
    
    @property
    def salario(self):
        return self.__salario   
    
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario < 1518:
            raise ValueError("Salário não pode ser menor que o salário mínimo.")
        self.__salario = novo_salario


func = FuncionarioV1(1518)
# func.__salario = 4000 
print(func.get_salario())

print(func.salario)

func.salario = 1700 
print(func.set_salario(1980))
print(func.salario)
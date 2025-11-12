class FuncionarioV2:
    def __init__(self, salario):
        self.__salario = salario
    
    @property
    def salario(self):
        return self.__salario
    
    def movimentacao_salarial(self, percentual):
        if percentual < 0:
            raise ValueError("Percentual de aumento deve ser positivo.")
        self.__salario = self.__salario * (1 + percentual / 100)
    
    


func = FuncionarioV2(2000)
func.movimentacao_salarial(10)
print(func.salario)


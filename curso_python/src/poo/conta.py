# Exemplo Simples: Conta Bancária
# Imagine que você tem uma classe ContaBancaria que representa uma conta bancária com saldo, titular, e métodos para depositar e sacar.
class ContaBancaria:
    def __init__(self,titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__numero_secreto = 123456
    
    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de {valor} realizado.")
    
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print(f"Saque de {valor} realizado.")
        else:
            print("Saldo insuficiente.")
    
    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self._saldo:.2f}")

conta1 = ContaBancaria("Flavio", 1000)
conta1.depositar(500)
conta1.mostrar_saldo()
conta1.sacar(200)
conta1.mostrar_saldo()

# Tentativas de acesso externo
print(f"Acesso público: {conta1.titular}")
print(f"Acesso protegido (funciona, mas evite): {conta1._saldo}")
# print(f"Acesso privado (erro): {conta1.__numero_secreto}") # Isso gera erro
print(f"Acesso privado (Name Mangling): {conta1._ContaBancaria__numero_secreto}")
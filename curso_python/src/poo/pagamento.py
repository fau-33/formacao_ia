# Exemplo Simples: Pagamento
# Imagine que você tem diferentes formas de pagamento (Cartão, Boleto, Pix). Todos eles têm um método para processar_pagamento(), mas a lógica interna é diferente para cada um.
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass
    
class PagamentoCartao(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} com cartão")
    
class PagamentoBoleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} com boleto")
    
class PagamentoPix(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} com pix")
    

pag1 = PagamentoCartao()
pag2 = PagamentoBoleto()
pag3 = PagamentoPix()

pag1.processar_pagamento(100)
pag2.processar_pagamento(200)
pag3.processar_pagamento(300)
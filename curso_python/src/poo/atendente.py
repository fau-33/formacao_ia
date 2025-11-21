from abc import ABC, abstractmethod

class Atendente(ABC):
    @abstractmethod
    def saudacao(self):
        pass

class AtendentePt(Atendente):
    def saudacao(self):
        return "Bom dia!"

class AtendenteEn(Atendente):
    def saudacao(self):
        return "Good morning!"
        
class AtendenteJp(Atendente):
    def saudacao(self):
        return "おはようございます!"
    

a1 = AtendenteEn()
print(a1.saudacao())

a2 = AtendentePt()
print(a2.saudacao())

a3 = AtendenteJp()
print(a3.saudacao())

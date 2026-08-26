from operacao import Operacao

class Elevado(Operacao):
    simbolo = "?"
    nome = "potencia"
    
    def calcular(self):
        return self.a ** self.b
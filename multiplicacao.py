from operacao import Operacao
class Multi(Operacao):
    simbolo = "x"
    nome = "Multiplicar"
    
    def calcular(self):
        return self.a * self.b
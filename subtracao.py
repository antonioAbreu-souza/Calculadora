from operacao import Operacao

class subtracao(Operacao):
    simbolo = "-"
    nome = "Subtrair"
    
    def calcular(self):
        return self.a - self.b
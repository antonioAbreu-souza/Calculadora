from operacao import Operacao
class divisao(Operacao):
    simbolo = "÷"
    nome = "dividir"
    
    def calcular(self):
        return self.a / self.b
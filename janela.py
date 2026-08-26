import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from soma import Soma
from divisao import divisao
from exponenciacao import Elevado
from multiplicacao import Multi
from subtracao import subtracao


OPERACOES = {

    "+": Soma,
    "*": Multi,
    "/": divisao,
    "-":subtracao,
    "**": Elevado
    
    
}


ESTILO = """
QWidget {
    background-color: #f2f2f2;
    font-family: Segoe UI, Arial;
}
QLabel#visor {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 28px;
    padding: 12px;
}
QLabel#conta {
    color: #777777;
    font-size: 13px;
    padding-left: 4px;
}
QPushButton {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 18px;
    min-width: 56px;
    min-height: 48px;
}
QPushButton:hover {
    background-color: #e8e8e8;
}
QPushButton:pressed {
    background-color: #dcdcdc;
}
"""

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        
        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False
        
        self.conta = QLabel("")
        self.conta.setObjectName("conta")
        self.conta.setAlignment(Qt.AlignRight)
        
        self.visor = QLabel(self.digitado)
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignRight)
        grade = QGridLayout()
        botoes = [
            {"c",0, 0},{"<",0, 1},{"+/-",0, 2},{"/",0, 3},
            {"7",1, 0},{"8",1, 1},{"9",1, 2},{"*",1, 3},
            {"4",2, 0},{"5",2, 1},{"6",2, 2},{"-",2, 3},
            {"1",3, 0},{"2",3, 1},{"3",3, 2},{"+",3, 3},
            {"0",4, 0} ,{",",4, 1}, {"=", 4, 2}
               
        ]
        for texto, linha, coluna, in botoes:
            botao = QPushButton(texto)
            largura = 2 if texto == "=" else 1
            grade.addWidget(botao,linha,coluna,1,largura)
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.conta)
        layout.addLayout(grade)
        self.setLayout(layout)
        def criar_acao(self,texto):
            pass #1 linha
        
        def clicar(self,texto):
            pass #0123456789 operacoes
        
        def digitar(self,tecla):
            pass #self.digitado = "0"
        def valo_do_visor(self):
            pass #return float(.......)
        def mostrar(self, numero):
            pass # self.digitado = f"{numero:g}"
        
        def escolher_operacao(self,simbolo):
            pass #@Calcular
        
        def calcular(self):
            pass #divisionbyzero self.primeiro = None...
        def limpar(self):
            pass #Voltar tudo como esta la no começo, todas as variaveis
        def apagar(self):
            pass #Verificar o digitado e atribuir o valor 
        def inverter_sinal(self):
            pass #Inverter o sinal

def main():
        app = QApplication(sys.argv)
        app.setStyleSheet(ESTILO)
        janela = Calculadora()
        janela.show()
        sys.exit(app.exec())     
    
if __name__ == "__main__":
    main()
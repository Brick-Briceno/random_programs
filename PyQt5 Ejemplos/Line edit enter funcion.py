import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lineaTexto = QLineEdit(self)
        self.lineaTexto.setPlaceholderText("Presiona Enter")

        # Conectar la señal returnPressed con la función correspondiente
        self.lineaTexto.returnPressed.connect(self.ejecutarAccion)

        layout = QVBoxLayout()
        layout.addWidget(self.lineaTexto)
        self.setLayout(layout)

    def ejecutarAccion(self):
        texto = self.lineaTexto.text()
        print(f"Texto ingresado: {texto}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    app.exec_()

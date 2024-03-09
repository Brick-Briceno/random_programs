import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout, QPushButton

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(6)  # Establece el número de dígitos que se mostrarán
        self.lcd.display(0)  # Inicialmente, muestra el valor 0

        self.button = QPushButton('Actualizar LCD', self)
        self.button.clicked.connect(self.actualizarLCD)

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def actualizarLCD(self):
        # Obtén el valor desde algún lugar, por ejemplo, un cuadro de texto
        valor = 42  # Puedes obtener este valor desde un QLineEdit u otra fuente de datos

        # Actualiza el valor en el QLCDNumber
        self.lcd.display(valor)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

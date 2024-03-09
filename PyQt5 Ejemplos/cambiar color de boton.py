import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.boton = QPushButton('Haz clic en mí', self)
        self.boton.clicked.connect(self.cambiarColor)

        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def cambiarColor(self):
        # Cambiar el color del botón cuando se hace clic en él
        self.boton.setStyleSheet("background-color: red; color: white;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

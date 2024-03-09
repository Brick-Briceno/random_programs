import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Crear un QCheckBox
        self.checkbox = QCheckBox('Marcar/Desmarcar', self)

        # Conectar la señal de estado cambiado con la función correspondiente
        self.checkbox.stateChanged.connect(self.mostrarEstado)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    def mostrarEstado(self, state):
        print(state)
        # Verificar si el QCheckBox está marcado o no
        if state == 2:  # 2 significa que está marcado
            print('CheckBox está marcado')
        else:
            print('CheckBox está desmarcado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

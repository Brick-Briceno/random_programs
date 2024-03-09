from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QMainWindow
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tabla = QTableWidget(5, 3)
        self.tabla.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.tabla)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("Tabla con Evento de Enter")
        self.show()

    def keyPressEvent(self, evento):
        if evento.key() == 16777220:  # 16777220 es el código de Enter
            celda_actual = self.tabla.currentItem()
            if celda_actual:
                fila = celda_actual.row()
                columna = celda_actual.column()
                print(f"Celda en la fila {fila}, columna {columna}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())

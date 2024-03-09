from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
import sys

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tabla = QTableWidget(5, 3)
        layout.addWidget(self.tabla)

        # Botón para cambiar el tamaño de la tabla
        btn_cambiar_tamano = QPushButton('Cambiar Tamaño de la Tabla', self)
        btn_cambiar_tamano.clicked.connect(self.cambiarTamanoTabla)
        layout.addWidget(btn_cambiar_tamano)

        self.setLayout(layout)
        self.setWindowTitle("Tabla Dinámica")
        self.show()

    def cambiarTamanoTabla(self):
        # Cambiar el número de filas y columnas cuando se hace clic en el botón
        nuevas_filas = 7
        nuevas_columnas = 4

        self.tabla.setRowCount(nuevas_filas)
        self.tabla.setColumnCount(nuevas_columnas)

        # Agregar datos a las nuevas celdas (opcional)
        for i in range(nuevas_filas):
            for j in range(nuevas_columnas):
                item = QTableWidgetItem(f"Fila {i}, Col {j}")
                self.tabla.setItem(i, j, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(app.exec_())

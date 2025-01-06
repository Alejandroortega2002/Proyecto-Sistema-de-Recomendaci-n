from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class Vista_principal(QMainWindow):
    """
    Clase que define la interfaz gráfica de la pantalla inicial o menú principal de la aplicación.

    Esta clase hereda de QMainWindow y crea una ventana con:
    - Un título.
    - Tres botones de opciones para acceder a diferentes funcionalidades de la aplicación.
    """

    def __init__(self):
        """
        Constructor de la clase Vista_principal.
        Inicializa los elementos de la interfaz gráfica y su disposición.
        """
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Pantalla Inicial")  # Título de la ventana
        self.setGeometry(100, 100, 600, 400)  # Tamaño y posición de la ventana

        # Widget central para contener los elementos de la interfaz
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal para organizar los elementos en vertical
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignCenter)  # Centrar los elementos en la ventana

        # Estilo general de la ventana y sus elementos
        self.setStyleSheet("""
            QWidget {
                background-color: #2E86C1;  /* Fondo azul */
            }
            QLabel {
                color: white;              /* Texto blanco */
            }
            QPushButton {
                background-color: #3498DB; /* Azul para botones */
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980B9; /* Azul más oscuro al pasar el mouse */
            }
        """)

        # Crear los elementos de la interfaz
        # Título de la pantalla principal
        self.label = QLabel("Menú Principal")
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")  # Estilo del texto
        self.label.setAlignment(Qt.AlignCenter)  # Alinear el texto en el centro
        self.layout.addWidget(self.label)  # Agregar el título al layout

        # Botón de Opción 1
        self.option1_button = QPushButton("Opción 1")
        self.layout.addWidget(self.option1_button)  # Agregar el botón al layout

        # Botón de Opción 2
        self.option2_button = QPushButton("Opción 2")
        self.layout.addWidget(self.option2_button)  # Agregar el botón al layout

        # Botón de Opción 3
        self.option3_button = QPushButton("Opción 3")
        self.layout.addWidget(self.option3_button)  # Agregar el botón al layout

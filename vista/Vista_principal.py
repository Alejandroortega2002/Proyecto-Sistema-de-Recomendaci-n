from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class Vista_principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pantalla Inicial")
        self.setGeometry(100, 100, 600, 400)

        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignCenter)

        # Estilo general
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

        # Título
        self.label = QLabel("Menú Principal")
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Botones del menú
        self.option1_button = QPushButton("Opción 1")
        self.layout.addWidget(self.option1_button)

        self.option2_button = QPushButton("Opción 2")
        self.layout.addWidget(self.option2_button)

        self.option3_button = QPushButton("Opción 3")
        self.layout.addWidget(self.option3_button)
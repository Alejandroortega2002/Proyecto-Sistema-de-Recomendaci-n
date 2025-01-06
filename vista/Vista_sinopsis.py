from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QDesktopWidget
from PyQt5.QtCore import Qt

class Vista_sinopsis(QMainWindow):
    """
    Clase que define la interfaz gráfica para mostrar la sinopsis de una película.

    Esta clase hereda de QMainWindow y crea una ventana con:
    - Un área para mostrar la información detallada de la película.
    - Un botón para volver a la pantalla principal.
    """

    def __init__(self):
        """
        Constructor de la clase Vista_sinopsis.
        Inicializa los elementos de la interfaz gráfica y su disposición.
        """
        super().__init__()
        self.setWindowTitle("Sinopsis de la Película")
        self.resize(1200, 800)  # Ajustar el tamaño para que coincida con la pantalla principal

        # Aplicar el estilo CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #2E86C1;  /* Fondo azul */
            }
            QLabel {
                color: white;              /* Texto blanco */
            }
            QLineEdit, QTextEdit {
                background-color: #F0F0F0; /* Fondo gris claro */
                border: 1px solid #DADADA;
                border-radius: 5px;
                padding: 10px;
                font-size: 24px;           /* Fuente más grande */
            }
            QPushButton {
                background-color: #3498DB; /* Azul para botones */
                color: white;
                font-size: 24px;           /* Fuente más grande */
                padding: 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980B9; /* Azul más oscuro al pasar el mouse */
            }
        """)

        # Centrar la ventana en la pantalla
        self.center_window()

        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout = QVBoxLayout(self.central_widget)

        # Título de la película
        self.title_label = QLabel("Título de la Película")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Sinopsis de la película
        self.synopsis_text = QTextEdit()
        self.synopsis_text.setReadOnly(True)
        self.layout.addWidget(self.synopsis_text)

        # Botón para volver a la pantalla principal
        self.back_button = QPushButton("Volver")
        self.layout.addWidget(self.back_button)

    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def conectar_volver(self, funcion):
        """
        Conecta el botón de volver con la función proporcionada.
        """
        self.back_button.clicked.connect(funcion)

    def mostrar_informacion_pelicula(self, titulo, sinopsis):
        """
        Muestra la información detallada de la película.
        """
        self.title_label.setText(titulo)
        self.synopsis_text.setText(sinopsis)
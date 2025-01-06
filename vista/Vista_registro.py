from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class Vista_registro(QMainWindow):
    """
    Clase que define la interfaz gráfica para el registro de nuevos usuarios en la aplicación.

    Esta clase hereda de QMainWindow y crea una ventana con:
    - Un campo para el nombre de usuario.
    - Un campo para la contraseña.
    - Botones para registrar un usuario y navegar de vuelta al inicio de sesión.
    """

    def __init__(self):
        """
        Constructor de la clase Vista_registro.
        Inicializa los elementos de la interfaz gráfica y su disposición.
        """
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Registrarse")  # Título de la ventana
        self.setGeometry(100, 100, 400, 300)  # Tamaño y posición de la ventana

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
            QLineEdit {
                background-color: #F0F0F0; /* Fondo gris claro */
                border: 1px solid #DADADA;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
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
        # Título de la ventana de registro
        self.label = QLabel("Registrarse")
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")  # Estilo del texto
        self.label.setAlignment(Qt.AlignCenter)  # Alinear el texto en el centro
        self.layout.addWidget(self.label)  # Agregar el título al layout

        # Campo de entrada para el nombre de usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("username")  # Texto que aparece por defecto
        self.layout.addWidget(self.username_input)  # Agregar el campo al layout

        # Campo de entrada para la contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("password")  # Texto que aparece por defecto
        self.password_input.setEchoMode(QLineEdit.Password)  # Ocultar el texto ingresado
        self.layout.addWidget(self.password_input)  # Agregar el campo al layout

        # Botón para registrar al usuario
        self.register_button = QPushButton("Registrarse")
        self.layout.addWidget(self.register_button)  # Agregar el botón al layout

        # Botón para volver al inicio de sesión
        self.login_button = QPushButton("Iniciar Sesión")
        self.layout.addWidget(self.login_button)  # Agregar el botón al layout

    def show_alert(self, message):
        """
        Muestra una alerta de error con un mensaje personalizado.

        :param message: Texto del mensaje que se mostrará en la alerta.
        """
        # Crear una instancia de QMessageBox para mostrar la alerta
        alert = QMessageBox()
        alert.setWindowTitle("Error")  # Título de la alerta
        alert.setText(message)  # Texto del mensaje de error
        alert.setIcon(QMessageBox.Warning)  # Tipo de ícono (advertencia)
        alert.exec_()  # Mostrar la alerta

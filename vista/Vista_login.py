from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt

class Vista_login(QMainWindow):
    """
    Clase que define la interfaz gráfica para el inicio de sesión de la aplicación.

    Esta clase hereda de QMainWindow y crea una ventana con:
    - Un campo para el nombre de usuario.
    - Un campo para la contraseña.
    - Botones para iniciar sesión y registrarse.
    """

    def __init__(self):
        """
        Constructor de la clase Vista_login.
        Inicializa los elementos de la interfaz gráfica y su disposición.
        """
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Iniciar Sesión")  # Título de la ventana
        self.resize(1200, 800)  # Tamaño de la ventana (mucho más grande)

        # Centrar la ventana en la pantalla
        self.center_window()

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

        # Crear los elementos de la interfaz
        # Título
        self.label = QLabel("Login")
        self.label.setStyleSheet("font-size: 48px; font-weight: bold;")  # Estilo del texto (más grande)
        self.label.setAlignment(Qt.AlignCenter)  # Alinear el texto en el centro
        self.layout.addWidget(self.label)  # Agregar el título al layout

        # Campo de entrada para el nombre de usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Nombre de usuario")  # Texto que aparece por defecto
        self.layout.addWidget(self.username_input)  # Agregar el campo al layout

        # Campo de entrada para la contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")  # Texto que aparece por defecto
        self.password_input.setEchoMode(QLineEdit.Password)  # Ocultar el texto ingresado
        self.layout.addWidget(self.password_input)  # Agregar el campo al layout

        # Botón para iniciar sesión
        self.login_button = QPushButton("Iniciar Sesión")
        self.layout.addWidget(self.login_button)  # Agregar el botón al layout

        # Botón para registrarse
        self.register_button = QPushButton("Registrarse")
        self.layout.addWidget(self.register_button)  # Agregar el botón al layout

    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        frame_geometry = self.frameGeometry()  # Obtiene el tamaño y posición de la ventana
        screen_center = QDesktopWidget().availableGeometry().center()  # Obtiene el centro de la pantalla
        frame_geometry.moveCenter(screen_center)  # Mueve el centro de la ventana al centro de la pantalla
        self.move(frame_geometry.topLeft())  # Ajusta la posición de la ventana según el centro calculado

    def show_alert(self, message):
        """
        Muestra una alerta de error con un mensaje personalizado.

        :param message: Texto del mensaje que se mostrará en la alerta.
        """
        alert = QMessageBox()  # Crear una instancia de QMessageBox
        alert.setWindowTitle("Error")  # Título de la alerta
        alert.setText(message)  # Texto del mensaje de error
        alert.setIcon(QMessageBox.Warning)  # Tipo de ícono (advertencia)
        alert.exec_()  # Mostrar la alerta


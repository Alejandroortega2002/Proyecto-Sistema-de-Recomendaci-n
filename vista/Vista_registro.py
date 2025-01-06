from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class Vista_registro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrarse")
        self.setGeometry(100, 100, 400, 300)

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

        # Título
        self.label = QLabel("Registrarse")
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Campo de nombre de usuario
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("username")
        self.layout.addWidget(self.username_input)

        # Campo de contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        # Botón de registro
        self.register_button = QPushButton("Registrarse")
        self.layout.addWidget(self.register_button)

        # Botón de inicio de sesión
        self.login_button = QPushButton("Iniciar Sesión")
        self.layout.addWidget(self.login_button)

    def show_alert(self, message):
        alert = QMessageBox()
        alert.setWindowTitle("Error")
        alert.setText(message)
        alert.setIcon(QMessageBox.Warning)
        alert.exec_()
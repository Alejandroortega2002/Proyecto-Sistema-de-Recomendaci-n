from PyQt5.QtWidgets import QApplication
from vista.Vista_login import Vista_login
from controlador.Controlador_peliculas import Controlador_peliculas
from modelo.Modelo_usuarios import Modelo_usuarios

class Controlador_login:
    def __init__(self, app, usuarios_model, register_controller):
        self.app = app
        self.usuarios_model = usuarios_model
        self.login_view = Vista_login()
        self.register_controller = register_controller
        self.intentos_fallidos = 0

        self.login_view.login_button.clicked.connect(self.login)
        self.login_view.register_button.clicked.connect(self.show_register_view)

    def login(self):
        nombre = self.login_view.username_input.text()
        contraseña = self.login_view.password_input.text()
        if self.usuarios_model.inicio_sesion(nombre, contraseña):
            print("Inicio de sesión exitoso.")
            self.show_principal_view()
        else:
            self.intentos_fallidos += 1
            if self.intentos_fallidos >= 3:
                self.login_view.show_alert("Demasiados intentos fallidos. La aplicación se cerrará.")
                self.app.quit()
            else:
                self.login_view.show_alert("Nombre de usuario o contraseña incorrectos.")

    def show_register_view(self):
        self.register_controller.run()
        self.login_view.close()

    def show_principal_view(self):
        self.principal_controller = Controlador_peliculas(self.app)
        self.principal_controller.run()
        self.login_view.close()

    def run(self):
        self.login_view.show()
        self.app.exec_()
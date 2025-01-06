from PyQt5.QtWidgets import QApplication
from vista.Vista_registro import Vista_registro
from modelo.Modelo_usuarios import Modelo_usuarios

class Controlador_registro:
    def __init__(self, app, usuarios_model, login_controller):
        self.app = app
        self.usuarios_model = usuarios_model
        self.register_view = Vista_registro()
        self.login_controller = login_controller

        self.register_view.register_button.clicked.connect(self.register_user)
        self.register_view.login_button.clicked.connect(self.show_login_view)

    def register_user(self):
        nombre = self.register_view.username_input.text()
        contraseña = self.register_view.password_input.text()
        if nombre and contraseña:
            self.usuarios_model.registrar_usuario(nombre, contraseña)
            self.show_login_view()
        else:
            self.register_view.show_alert("Por favor, complete todos los campos.")

    def show_login_view(self):
        self.login_controller.run()
        self.register_view.close()

    def run(self):
        self.register_view.show()
        self.app.exec_()
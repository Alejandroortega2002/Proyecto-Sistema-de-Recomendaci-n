from PyQt5.QtWidgets import QApplication
from controlador.Controlador_login import Controlador_login
from controlador.Controlador_registro import Controlador_registro
from modelo.Modelo_usuarios import Modelo_usuarios

if __name__ == "__main__":
    """
    Punto de entrada de la aplicación.
    """
    app = QApplication([])
    usuarios_model = Modelo_usuarios()

    # Inicializar los controladores con las dependencias necesarias
    login_controller = Controlador_login(app, usuarios_model, None)
    register_controller = Controlador_registro(app, usuarios_model, login_controller)

    # Establecer la referencia cruzada
    login_controller.register_controller = register_controller

    # Ejecutar la aplicación
    login_controller.run()
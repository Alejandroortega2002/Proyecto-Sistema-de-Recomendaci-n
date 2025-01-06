from PyQt5.QtWidgets import QApplication
from vista.Vista_registro import Vista_registro
from modelo.Modelo_usuarios import Modelo_usuarios

class Controlador_registro:
    """
    Clase que controla el flujo de la aplicación relacionado con el registro de nuevos usuarios.
    Se encarga de conectar la vista de registro y el modelo de usuarios, y de gestionar la lógica de registro.
    """

    def __init__(self, app, usuarios_model, login_controller):
        """
        Constructor de la clase Controlador_registro.

        :param app: Instancia de QApplication para manejar el ciclo de vida de la aplicación.
        :param usuarios_model: Instancia del modelo de usuarios para registrar nuevos usuarios.
        :param login_controller: Controlador para manejar la navegación de vuelta a la vista de inicio de sesión.
        """
        self.app = app  # Referencia a la instancia de QApplication.
        self.usuarios_model = usuarios_model  # Modelo para manejar la lógica de usuarios.
        self.register_view = Vista_registro()  # Vista de registro de nuevos usuarios.
        self.login_controller = login_controller  # Controlador de inicio de sesión.

        # Conectar el botón de registro a la función de registro de usuarios.
        self.register_view.register_button.clicked.connect(self.register_user)

        # Conectar el botón de inicio de sesión a la función que muestra la vista de inicio de sesión.
        self.register_view.login_button.clicked.connect(self.show_login_view)

    def register_user(self):
        """
        Maneja la lógica de registro de usuarios al presionar el botón 'Registrar'.

        Este método:
        - Obtiene los datos ingresados en los campos de la vista de registro.
        - Valida que los campos no estén vacíos.
        - Registra al usuario en el modelo y redirige a la vista de inicio de sesión en caso de éxito.
        - Muestra un mensaje de error si los campos están incompletos.
        """
        # Obtiene el nombre de usuario y la contraseña ingresados por el usuario.
        nombre = self.register_view.username_input.text()
        contraseña = self.register_view.password_input.text()

        if nombre and contraseña:
            # Si ambos campos están llenos, registra al usuario.
            self.usuarios_model.registrar_usuario(nombre, contraseña)
            self.show_login_view()  # Redirige a la vista de inicio de sesión.
        else:
            # Si los campos están vacíos, muestra una alerta al usuario.
            self.register_view.show_alert("Por favor, complete todos los campos.")

    def show_login_view(self):
        """
        Muestra la vista de inicio de sesión al presionar el botón 'Iniciar Sesión'.

        Este método:
        - Ejecuta el controlador de inicio de sesión.
        - Cierra la ventana de registro.
        """
        self.login_controller.run()  # Ejecuta el controlador de inicio de sesión.
        self.register_view.close()  # Cierra la ventana de registro.

    def run(self):
        """
        Ejecuta la aplicación mostrando la vista de registro.

        Este método:
        - Muestra la ventana de registro.
        - Ejecuta el ciclo de eventos principal de PyQt.
        """
        self.register_view.show()  # Muestra la ventana de registro.
        self.app.exec_()  # Ejecuta el ciclo de eventos principal de PyQt.

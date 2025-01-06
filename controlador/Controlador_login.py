from PyQt5.QtWidgets import QApplication
from vista.Vista_login import Vista_login
from vista.Vista_principal import Vista_principal
from modelo.Modelo_usuarios import Modelo_usuarios

class Controlador_login:
    """
    Clase que controla el flujo de la aplicación relacionado con el inicio de sesión.
    Se encarga de conectar la vista de inicio de sesión, el modelo de usuarios y las demás vistas necesarias.
    """

    def __init__(self, app, usuarios_model, register_controller):
        """
        Constructor de la clase Controlador_login.

        :param app: Instancia de QApplication para manejar el ciclo de vida de la aplicación.
        :param usuarios_model: Instancia del modelo de usuarios para validar credenciales.
        :param register_controller: Controlador para manejar el registro de nuevos usuarios.
        """
        self.app = app  # Referencia a la instancia de QApplication.
        self.usuarios_model = usuarios_model  # Modelo de usuarios para manejar la lógica de autenticación.
        self.login_view = Vista_login()  # Vista de inicio de sesión.
        self.register_controller = register_controller  # Controlador para manejar la vista de registro.
        self.intentos_fallidos = 0  # Contador de intentos fallidos de inicio de sesión.

        # Conectar el botón de inicio de sesión a la función de inicio de sesión.
        self.login_view.login_button.clicked.connect(self.login)

        # Conectar el botón de registro a la función que muestra la vista de registro.
        self.login_view.register_button.clicked.connect(self.show_register_view)

    def login(self):
        """
        Maneja la lógica de inicio de sesión cuando se presiona el botón de 'Iniciar Sesión'.

        Este método:
        - Obtiene el nombre de usuario y la contraseña ingresados en la vista.
        - Verifica las credenciales utilizando el modelo de usuarios.
        - Muestra la vista principal en caso de éxito.
        - Muestra un mensaje de error o cierra la aplicación tras varios intentos fallidos.
        """
        nombre = self.login_view.username_input.text()  # Obtiene el nombre de usuario del campo de entrada.
        contraseña = self.login_view.password_input.text()  # Obtiene la contraseña del campo de entrada.

        if self.usuarios_model.inicio_sesion(nombre, contraseña):
            # Inicio de sesión exitoso.
            print("Inicio de sesión exitoso.")
            self.show_initial_view()  # Muestra la vista principal.
        else:
            # Incrementa el contador de intentos fallidos.
            self.intentos_fallidos += 1

            if self.intentos_fallidos >= 3:
                # Si se superan los intentos permitidos, muestra una alerta y cierra la aplicación.
                self.login_view.show_alert("Demasiados intentos fallidos. La aplicación se cerrará.")
                self.app.quit()
            else:
                # Muestra un mensaje de error por credenciales incorrectas.
                self.login_view.show_alert("Nombre de usuario o contraseña incorrectos.")

    def show_register_view(self):
        """
        Muestra la vista de registro al presionar el botón 'Registrarse'.

        Este método:
        - Ejecuta el controlador de registro.
        - Cierra la ventana de inicio de sesión.
        """
        self.register_controller.run()  # Ejecuta la vista de registro.
        self.login_view.close()  # Cierra la ventana de inicio de sesión.

    def show_initial_view(self):
        """
        Muestra la vista principal de la aplicación tras un inicio de sesión exitoso.

        Este método:
        - Crea una instancia de la vista principal.
        - Cierra la ventana de inicio de sesión.
        """
        self.initial_view = Vista_principal()  # Crea una instancia de la vista principal.
        self.initial_view.show()  # Muestra la vista principal.
        self.login_view.close()  # Cierra la ventana de inicio de sesión.

    def run(self):
        """
        Ejecuta la aplicación mostrando la vista de inicio de sesión.

        Este método:
        - Muestra la ventana de inicio de sesión.
        - Ejecuta el ciclo de eventos principal de la aplicación.
        """
        self.login_view.show()  # Muestra la ventana de inicio de sesión.
        self.app.exec_()  # Ejecuta el ciclo de eventos principal de PyQt.

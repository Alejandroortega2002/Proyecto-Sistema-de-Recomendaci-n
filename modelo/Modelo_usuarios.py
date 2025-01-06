import pandas as pd

class Modelo_usuarios:
    """
    Clase que gestiona los usuarios en el sistema, incluyendo el inicio de sesión y el registro.
    Utiliza un archivo CSV para almacenar los datos de los usuarios.
    """

    def __init__(self):
        """
        Constructor de la clase Modelo_usuarios.
        Inicializa el nombre del archivo CSV donde se almacenan los datos de los usuarios.
        """
        self.archivo_csv = 'usuarios.csv'  # Nombre del archivo CSV que almacena los datos de los usuarios.

    def inicio_sesion(self, nombre, contraseña):
        """
        Verifica si las credenciales proporcionadas (nombre y contraseña) son válidas.

        :param nombre: El nombre de usuario ingresado por el usuario.
        :param contraseña: La contraseña ingresada por el usuario.
        :return: True si el usuario existe y las credenciales son correctas, False de lo contrario.
        """
        try:
            # Lee el archivo CSV con los datos de los usuarios.
            df_usuarios = pd.read_csv(self.archivo_csv)

            # Asegurarse de que las columnas 'Nombre de usuario' y 'Contraseña' sean de tipo string.
            df_usuarios['Nombre de usuario'] = df_usuarios['Nombre de usuario'].astype(str)
            df_usuarios['Contraseña'] = df_usuarios['Contraseña'].astype(str)

            # Limpiar los espacios en blanco de los nombres de las columnas.
            df_usuarios.columns = df_usuarios.columns.str.strip()

            # Verificar si el nombre de usuario y la contraseña coinciden con algún registro en el CSV.
            usuario_valido = df_usuarios[
                (df_usuarios['Nombre de usuario'].str.strip() == nombre.strip()) &
                (df_usuarios['Contraseña'].str.strip() == contraseña.strip())
            ]

            # Retorna True si se encontró un usuario válido, False si no.
            return not usuario_valido.empty

        except FileNotFoundError:
            # Maneja el caso en que el archivo CSV no exista.
            print("El archivo de usuarios no existe. No se pueden verificar los datos.")
            return False

    def registrar_usuario(self, nombre, contraseña):
        """
        Registra un nuevo usuario en el sistema y lo guarda en el archivo CSV.

        :param nombre: El nombre de usuario del nuevo usuario.
        :param contraseña: La contraseña del nuevo usuario.
        """
        # Crea un DataFrame con los datos del nuevo usuario.
        nuevo_usuario = pd.DataFrame([[nombre, contraseña]], columns=['Nombre de usuario', 'Contraseña'])

        try:
            # Intenta leer el archivo CSV existente.
            df_usuarios = pd.read_csv(self.archivo_csv)

            # Añade el nuevo usuario al DataFrame existente.
            df_usuarios = pd.concat([df_usuarios, nuevo_usuario], ignore_index=True)
        except FileNotFoundError:
            # Si el archivo no existe, crea un nuevo DataFrame con el usuario actual.
            df_usuarios = nuevo_usuario

        # Guarda el DataFrame actualizado en el archivo CSV.
        df_usuarios.to_csv(self.archivo_csv, index=False)
        print("Usuario registrado correctamente.")

import pandas as pd

class Modelo_usuarios:
    def __init__(self):
        self.archivo_csv = 'usuarios.csv'

    def inicio_sesion(self, nombre, contraseña):
        try:
            df_usuarios = pd.read_csv(self.archivo_csv)

            # Asegurarse de que las columnas 'Nombre' y 'Contraseña' sean del tipo string
            df_usuarios['Nombre de usuario'] = df_usuarios['Nombre de usuario'].astype(str)
            df_usuarios['Contraseña'] = df_usuarios['Contraseña'].astype(str)

            # Limpiar los espacios en blanco alrededor de las columnas y los datos
            df_usuarios.columns = df_usuarios.columns.str.strip()

            # Verificar si el nombre y la contraseña coinciden
            usuario_valido = df_usuarios[(df_usuarios['Nombre de usuario'].str.strip() == nombre.strip()) &
                                         (df_usuarios['Contraseña'].str.strip() == contraseña.strip())]

            return not usuario_valido.empty

        except FileNotFoundError:
            print("El archivo de usuarios no existe. No se pueden verificar los datos.")
            return False

    def registrar_usuario(self, nombre, contraseña):
        nuevo_usuario = pd.DataFrame([[nombre, contraseña]], columns=['Nombre de usuario', 'Contraseña'])
        try:
            df_usuarios = pd.read_csv(self.archivo_csv)
            df_usuarios = pd.concat([df_usuarios, nuevo_usuario], ignore_index=True)
        except FileNotFoundError:
            df_usuarios = nuevo_usuario

        df_usuarios.to_csv(self.archivo_csv, index=False)
        print("Usuario registrado correctamente.")
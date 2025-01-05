import pandas as pd

def inicio_sesion(nombre, contraseña):
    archivo_csv = 'usuarios.csv'
    try:
        df_usuarios = pd.read_csv(archivo_csv)

        # Asegurarse de que las columnas 'Nombre' y 'Contraseña' sean del tipo string
        df_usuarios['Nombre de usuario'] = df_usuarios['Nombre de usuario'].astype(str)
        df_usuarios['Contraseña'] = df_usuarios['Contraseña'].astype(str)

        # Limpiar los espacios en blanco alrededor de las columnas y los datos
        df_usuarios.columns = df_usuarios.columns.str.strip()

        # Verificar si el nombre y la contraseña coinciden
        usuario_valido = df_usuarios[(df_usuarios['Nombre de usuario'].str.strip() == nombre.strip()) &
                                     (df_usuarios['Contraseña'].str.strip() == contraseña.strip())]

        if not usuario_valido.empty:
            print("Inicio de sesión exitoso.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    except FileNotFoundError:
        print("El archivo de usuarios no existe. No se pueden verificar los datos.")

def registrar_usuario(nombre, contraseña):
    archivo_csv = 'usuarios.csv'

    nuevo_usuario = pd.DataFrame([[nombre, contraseña]], columns=['Nombre de usuario', 'Contraseña'])
    df_usuarios = pd.read_csv(archivo_csv)

    df_usuarios = pd.concat([df_usuarios, nuevo_usuario], ignore_index=True)

    df_usuarios.to_csv(archivo_csv, index=False)

    print("Usuario registrado correctamente.")

if __name__ == "__main__":
     menu = True
     while menu:
         eleccion = input('Que desea hacer: iniciar sesion o registrarse')
         if eleccion == 'iniciar sesion':
             nombre_inicio = input('Ingrese el nombre de ususario: ')
             contraseña = input('Ingrese la contraseña')
             inicio_sesion(nombre_inicio, contraseña)
             menu = True
         elif eleccion == 'registrarse':
             nombre_registrar = input('Ingrese el nombre de usuario: ')
             contraseña_registrar = input('Ingrese su contraseña: ')
             registrar_usuario(nombre_registrar, contraseña_registrar)
             menu = True
         elif eleccion == 'salir':
             menu = False
         else:
             print('Opcion no valida')
             menu = True

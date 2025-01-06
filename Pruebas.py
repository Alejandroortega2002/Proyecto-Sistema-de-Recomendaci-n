import pandas as pd
import ast

# Cargar los archivos CSV
file_path_peliculas = 'peliculas_final.csv'
file_path_usuarios = 'usuarios.csv'

peliculas_df = pd.read_csv(file_path_peliculas)
usuarios_df = pd.read_csv(file_path_usuarios)


def votaciones(NombrePelicula, puntuacion, usuarios_df, username):
    if username in usuarios_df["Nombre de usuario"].values:
        # Si el usuario ya tiene una fila, obtenemos las votaciones actuales
        usuario_row = usuarios_df[usuarios_df["Nombre de usuario"] == username].iloc[0]

        # Convertir la columna 'votaciones' a una lista (si no es None)
        if pd.isna(usuario_row["votaciones"]):
            votaciones_usuario = []
        else:
            votaciones_usuario = ast.literal_eval(usuario_row["votaciones"])

        # Buscar si la película ya está en las votaciones del usuario
        pelicula_existente = next((v for v in votaciones_usuario if v['title'] == NombrePelicula), None)

        if pelicula_existente:
            # Si la película ya está votada, actualizamos la puntuación
            pelicula_existente['rating'] = puntuacion
        else:
            # Si no está, agregamos la nueva película y la puntuación
            votaciones_usuario.append({"title": NombrePelicula, "rating": puntuacion})

        # Actualizamos solo la columna 'votaciones' del usuario
        usuarios_df.loc[usuarios_df["Nombre de usuario"] == username, "votaciones"] = str(votaciones_usuario)
    else:
        # Si el usuario no existe, agregamos una nueva fila para el usuario
        nuevas_votaciones = [{"title": NombrePelicula, "rating": puntuacion}]
        nuevas_filas = pd.DataFrame([{"Nombre de usuario": username, "votaciones": str(nuevas_votaciones)}])

        # Concatenar la nueva fila al DataFrame de usuarios
        usuarios_df = pd.concat([usuarios_df, nuevas_filas], ignore_index=True)

    # Asegurarse de que las columnas no numéricas (como la contraseña) no se conviertan a números
    usuarios_df["Contraseña"] = usuarios_df["Contraseña"].astype(str)

    # Guardamos el DataFrame actualizado en el archivo CSV
    usuarios_df.to_csv(file_path_usuarios, index=False)
    print(f"Votación guardada para el usuario '{username}' para la película '{NombrePelicula}' con puntuación {puntuacion}.")

# Ejemplo de uso:
votaciones("Titanic", 5, usuarios_df, "Miguel")

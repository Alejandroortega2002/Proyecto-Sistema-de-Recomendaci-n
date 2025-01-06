
import pandas as pd

class Modelo_peliculas:
    def __init__(self):
        self.file_path = 'peliculas_final.csv'
        self.peliculas_df = pd.read_csv(self.file_path)

    def sacar_peliculas(self, nombre_pelicula):
        resultado = self.peliculas_df[self.peliculas_df['title'].str.contains(nombre_pelicula, case=False, na=False)]
        if resultado.empty:
            return f"No se encontró la película: {nombre_pelicula}"

        columnas_necesarias = ['title', 'synopsis', 'people_score', 'critic_score', 'type', 'link']
        datos_relevantes = resultado[columnas_necesarias]

        return datos_relevantes

    def peliculas_azar(self):
        muestra = self.peliculas_df.sample(n=12)
        return muestra[['title']].values.tolist()

    def votaciones(self, NombrePelicula, puntuacion, username):
        # Comprobar si el usuario ya existe en el DataFrame de usuarios
        if username in self.usuarios_df["Nombre de usuario"].values:
            # Si el usuario tiene una fila, obtenemos las votaciones actuales
            usuario_row = self.usuarios_df[self.usuarios_df["Nombre de usuario"] == username].iloc[0]

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
            self.usuarios_df.loc[self.usuarios_df["Nombre de usuario"] == username, "votaciones"] = str(votaciones_usuario)
        else:
            # Si el usuario no existe, agregamos una nueva fila para el usuario
            nuevas_votaciones = [{"title": NombrePelicula, "rating": puntuacion}]
            nuevas_filas = pd.DataFrame([{"Nombre de usuario": username, "votaciones": str(nuevas_votaciones)}])

            # Concatenar la nueva fila al DataFrame de usuarios
            self.usuarios_df = pd.concat([self.usuarios_df, nuevas_filas], ignore_index=True)

        # Asegurarse de que las columnas no numéricas (como la contraseña) no se conviertan a números
        self.usuarios_df["Contraseña"] = self.usuarios_df["Contraseña"].astype(str)

        # Guardamos el DataFrame actualizado en el archivo CSV
        self.usuarios_df.to_csv(self.file_path_usuarios, index=False)
        print( f"Votación guardada para el usuario '{username}' para la película '{NombrePelicula}' con puntuación {puntuacion}.")

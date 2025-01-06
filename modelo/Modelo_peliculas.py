
import pandas as pd
import ast

class Modelo_peliculas:

    def __init__(self):
        self.file_path_peliculas = 'peliculas_final.csv'
        self.file_path_usuarios = 'usuarios.csv'
        self.peliculas_df = pd.read_csv(self.file_path_peliculas)
        self.usuarios_df = pd.read_csv(self.file_path_usuarios)

    def sacar_peliculas(self, nombre_pelicula):
        resultado = self.peliculas_df[self.peliculas_df['title'].str.contains(nombre_pelicula, case=False, na=False)]
        if resultado.empty:
            return f"No se encontró la película: {nombre_pelicula}"

        columnas_necesarias = ['title', 'synopsis', 'people_score', 'critic_score', 'type', 'link']
        datos_relevantes = resultado[columnas_necesarias]

        return datos_relevantes

    def peliculas_azar(self):
        muestra = self.peliculas_df.sample(n=12, random_state=123)
        return muestra[['title', 'Imagen']].values.tolist()

    def votaciones(self, NombrePelicula, puntuacion, username):
        if username in self.usuarios_df["Nombre de usuario"].values:
            usuario_row = self.usuarios_df[self.usuarios_df["Nombre de usuario"] == username].iloc[0]
            if pd.isna(usuario_row["votaciones"]):
                votaciones_usuario = []
            else:
                votaciones_usuario = ast.literal_eval(usuario_row["votaciones"])

            pelicula_existente = next((v for v in votaciones_usuario if v['title'] == NombrePelicula), None)

            if pelicula_existente:
                pelicula_existente['rating'] = puntuacion
            else:
                votaciones_usuario.append({"title": NombrePelicula, "rating": puntuacion})

            self.usuarios_df.loc[self.usuarios_df["Nombre de usuario"] == username, "votaciones"] = str(
                votaciones_usuario)
        else:
            nuevas_votaciones = [{"title": NombrePelicula, "rating": puntuacion}]
            nuevas_filas = pd.DataFrame([{"Nombre de usuario": username, "votaciones": str(nuevas_votaciones)}])
            self.usuarios_df = pd.concat([self.usuarios_df, nuevas_filas], ignore_index=True)

        self.usuarios_df.to_csv(self.file_path_usuarios, index=False)
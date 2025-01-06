
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
        muestra = self.peliculas_df.sample(n=12, random_state=123)
        return muestra[['title']].values.tolist()
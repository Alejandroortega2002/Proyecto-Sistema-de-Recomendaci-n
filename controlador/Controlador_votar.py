from PyQt5.QtWidgets import QApplication
from vista.Vista_votar import Vista_votar
from modelo.Modelo_peliculas import Modelo_peliculas

class Controlador_votar:
    def __init__(self, app):
        self.app = app
        self.peliculas_model = Modelo_peliculas()
        self.votar_view = Vista_votar()

        self.votar_view.conectar_busqueda(self.buscar_peliculas)
        self.votar_view.conectar_votar(self.votar_pelicula)
        self.cargar_peliculas_azar()

    def buscar_peliculas(self):
        nombre_pelicula = self.votar_view.search_input.text()
        resultados = self.peliculas_model.sacar_peliculas(nombre_pelicula)
        self.votar_view.mostrar_resultados(resultados)

    def cargar_peliculas_azar(self):
        peliculas = self.peliculas_model.peliculas_azar()
        self.votar_view.mostrar_peliculas_azar(peliculas)

    def votar_pelicula(self):
        nombre_pelicula = self.votar_view.selected_movie_input.text()
        pelicula = self.peliculas_model.sacar_peliculas(nombre_pelicula)
        if isinstance(pelicula, str):
            self.votar_view.show_alert(pelicula)
        else:
            pelicula = pelicula.iloc[0].to_dict()
            # Aquí puedes agregar la lógica para votar por la película
            print(f"Votando por la película: {pelicula['title']}")

    def run(self):
        self.votar_view.show()
        self.app.exec_()
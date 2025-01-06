from PyQt5.QtWidgets import QApplication
from vista.Vista_principal import Vista_principal
from modelo.Modelo_peliculas import Modelo_peliculas


class Controlador_peliculas:
    def __init__(self, app):
        self.app = app
        self.peliculas_model = Modelo_peliculas()
        self.principal_view = Vista_principal()

        self.principal_view.conectar_busqueda(self.buscar_peliculas)
        self.principal_view.conectar_votacion(self.votaciones)
        self.cargar_peliculas_azar()

    def buscar_peliculas(self):
        nombre_pelicula = self.principal_view.search_input.text()
        resultados = self.peliculas_model.sacar_peliculas(nombre_pelicula)
        self.principal_view.mostrar_resultados(resultados)

    def cargar_peliculas_azar(self):
        peliculas = self.peliculas_model.peliculas_azar()
        self.principal_view.mostrar_peliculas_azar(peliculas)

    def votaciones(self):
        nombre_pelicula = self.principal_view.pelicula_input.text()
        puntuacion = int(self.principal_view.puntuacion_input.text())
        username = self.principal_view.username_input.text()

        self.peliculas_model.votaciones(nombre_pelicula, puntuacion, username)
        self.principal_view.mostrar_mensaje(f"Votación guardada para {username} en la película '{nombre_pelicula}'")

    def run(self):
        self.principal_view.show()
        self.app.exec_()

from PyQt5.QtWidgets import QApplication
from vista.Vista_principal import Vista_principal
from modelo.Modelo_peliculas import Modelo_peliculas
from controlador.Controlador_sinopsis import Controlador_sinopsis
from controlador.Controlador_votar import Controlador_votar

class Controlador_peliculas:
    def __init__(self, app):
        self.app = app
        self.peliculas_model = Modelo_peliculas()
        self.principal_view = Vista_principal(self.go_to_main_view, self.go_to_vote_view, self.go_to_recommendations_view)

        self.principal_view.conectar_busqueda(self.buscar_peliculas)
        self.principal_view.conectar_ver_sinopsis(self.ver_sinopsis)
        self.cargar_peliculas_azar()

    def buscar_peliculas(self):
        nombre_pelicula = self.principal_view.search_input.text()
        resultados = self.peliculas_model.sacar_peliculas(nombre_pelicula)
        self.principal_view.mostrar_resultados(resultados)

    def cargar_peliculas_azar(self):
        peliculas = self.peliculas_model.peliculas_azar()
        self.principal_view.mostrar_peliculas_azar(peliculas)

    def ver_sinopsis(self):
        nombre_pelicula = self.principal_view.search_input.text()
        pelicula = self.peliculas_model.sacar_peliculas(nombre_pelicula)
        if isinstance(pelicula, str):
            self.principal_view.show_alert(pelicula)
        else:
            pelicula = pelicula.iloc[0].to_dict()
            self.sinopsis_controller = Controlador_sinopsis(pelicula)
            self.sinopsis_controller.run()

    def go_to_main_view(self):
        """
        Implementar la lógica para ir a la vista principal.
        """
        print("Navegando a la vista principal...")

    def go_to_vote_view(self):
        """
        Implementar la lógica para ir a la vista de votar.
        """
        self.votar_controller = Controlador_votar(self.app)
        self.votar_controller.run()

    def go_to_recommendations_view(self):
        """
        Implementar la lógica para ir a la vista de recomendaciones.
        """
        print("Navegando a la vista de recomendaciones...")

    def run(self):
        self.principal_view.show()
        self.app.exec_()
from PyQt5.QtWidgets import QApplication
from vista.Vista_sinopsis import Vista_sinopsis

class Controlador_sinopsis:
    def __init__(self, app, pelicula):
        self.app = app
        self.pelicula = pelicula
        self.sinopsis_view = Vista_sinopsis()

        self.sinopsis_view.conectar_volver(self.volver)
        self.mostrar_informacion_pelicula()

    def mostrar_informacion_pelicula(self):
        titulo = self.pelicula['title']
        sinopsis = self.pelicula['synopsis']
        self.sinopsis_view.mostrar_informacion_pelicula(titulo, sinopsis)

    def volver(self):
        self.sinopsis_view.close()

    def run(self):
        self.sinopsis_view.show()
        self.app.exec_()
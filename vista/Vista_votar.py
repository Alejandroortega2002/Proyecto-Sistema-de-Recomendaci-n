from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QMenuBar, QAction, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtCore import Qt

class Vista_votar(QMainWindow):
    """
    Clase que define la interfaz gráfica para votar por una película.

    Esta clase hereda de QMainWindow y crea una ventana con:
    - Un área para buscar películas.
    - Un área para mostrar los resultados de la búsqueda.
    - Un menú con opciones para navegar a otras vistas.
    """

    def __init__(self):
        """
        Constructor de la clase Vista_votar.
        Inicializa los elementos de la interfaz gráfica y su disposición.
        """
        super().__init__()
        self.setWindowTitle("Sistema de Recomendación de Películas - Votar")
        self.resize(1200, 800)  # Ajustar el tamaño para que coincida con la pantalla principal

        # Aplicar el estilo CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #2E86C1;  /* Fondo azul */
            }
            QLabel {
                color: white;              /* Texto blanco */
            }
            QLineEdit, QTextEdit {
                background-color: #F0F0F0; /* Fondo gris claro */
                border: 1px solid #DADADA;
                border-radius: 5px;
                padding: 10px;
                font-size: 24px;           /* Fuente más grande */
            }
            QPushButton {
                background-color: #3498DB; /* Azul para botones */
                color: white;
                font-size: 24px;           /* Fuente más grande */
                padding: 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980B9; /* Azul más oscuro al pasar el mouse */
            }
        """)

        # Centrar la ventana en la pantalla
        self.center_window()

        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout = QVBoxLayout(self.central_widget)

        # Barra de menú
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Menú de navegación
        self.menu_navegacion = self.menu_bar.addMenu("Navegación")

        # Acción para ir a la vista de votar
        self.action_votar = QAction("Votar", self)
        self.menu_navegacion.addAction(self.action_votar)

        # Área de búsqueda
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar película...")
        self.layout.addWidget(self.search_input)

        # Botón de búsqueda
        self.search_button = QPushButton("Buscar")
        self.layout.addWidget(self.search_button)

        # Lista de resultados de búsqueda
        self.results_list = QListWidget()
        self.layout.addWidget(self.results_list)

        # Botón para votar
        self.vote_button = QPushButton("Votar")
        self.layout.addWidget(self.vote_button)

    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def conectar_busqueda(self, funcion):
        """
        Conecta el botón de búsqueda con la función proporcionada.
        """
        self.search_button.clicked.connect(funcion)

    def conectar_votar(self, funcion):
        """
        Conecta el botón de votar con la función proporcionada.
        """
        self.vote_button.clicked.connect(funcion)

    def mostrar_resultados(self, resultados):
        """
        Muestra los resultados de la búsqueda en la lista de resultados.
        """
        self.results_list.clear()
        for resultado in resultados:
            self.results_list.addItem(resultado)

    def mostrar_peliculas_azar(self, peliculas):
        """
        Muestra una lista de películas al azar en la lista de resultados.
        """
        self.results_list.clear()
        for pelicula in peliculas:
            self.results_list.addItem(pelicula)

    def show_alert(self, mensaje):
        """
        Muestra una alerta con el mensaje proporcionado.
        """
        alert = QMessageBox()
        alert.setText(mensaje)
        alert.exec_()
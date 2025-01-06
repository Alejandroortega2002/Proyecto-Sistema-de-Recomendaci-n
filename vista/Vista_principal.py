from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QListWidgetItem, QDesktopWidget
from PyQt5.QtCore import Qt

class Vista_principal(QMainWindow):
    """
    Clase que define la interfaz gráfica para la pantalla principal de la aplicación.

    Esta clase hereda de QMainWindow y crea una ventana con:
    - Un campo de búsqueda para el título de la película.
    - Un botón para realizar la búsqueda.
    - Un área para mostrar los resultados de la búsqueda.
    - Un campo de texto editable para el nombre de la película seleccionada.
    - Un botón para ver la sinopsis de la película seleccionada.
    """

    def __init__(self):
        """
        Constructor de la clase Vista_principal.
        Inicializa los elementos de la interfaz gráfica y su disposición.
        """
        super().__init__()
        self.setWindowTitle("Buscador de Películas")
        self.resize(1200, 800)

        # Aplicar el estilo CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #2E86C1;  /* Fondo azul */
            }
            QLabel {
                color: white;              /* Texto blanco */
            }
            QLineEdit {
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
            QListWidget {
                background-color: #F0F0F0; /* Fondo gris claro */
                border: 1px solid #DADADA;
                border-radius: 5px;
                font-size: 24px;           /* Fuente más grande */
            }
        """)

        # Centrar la ventana en la pantalla
        self.center_window()

        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout = QVBoxLayout(self.central_widget)

        # Título
        self.label = QLabel("Buscador de Películas")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Campo de búsqueda
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Ingrese el título de la película...")
        self.layout.addWidget(self.search_input)

        # Botón de búsqueda
        self.search_button = QPushButton("Buscar")
        self.layout.addWidget(self.search_button)

        # Lista de resultados
        self.results_list = QListWidget()
        self.layout.addWidget(self.results_list)
        self.results_list.itemClicked.connect(self.actualizar_pelicula_seleccionada)

        # Campo de texto editable para el nombre de la película seleccionada
        self.selected_movie_input = QLineEdit()
        self.selected_movie_input.setPlaceholderText("Película seleccionada...")
        self.layout.addWidget(self.selected_movie_input)

        # Botón para ver la sinopsis
        self.view_synopsis_button = QPushButton("Ver Sinopsis")
        self.layout.addWidget(self.view_synopsis_button)

    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        frame_geometry = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        self.move(frame_geometry.topLeft())

    def show_alert(self, message):
        """
        Muestra una alerta con el mensaje proporcionado.
        """
        alert = QMessageBox()
        alert.setWindowTitle("Error")
        alert.setText(message)
        alert.setIcon(QMessageBox.Warning)
        alert.exec_()

    def conectar_busqueda(self, funcion):
        """
        Conecta el botón de búsqueda con la función proporcionada.
        """
        self.search_button.clicked.connect(funcion)

    def conectar_ver_sinopsis(self, funcion):
        """
        Conecta el botón de ver sinopsis con la función proporcionada.
        """
        self.view_synopsis_button.clicked.connect(funcion)

    def mostrar_resultados(self, resultados):
        """
        Muestra los resultados de la búsqueda en la lista de resultados.
        """
        self.results_list.clear()
        if isinstance(resultados, str):
            self.show_alert(resultados)
        else:
            for _, row in resultados.iterrows():
                item_text = f"{row['title']}"
                item = QListWidgetItem(item_text)
                self.results_list.addItem(item)

    def mostrar_peliculas_azar(self, peliculas):
        """
        Muestra las películas aleatorias en la lista de resultados.
        """
        self.results_list.clear()
        for pelicula in peliculas:
            item_text = f"{pelicula[0]}"
            item = QListWidgetItem(item_text)
            self.results_list.addItem(item)

    def actualizar_pelicula_seleccionada(self, item):
        """
        Actualiza el campo de texto editable con el nombre de la película seleccionada.
        """
        self.selected_movie_input.setText(item.text().split(" - ")[0])
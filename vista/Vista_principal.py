from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QListWidgetItem, QDesktopWidget
from PyQt5.QtCore import Qt

class Vista_principal(QMainWindow):
    """
    Clase que define la interfaz gráfica para la pantalla principal de la aplicación.

    Esta clase hereda de QMainWindow y crea una ventana con:
    - Un campo de búsqueda para el título de la película.
    - Un botón para realizar la búsqueda.
    - Un área para mostrar los resultados de la búsqueda.
    """

    def __init__(self):
        """
        Constructor de la clase Vista_principal.
        Inicializa los elementos de la interfaz gráfica y su disposición.
        """
        super().__init__()
        self.setWindowTitle("Buscador de Películas")
        self.resize(1200, 800)

        # Centrar la ventana en la pantalla
        self.center_window()

        # Widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout principal
        self.layout = QVBoxLayout(self.central_widget)

        # Título
        self.label = QLabel("Buscador de Películas")
        self.label.setStyleSheet("font-size: 36px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        # Campo de búsqueda
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Ingrese el título de la película...")
        self.search_input.setStyleSheet("font-size: 18px; padding: 10px;")
        self.layout.addWidget(self.search_input)

        # Botón de búsqueda
        self.search_button = QPushButton("Buscar")
        self.search_button.setStyleSheet("font-size: 18px; padding: 10px;")
        self.layout.addWidget(self.search_button)

        # Lista de resultados
        self.results_list = QListWidget()
        self.results_list.setStyleSheet("font-size: 18px;")
        self.layout.addWidget(self.results_list)

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

    def mostrar_resultados(self, resultados):
        """
        Muestra los resultados de la búsqueda en la lista de resultados.
        """
        self.results_list.clear()
        if isinstance(resultados, str):
            self.show_alert(resultados)
        else:
            for _, row in resultados.iterrows():
                item_text = f"{row['title']} - {row['synopsis']}"
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
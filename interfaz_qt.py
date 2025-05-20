import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QLabel
from PyQt5.QtCore import Qt

from procesamiento import Partida
from arbol import ArbolPartida

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx

class VisualizadorArbol(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualizador de Partidas SAN")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.instruccion = QLabel("Escribe la partida en notación SAN:")
        layout.addWidget(self.instruccion)

        self.entrada = QTextEdit()
        layout.addWidget(self.entrada)

        self.boton = QPushButton("Validar y Generar Árbol")
        self.boton.clicked.connect(self.procesar_partida)
        layout.addWidget(self.boton)

        self.canvas = FigureCanvas(Figure())
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def procesar_partida(self):
        texto = self.entrada.toPlainText().strip()
        self.canvas.figure.clear()
        try:
            partida = Partida(texto)
            arbol = ArbolPartida(partida)
            QMessageBox.information(self, "Éxito", "Partida válida. Mostrando árbol.")
            self.dibujar_arbol(arbol)
        except ValueError as e:
            QMessageBox.critical(self, "Error de Validación", str(e))

    def dibujar_arbol(self, arbol):
        G = nx.DiGraph()
        etiquetas = {}

        def agregar_nodos(nodo, padre_id=None, contador=[0]):
            if nodo is None:
                return
            nodo_id = contador[0]
            etiquetas[nodo_id] = nodo.valor
            G.add_node(nodo_id)
            if padre_id is not None:
                G.add_edge(padre_id, nodo_id)
            contador[0] += 1
            agregar_nodos(nodo.izquierda, nodo_id, contador)
            agregar_nodos(nodo.derecha, nodo_id, contador)

        agregar_nodos(arbol.raiz)

      
        pos = nx.spring_layout(G)

        ax = self.canvas.figure.add_subplot(111)
        ax.clear()
        nx.draw(G, pos, ax=ax, with_labels=True, labels=etiquetas,
                node_color="lightblue", node_size=1500, font_size=9, arrows=False)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VisualizadorArbol()
    ventana.show()
    sys.exit(app.exec_())

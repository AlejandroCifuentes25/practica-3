class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  # Blanca
        self.derecha = None    # Negra

class ArbolPartida:
    def __init__(self, partida):
        self.raiz = NodoArbol("Partida")
        self.construir_arbol(partida.turnos)

    def construir_arbol(self, turnos):
        nodo_actual = self.raiz
        for turno in turnos:
            nodo_izq = NodoArbol(turno.blanca.texto)
            nodo_der = NodoArbol(turno.negra.texto if turno.negra else "—")
            nodo_actual.izquierda = nodo_izq
            nodo_actual.derecha = nodo_der
            nodo_actual = nodo_izq  # Continua a partir del hijo izquierdo para representar intercalado

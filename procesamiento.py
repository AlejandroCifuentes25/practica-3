from validacion import ParserSAN
from validacion import Movimiento
class Turno:
    def __init__(self, numero, blanca, negra=None):
        self.numero = numero
        self.blanca = Movimiento(blanca)
        self.negra = Movimiento(negra) if negra else None

class Partida:
    def __init__(self, texto_partida):
        self.turnos = []
        self.parser = ParserSAN()
        self.parsear_partida(texto_partida)

    def parsear_partida(self, texto):
        tokens = texto.split()
        i = 0
        while i < len(tokens):
            if '.' in tokens[i]:
                num_turno = tokens[i].replace('.', '')
                jugada_blanca = tokens[i + 1]
                jugada_negra = tokens[i + 2] if (i + 2 < len(tokens) and '.' not in tokens[i + 2]) else None

                if not self.parser.es_valida(jugada_blanca):
                    raise ValueError(f"Error en turno {num_turno}: jugada blanca inválida '{jugada_blanca}'")
                if jugada_negra and not self.parser.es_valida(jugada_negra):
                    raise ValueError(f"Error en turno {num_turno}: jugada negra inválida '{jugada_negra}'")

                self.turnos.append(Turno(num_turno, jugada_blanca, jugada_negra))
                i += 3 if jugada_negra else 2
            else:
                i += 1

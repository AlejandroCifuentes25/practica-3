from procesamiento import Partida
from validacion import ParserSAN
from arbol import ArbolPartida

import re

if __name__ == "__main__":
    texto = """e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3"""
    
    try:
        partida = Partida(texto)
        arbol = ArbolPartida(partida)
        print("Partida válida. Árbol generado.")
    except ValueError as e:
        print("Error:", e)
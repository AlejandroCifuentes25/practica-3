import re
class ParserSAN:
    def __init__(self):
        self.regex_enroque = r"^(O-O(-O)?)$"
        self.regex_pieza = r"^[KQRBN]"
        self.regex_casilla = r"[a-h][1-8]"
        self.regex_captura = r"x"
        self.regex_promocion = r"(=[QRBN])?"
        self.regex_jaque = r"[\+#]?"

        # Combinaciones válidas de jugadas
        self.regex_mov_pieza = rf"^[KQRBN]([a-h1-8]?)(x)?{self.regex_casilla}{self.regex_promocion}{self.regex_jaque}$"
        self.regex_peon_avance = rf"^{self.regex_casilla}{self.regex_promocion}{self.regex_jaque}$"
        self.regex_peon_captura = rf"^[a-h]x{self.regex_casilla}{self.regex_promocion}{self.regex_jaque}$"

    def es_valida(self, movimiento):
        if re.match(self.regex_enroque, movimiento):
            return True
        if re.match(self.regex_mov_pieza, movimiento):
            return True
        if re.match(self.regex_peon_avance, movimiento):
            return True
        if re.match(self.regex_peon_captura, movimiento):
            return True
        return False
class Movimiento:
    def __init__(self, texto):
        self.texto = texto

    def __str__(self):
        return self.texto
class token:
    def __init__(self,lexema:str, linea:int,columna:int,tipo:str):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
    def imprimir_token(self):
        print(self.lexema, self.tipo )
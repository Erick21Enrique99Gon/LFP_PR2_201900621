class error:
    def __init__(self,descripcion:str,linea:int,columna:int):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
    
    def imprimir(self):
        print(self.descripcion,str(self.line),str(self.columna))
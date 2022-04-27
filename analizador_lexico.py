from token import token
from error import error
from prettytable import PrettyTable

class analizador_lexico:
    def __init__(self):
        self.lista_de_Tokens = []
        self.lista_de_Errores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0

    def agregar_error(self,caracter:str,linea:int,columna:int):
        self.lista_de_Errores.append(error(caracter,linea,columna))
        self.buffer=''
        
    
    def agregar_token(self,lexema:str,linea:int,columna:int,tipo:str):
        self.lista_de_Tokens.append(token(lexema,linea,columna,tipo))
        self.buffer= ''
    
    def e0(self,caracter:str):
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter == "\"":
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter=="<":
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<SIGNO MENOR QUE>")
        elif caracter=="-":
            self.estado = 11
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<GUION INICIO DE BANDERAS>")

        elif caracter == ' ':
            self.columna += 1
        elif caracter == '&':
            print("Finalizacion de analizador")    
        else:
            self.columna +=1
            self.agregar_error("Caracter desconocido: "+caracter,self.linea,self.columna)

    def e1(self,caracter:str):
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        else:
            if self.buffer == "RESULTADO":
                self.agregar_token(self.buffer, self.linea, self.columna, "<RESULTADO>")
                self.estado = 0
                self.i -=1
            elif self.buffer == "VS":
                self.agregar_token(self.buffer, self.linea, self.columna, "VS")
                self.estado = 0
                self.i -=1
            elif self.buffer == "TEMPORADA":
                self.agregar_token(self.buffer, self.linea, self.columna, "<TEMPORADA>")
                self.estado = 0
                self.i -=1
            elif self.buffer == "JORNADA":
                self.agregar_token(self.buffer, self.linea, self.columna, "<JORNADA>")
                self.estado = 0
                self.i -=1
            elif self.buffer == "GOLES":
                self.agregar_token(self.buffer, self.linea, self.columna, "<GOLES>")
                self.estado = 0
                self.i -=1
            elif self.buffer in ["LOCAL","VISITANTE","TOTAL"]:
                self.agregar_token(self.buffer, self.linea, self.columna, "<CONDICION>")
                self.estado = 0
                self.i -=1
            
            elif self.buffer == "TABLA":
                self.agregar_token(self.buffer, self.linea, self.columna, "<TABLA>")
                self.estado = 0
                self.i -=1
            elif self.buffer == "PARTIDOS":
                self.agregar_token(self.buffer, self.linea, self.columna, "<PARTIDOS>")
                self.estado = 0
                self.i -=1
            elif self.buffer == "TOP":
                self.agregar_token(self.buffer, self.linea, self.columna, "<TOP>")
                self.estado = 0
                self.i -=1
            elif self.buffer in ["SUPERIOR","INFERIOR"]:
                self.agregar_token(self.buffer, self.linea, self.columna, "<CONDICION>")
                self.estado = 0
                self.i -=1
            elif self.buffer == "ADIOS":
                self.agregar_token(self.buffer, self.linea, self.columna, "ADIOS")
                self.estado = 0
                self.i -=1
            else:
                self.estado = 0
                self.i -=1
                self.agregar_error("Palabra desconocido: "+self.buffer,self.linea,self.columna)
    
    def e2(self,caracter:str):
        if caracter != "\"":
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        else:
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<TEXTO>")
            self.estado = 0
    def e3(self,caracter:str):
        if caracter.isdigit():
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(self.buffer, self.linea, self.columna, "<NUMERO>")
            self.estado = 0
            self.i -=1
    
    def e4(self,caracter:str):
        self.agregar_token(self.buffer, self.linea, self.columna, "<NUMERO>")
        self.estado = 0
        self.i -=1
    
    def e6(self,caracter:str):
        if caracter.isdigit():
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 0
            self.i -=1
            self.agregar_error("Cadena desconocida: "+self.buffer,self.linea,self.columna) 
    def e7(self,caracter:str):
        if caracter.isdigit():
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 0
            self.i -=1
            self.agregar_error("Cadena desconocida: "+self.buffer,self.linea,self.columna) 
    def e8(self,caracter:str):
        if caracter.isdigit():
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 0
            self.i -=1
            self.agregar_error("Cadena desconocida: "+self.buffer,self.linea,self.columna) 
    def e9(self,caracter:str):
        if caracter.isdigit():
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 0
            self.i -=1
            self.agregar_error("Cadena desconocida: "+self.buffer,self.linea,self.columna) 
    
    def e10(self,caracter:str):
        self.agregar_token(self.buffer, self.linea, self.columna, "<AÑO>")
        self.estado = 0
        if caracter == "-":
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<GUION>")
        elif caracter == ">":
            self.estado = 0
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<SIGNO MAYOR QUE>")

    def e11(self,caracter:str):
        if caracter == "f":
            self.estado = 12
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<BANDERA>")
        elif caracter == "n":
            self.estado = 13
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<BANDERA>")
        elif caracter == "j":
            self.estado = 14
            self.buffer += caracter
            self.columna += 1
        else:
            self.estado = 0
            self.i -=1
            self.agregar_error("Caracter desconocido: "+self.buffer,self.linea,self.columna) 

    def e12(self,caracter:str):
        if caracter.isalpha() or caracter.isdigit():
            self.estado = 12
            self.buffer += caracter
            self.columna += 1
        elif caracter == '_':
            self.estado = 12
            self.buffer += caracter
            self.columna += 1
        elif caracter == ' ':
            self.columna +=1
        else:
            self.agregar_token(self.buffer, self.linea, self.columna, "<TEXTO>")
            self.estado = 0
            self.i -=1

    def e13(self,caracter:str):
        if caracter.isdigit():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(self.buffer, self.linea, self.columna, "<NUMERO>")
            self.estado = 0
            self.i -=1
    def e14(self,caracter:str):
        if caracter in ["i","f"]:
            self.buffer += caracter
            self.columna += 1
            self.agregar_token(self.buffer, self.linea, self.columna, "<BANDERA>")
            self.estado = 0
        else:
            self.estado = 0
            self.i -=1
            self.agregar_error("Cadena desconocida: "+self.buffer,self.linea,self.columna) 

    def analizar(self, cadena:str):
        self.lista_de_Errores = []
        self.lista_de_Tokens = []
        self.i = 0
        cadena+='&'
        while self.i < cadena.__len__():
            if self.estado == 0:
                self.e0(cadena[self.i])
            elif self.estado == 1:
                self.e1(cadena[self.i])
            elif self.estado == 2:
                self.e2(cadena[self.i])
            elif self.estado == 3:
                self.e3(cadena[self.i])
            elif self.estado == 4:
                self.e4(cadena[self.i])
            elif self.estado == 6:
                self.e6(cadena[self.i])
            elif self.estado == 7:
                self.e7(cadena[self.i])
            elif self.estado == 8:
                self.e8(cadena[self.i])
            elif self.estado == 9:
                self.e9(cadena[self.i])
            elif self.estado == 10:
                self.e10(cadena[self.i])
            elif self.estado == 11:
                self.e11(cadena[self.i])
            elif self.estado == 12:
                self.e12(cadena[self.i])
            elif self.estado == 13:
                self.e13(cadena[self.i])
            elif self.estado == 14:
                self.e14(cadena[self.i])
            self.i += 1
    def imprimir_lista_de_tokens(self):
        x = PrettyTable()
        x.field_names = ["Descripcion","linea","columna","tipo"]

        for t in self.lista_de_Tokens:
            x.add_row([t.lexema,t.linea,t.columna,t.tipo])
        print(x)
    
    def imprimir_lista_de_error(self):
        x = PrettyTable()
        x.field_names = ["Descripcion","linea","columna"]

        for e in self.lista_de_Errores:
            x.add_row([e.descripcion,e.linea,e.columna])
        print(x)
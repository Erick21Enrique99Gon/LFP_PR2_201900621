from prettytable import PrettyTable
class analizador_sintactico:
    def __init__(self,tokens):
        self.errors = []
        self.tokens = tokens

    def agregar_error(self,obtenido,esperado):
        self.errors.append(
            '''Error SINTACTIVO:se obtubo {} se esperaba {}'''.format(obtenido,esperado)
        )
    
    def sacar_token(self):
        try:
            return self.tokens.pop(0)
        except:
            return None
    
    def observar_token(self):
        try:
            return self.tokens[0]
        except:
            return None
    
    def analizar(self):
        return self.inicio()

    def inicio(self):
        temporal =self.observar_token()
        if temporal == None:
            self.agregar_error("EOF","<RESULTADO> | <JORNADA> | <GOLES> | <TABLA> | <PARTIDOS> | <TOP> | ADIOS")
            return [-1000]
        elif temporal.tipo ==  "<RESULTADO>":
            return self.RESULTADO()
        elif temporal.tipo ==  "<JORNADA>":
            return self.JORNADA()
        elif temporal.tipo == "<GOLES>":
            return self.GOLES()
        elif temporal.tipo == "<TABLA>":
            return self.TABLA()
        elif temporal.tipo == "<PARTIDOS>":
            return self.PARTIDOS()
        else:
            self.agregar_error(temporal.tipo, "<RESULTADO> | <JORNADA> | <GOLES> | <TABLA> | <PARTIDOS> | <TOP> | ADIOS")
    
    def RESULTADO(self):
        token = self.sacar_token()
        resultado = token.lexema
        if token.tipo ==  "<RESULTADO>":
            token = self.sacar_token()
            
            if token == None:
                self.agregar_error("EOF","<TEXTO>")
            elif token.tipo == "<TEXTO>":
                texto1 = token.lexema
                token = self.sacar_token()
                
                if token == None:
                    self.agregar_error("EOF","VS")
                elif token.tipo == "VS":
                    VS = token.lexema
                    token = self.sacar_token()
                    
                    if token == None:
                        self.agregar_error("EOF","<TEXTO>")
                    elif token.tipo == "<TEXTO>":
                        texto2 = token.lexema
                        self.sacar_token()
                        self.sacar_token()
                        token = self.sacar_token()
                        
                        if token == None:
                            self.agregar_error("EOF","<AÑO>")
                        elif token.tipo == "<AÑO>":
                            año1 = token.lexema
                            self.sacar_token()
                            token = self.sacar_token()
                            
                            if token == None:
                                self.agregar_error("EOF","<AÑO>")
                            elif token.tipo == "<AÑO>":
                                año2 = token.lexema
                                return [resultado,texto1,VS,texto2,año1,año2]
                            else:
                                self.agregar_error(token.tipo,"<AÑO>")
                        else:
                            self.agregar_error(token.tipo,"<AÑO>")
                    else:
                        self.agregar_error(token.tipo,"<TEXTO>")
                else:
                    self.agregar_error(token.tipo,"VS")
            else:
                self.agregar_error(token.tipo, "<TEXTO>")
        else:
            self.agregar_error(token,tipo, "<RESULTADO>")

    def JORNADA(self):
        token = self.sacar_token()
        if token == None:
            self.agregar_error("EOF", "<JORNADA>")
        elif token.tipo == "<JORNADA>":
            jornada = token.lexema
            token = self.sacar_token()
            if token == None:
                self.agregar_error("EOF", "<NUMERO>")
            elif token.tipo == "<NUMERO>":
                numero = token.lexema
                token = self.sacar_token()
                if token == None:
                    self.agregar_error("EOF", "<TEMPORADA>")
                elif token.tipo == "<TEMPORADA>":
                    
                    self.sacar_token()
                    token = self.sacar_token()
                    if token == None:
                        self.agregar_error("EOF", "<AÑO>")
                    elif token.tipo == "<AÑO>":
                        año1 = token.lexema
                        self.sacar_token()
                        token = self.sacar_token()
                        if token == None:
                            self.agregar_error("EOF", "<AÑO>")
                        elif token.tipo == "<AÑO>":
                            año2 = token.lexema
                            self.sacar_token()
                            token = self.sacar_token()
                            if token == None:
                                return [jornada,numero,año1,año2]
                            elif token.tipo == "<GUION INICIO DE BANDERAS>":
                                self.sacar_token()
                                token = self.sacar_token()
                                if token == None:
                                    self.agregar_error("EOF", "<TEXTO>")
                                elif token.tipo =="<TEXTO>":
                                    nombre = token.lexema
                                    return [jornada,numero,año1,año2,nombre]
                                else:
                                    self.agregar_error(token.tipo, "<TEXTO>")
                            else:
                                self.agregar_error(token.tipo, "<GUION INICIO DE BANDERAS>")
                        else:
                            self.agregar_error(token.tipo, "<AÑO>")
                    else:
                        self.agregar_error(token.tipo, "<AÑO>")
                else:
                    self.agregar_error(token.tipo, "<TEMPORADA>")
            else:
                self.agregar_error(token.tipo, "<NUMERO>")
        else:
            self.agregar_error(token,tipo, "<JORNADA>")

    def GOLES(self):
        token = self.sacar_token()
        if token == None:
            self.agregar_error("EOF", "<GOLES>")
        elif token == "<GOLES>":
            goles = token.lexema
            token = self.sacar_token()
            if token == None:
                self.agregar_error("EOF", "<CONDICION>")
            elif token.tipo == "<CONDICION>":
                condicion = token.lexema
                token = self.sacar_token()
                if token == None:
                    self.agregar_error("EOF", "<TEXTO>")
                elif token.tipo == "<TEXTO>":
                    texto = token.lexema
                    token = self.sacar_token()
                    if token ==None:
                        self.agregar_error("EOF", "<TEMPORADA>")
                    elif token.tipo == "<TEMPORADA>": 
                        temporada = token.lexema
                        self.sacar_token()
                        token = self.sacar_token()
                        if token == None:
                            self.agregar_error("EOF", "<AÑO>")
                        elif token.tipo == "<AÑO>":
                            año1 = token.lexema
                            self.sacar_token()
                            token = self.sacar_token()
                            if token == None:
                                self.agregar_error("EOF", "<AÑO>")
                            elif token.tipo == "<AÑO>":
                                año2 = token.lexema
                                return [goles,condicion,texto,temporada,año1,año2]
                            else:
                                self.agregar_error(token.tipo, "<AÑO>")
                        else:
                            self.agregar_error(token.tipo, "<AÑO>")
                    else:
                        self.agregar_error(token.tipo, "<TEMPORADA>")
                else:
                    self.agregar_error(token.tipo, "<TEXTO>")
            else:
                self.agregar_error(token.tipo, "<CONDICION>")
        else:
            self.agregar_error(token.tipo, "<GOLES>")
    
    def TABLA(self):
        token = self.sacar_token()
        if token == None:
            self.agregar_error("EOF", "<TABLA>")
        elif token.tipo == "<TABLA>":
            tabla = token.lexema
            token = self.sacar_token()
                    
            if token ==None:
                self.agregar_error("EOF", "<TEMPORADA>")
            elif token.tipo == "<TEMPORADA>": 
                
                self.sacar_token()
                token = self.sacar_token()
                if token == None:
                    self.agregar_error("EOF", "<AÑO>")
                elif token.tipo == "<AÑO>":
                    año1 = token.lexema
                    self.sacar_token()
                    token = self.sacar_token()
                    if token == None:
                        self.agregar_error("EOF", "<AÑO>")
                    elif token.tipo == "<AÑO>":
                        año2 = token.lexema
                        self.sacar_token()
                        token = self.sacar_token()
                        if token == None:
                            return [tabla,año1,año2]
                        elif token.tipo == "<GUION INICIO DE BANDERAS>":
                            self.sacar_token()
                            token = self.sacar_token()
                            if token == None:
                                self.agregar_error("EOF", "<TEXTO>")
                            elif token.tipo =="<TEXTO>":
                                nombre = token.lexema
                                return [tabla,año1,año2,nombre]
                            else:
                                self.agregar_error(token.tipo, "<TEXTO>")
                        else:
                            self.agregar_error(token.tipo, "<GUION INICIO DE BANDERAS>")
                    else:
                        self.agregar_error(token.tipo, "<AÑO>")
                else:
                    self.agregar_error(token.tipo, "<AÑO>")
            else:
                self.agregar_error(token.tipo, "<TEMPORADA>")
        else:
            self.agregar_error(token.tipo, "<TABLA>")

    def PARTIDOS(self):
        token = self.sacar_token()
        if token == None:
            self.agregar_error("EOF", "<PARTIDOS>")
        elif token.tipo == "<PARTIDOS>":
            partidos = token.lexema
            token = self.sacar_token()
            if token == None:
                self.agregar_error("EOF", "<TEXTO>")
            elif token.tipo == "<TEXTO>":
                texto = token.lexema
                token = self.sacar_token()
                if token ==None:
                    self.agregar_error("EOF", "<TEMPORADA>")
                elif token.tipo == "<TEMPORADA>": 

                    self.sacar_token()
                    token = self.sacar_token()
                    if token == None:
                        self.agregar_error("EOF", "<AÑO>")
                    elif token.tipo == "<AÑO>":
                        año1 = token.lexema
                        self.sacar_token()
                        token = self.sacar_token()
                        if token == None:
                            self.agregar_error("EOF", "<AÑO>")
                        elif token.tipo == "<AÑO>":
                            año2 = token.lexema
                            self.sacar_token()
                            token = self.sacar_token()
                            if token == None:
                                return [partidos,texto,año1,año2]
                            elif token.tipo == "<GUION INICIO DE BANDERAS>":
                                token = self.sacar_token()
                                if token == None:
                                    self.agregar_error("EOF", "<BANDERA>")
                                elif token.lexema =="f":
                                    token = self.sacar_token()
                                   
                                    if token == None:
                                        self.agregar_error("EOF", "<TEXTO>")
                                    elif token.tipo == "<TEXTO>":
                                        nombre = token.lexema
                                        token = self.sacar_token()
                                        if token == None:
                                            return [partidos,texto,año1,año2,nombre]
                                        elif token.tipo ==  "<GUION INICIO DE BANDERAS>":
                                            token = self.sacar_token()
                                            if token == None:
                                                self.agregar_error("EOF", "<BANDERA>")
                                            elif token.tipo == "<BANDERA>":
                                                token = self.sacar_token()
                                                if token == None:
                                                    self.agregar_error("EOF", "<NUMERO>")
                                                elif token.tipo == "<NUMERO>":
                                                    numero1 = token.lexema
                                                    token = self.sacar_token()
                                                    if token == None:
                                                        self.agregar_error("EOF", "<GUION INICIO DE BANDERAS>")
                                                    elif token.tipo ==  "<GUION INICIO DE BANDERAS>":
                                                        token = self.sacar_token()
                                                        if token == None:
                                                            self.agregar_error("EOF", "<BANDERA>")
                                                        elif token.tipo ==  "<BANDERA>":
                                                            token = self.sacar_token()
                                                            if token == None:
                                                                self.agregar_error("EOF", "<NUMERO>")
                                                            elif token.tipo ==  "<NUMERO>":
                                                                numero2 = token.lexema
                                                                return [partidos,texto,año1,año2,nombre,numero1,numero2]
                                                            else:
                                                                self.agregar_error(token.tipo, "<NUMERO>")
                                                        else:
                                                            self.agregar_error(token.tipo, "<BANDERA>")
                                                    else:
                                                        self.agregar_error(token.tipo, "<GUION INICIO DE BANDERAS>")
                                                else:
                                                    self.agregar_error(token.tipo, "<NUMERO>")
                                            else:
                                                self.agregar_error(token.tipo, "<BANDERA>")
                                        else:
                                            self.agregar_error(token.tipo, "<GUION INICIO DE BANDERAS>")
                                    else:
                                        self.agregar_error(token.tipo, "<TEXTO>")
                                elif token.lexema =="ji":
                                    token = self.sacar_token()
                                    if token == None:
                                        self.agregar_error("EOF", "<NUMERO>")
                                    elif token.tipo == "<NUMERO>":
                                        numero1 = token.lexema
                                        token = self.sacar_token()
                                        if token == None:
                                            self.agregar_error("EOF", "<GUION INICIO DE BANDERAS>")
                                        elif token.tipo ==  "<GUION INICIO DE BANDERAS>":
                                            token = self.sacar_token()
                                            if token == None:
                                                self.agregar_error("EOF", "<BANDERA>")
                                            elif token.tipo ==  "<BANDERA>":
                                                token = self.sacar_token()
                                                if token == None:
                                                    self.agregar_error("EOF", "<NUMERO>")
                                                elif token.tipo ==  "<NUMERO>":
                                                    numero2 = token.lexema
                                                    return [partidos,texto,año1,año2,numero1,numero2]
                                                else:
                                                    self.agregar_error(token.tipo, "<NUMERO>")
                                            else:
                                                self.agregar_error(token.tipo, "<BANDERA>")
                                        else:
                                            self.agregar_error(token.tipo, "<GUION INICIO DE BANDERAS>")
                                    else:
                                        self.agregar_error(token.tipo, "<NUMERO>")
                                else:
                                    self.agregar_error(token.tipo, "<BANDERA>")
                            else:
                                self.agregar_error(token.tipo, "<GUION INICIO DE BANDERAS>")
                        else:
                            self.agregar_error(token.tipo, "<AÑO>")
                    else:
                        self.agregar_error(token.tipo, "<AÑO>")
                else:
                    self.agregar_error(token.tipo, "<TEMPORADA>")
            else:
                self.agregar_error(token.tipo, "<TEXTO>")
        else:
            self.agregar_error(token.tipo, "<PARTIDOS>")

    def imprimir_errores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errors:
            x.add_row([error_])
        print(x)            
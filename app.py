from analizador_lexico import analizador_lexico
from analizador_sintactico import analizador_sintactico
import csv
from prettytable import PrettyTable
import tkinter
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import sys

s2 = []
errores_lexicos = []
errores_semanticos = []
with open('LaLigaBot-LFP.csv',newline='',encoding="utf-8") as file_vsc:
    s = csv.reader(file_vsc,delimiter=',',quotechar='|')
    for row in s:
        s2.append(row)

class app:
    def __init__(self):
        self.errores_lexicos = []
        self.errores_semanticos = []
        self.analizador_lexico =  analizador_lexico()
        self.analizador_sintactico = analizador_sintactico()
        self.ventana1 = tkinter.Tk()
        self.scrolledtext1 = scrolledtext.ScrolledText(self.ventana1,width=100,height=30)
        self.scrolledtext1.grid(column=0,row=0,padx=10,pady=10,rowspan=6)
        self.scrolledtext1.insert("end", "BOT: Bienvenido a la liga BOT ingresar un comando"+"\n")
        self.entry1 = tkinter.Entry(self.ventana1,width=75)
        self.entry1.grid(column=0,row=6,padx=10,pady=10)
        boton_reporte_errores = tkinter.ttk.Button(self.ventana1,text="Reporte de Errores",command=self.reporte_errores)
        boton_reporte_errores.grid(column=1,row=0)
        boton_limpiar_log_errores = tkinter.ttk.Button(self.ventana1,text="Limpiar log de errores")
        boton_limpiar_log_errores.grid(column=1,row=1)
        boton_reporte_tokens = tkinter.ttk.Button(self.ventana1,text="Reporte de tokens")
        boton_reporte_tokens.grid(column=1,row=2)
        boton_limpiar_log_tokens = tkinter.ttk.Button(self.ventana1,text="Limpiar log de token")
        boton_limpiar_log_tokens.grid(column=1,row=3)
        boton_manual_usuario = tkinter.ttk.Button(self.ventana1,text="Manual de usuario")
        boton_manual_usuario.grid(column=1,row=4)
        boton_manual_tecnico = tkinter.ttk.Button(self.ventana1,text="Manual Tecnico")
        boton_manual_tecnico.grid(column=1,row=5)
        boton_enviar = tkinter.ttk.Button(self.ventana1,text="Enviar",command=self.enviar)
        boton_enviar.grid(column=1,row=6)
        self.ventana1.mainloop()
    
    def enviar(self):
        cont = self.entry1.get()
        self.scrolledtext1.insert("end", cont+"\n")
        self.entry1.delete(0, 'end')
        self.seleccionador(cont)
        

    def seleccionador(self,entrada):
        self.analizador_lexico.analizar(entrada)
        self.analizador_lexico.imprimir_lista_de_error()
        self.errores_lexicos.extend(self.analizador_lexico.lista_de_Errores)
        resultado_analizado = self.analizador_sintactico.analizar(self.analizador_lexico.lista_de_Tokens)
        self.analizador_sintactico.imprimir_errores()
        self.errores_semanticos.extend(self.analizador_sintactico.errors)
        print(resultado_analizado)
        
        if resultado_analizado == None:
            self.scrolledtext1.insert("end", "BOT: No se ingreso un comando aceptable"+"\n")
        elif resultado_analizado[0]== "RESULTADO":
            self.resultado(resultado_analizado)
        elif resultado_analizado[0]== "JORNADA":
            self.jornada(resultado_analizado)
        elif resultado_analizado[0]== "GOLES":
            self.goles(resultado_analizado)
        elif resultado_analizado[0]== "TABLA":
            self.tabla(resultado_analizado)
        elif resultado_analizado[0]== "ADIOS":
            self.adios()
        
        pass

    def resultado(self,resultado_analizado):
        arreglo_seleccion_1 =[]
        arreglo_seleccion_2 =[]
        
        for r in s2:
            if r[1]== resultado_analizado[3]+"-"+resultado_analizado[4]:
                arreglo_seleccion_1.append(r)
        
        for r in arreglo_seleccion_1:
            if r[3] == resultado_analizado[1] and r[4] == resultado_analizado[2]:
                arreglo_seleccion_2.append(r)
        
        print(arreglo_seleccion_2)
        
        if arreglo_seleccion_2 != []:
            self.scrolledtext1.insert("end", "BOT: El resultado de este partido fue de {} {} - {} {}".format(arreglo_seleccion_2[0][3],arreglo_seleccion_2[0][5],arreglo_seleccion_2[0][4],arreglo_seleccion_2[0][6])+"\n")
        else:
            self.scrolledtext1.insert("end", "BOT: comando incorrecto\n")

    def jornada(self,resultado_analizado):
        arreglo_seleccion_1 = []
        arreglo_seleccion_2 = []
        for r in s2:
            if r[1]== resultado_analizado[2]+"-"+resultado_analizado[3]:
                arreglo_seleccion_1.append(r)
        for r in arreglo_seleccion_1:
            if r[2]== resultado_analizado[1]:
                arreglo_seleccion_2.append(r)
        if arreglo_seleccion_2 != []:
            nombre = ""
            if resultado_analizado.__len__()== 5:
                nombre = resultado_analizado[4]+".html"
            else:
                nombre = 'jornada.html'

            buffer = '''<table border="1">
                                <caption>Jornada</caption>
                                <tbody>
                                <tr>
                                    <td>FECHA</td>
                                    <td>TEMPORADA</td>
                                    <td>JORNADA</td>
                                    <td>LOCAL</td>
                                    <td>VISITANTE</td>
                                    <td>LOCAL GOLES</td>
                                    <td>VISITANTE GOLES</td>
                            </tr>'''
            for r in arreglo_seleccion_2:
                buffer += '''<tr>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                            </tr>'''.format(r[0],r[1],r[2],r[3],r[4],r[5],r[6])
            
            buffer += '''</tbody>
                </table>'''
            archivo = open(nombre,'w')
            archivo.write(buffer)
            archivo.close()
            self.scrolledtext1.insert("end", "BOT: Generando archivo de resultados jornada {} temporada {}-{}\n".format(resultado_analizado[1],resultado_analizado[2],resultado_analizado[3]))
            webbrowser.open_new_tab(nombre)

        else:
            self.scrolledtext1.insert("end", "BOT: comando incorrecto\n")

    def goles(self,resultado_analizado):
        arreglo_seleccion_1 =[]
        total_goles = 0
        for r in s2:
            if r[1]== resultado_analizado[4]+"-"+resultado_analizado[5]:
                arreglo_seleccion_1.append(r)
        if arreglo_seleccion_1 != []:
            if resultado_analizado[1] == "LOCAL":
                for r in arreglo_seleccion_1:
                    if r[3]== resultado_analizado[2]:
                        total_goles += int(r[5])
                self.scrolledtext1.insert("end", "BOT: Los goles anotados por el {} en local en la temporada {}-{} fueron {}\n".format(resultado_analizado[2],resultado_analizado[4],resultado_analizado[5],total_goles))
            elif resultado_analizado[1] == "VISITANTE":
                for r in arreglo_seleccion_1:
                    if r[4]== resultado_analizado[2]:
                        total_goles += int(r[6])
                self.scrolledtext1.insert("end", "BOT: Los goles anotados por el {} en visitante en la temporada {}-{} fueron {}\n".format(resultado_analizado[2],resultado_analizado[4],resultado_analizado[5],total_goles))
            elif resultado_analizado[1] == "TOTAL":
                for r in arreglo_seleccion_1:
                    if r[4]== resultado_analizado[2]:
                        total_goles += int(r[6])
                        print(r[6])
                    elif  resultado_analizado[2] == r[3]:
                        total_goles += int(r[5])
                        print(r[5])
                    else:
                        pass
                self.scrolledtext1.insert("end", "BOT: Los goles anotados por el {} en total en la temporada {}-{} fueron {}\n".format(resultado_analizado[2],resultado_analizado[4],resultado_analizado[5],total_goles))
        else:
            self.scrolledtext1.insert("end", "BOT: comando incorrecto\n")


    def tabla(self,resultado_analizado):
        arreglo_seleccion_1 =[]
        arreglo_seleccion_2 = []
        total_goles = 0
        
        for r in s2:
            if r[1]== resultado_analizado[4]+"-"+resultado_analizado[5]:
                arreglo_seleccion_1.append(r)
        
        if arreglo_seleccion_1 != []:
            pass
        else:
            self.scrolledtext1.insert("end", "BOT: comando incorrecto\n")


    def adios(self):
        self.ventana1.quit()

    def reporte_errores(self):
        s = '''<table border="1">
                                <caption>Errores lexicos</caption>
                                <tbody>
                                <tr>
                                    <td>Descripcion</td>
                                    <td>Linea</td>
                                    <td>Columna</td>
                                </tr>'''
        
        for e in self.errores_lexicos:
            s += '''<tr>
                                    <td>{}</td>
                                    <td>{}</td>
                                    <td>{}</td>
                        </tr>'''.format(e.descripcion,str(e.linea),str(e.columna))
        
        s += '''</tbody>
                </table>'''

        a = open("Reporte errores lexicos.html",'w+')
        a.write(s)
        a.close()
        webbrowser.open_new_tab("Reporte errores lexicos.html")
        s = '''<table border="1">
                                <caption>Errores semanticos</caption>
                                <tbody>
                                <tr>
                                    <td>Descripcion</td>
                                </tr>'''
        
        for e in self.analizador_sintactico.errors:
            s += '''<tr>
                                    <td>{}</td>
                        </tr>'''.format(e)
        
        s += '''</tbody>
                </table>'''

        a = open("Reporte errores semanticos.html",'w+')
        a.write(s)
        a.close()
        webbrowser.open_new_tab("Reporte errores semanticos.html")
    
    def imprimir_lista_de_error(lista_de_Errores):
            x = PrettyTable()
            x.field_names = ["Descripcion","linea","columna"]

            for e in lista_de_Errores:
                x.add_row([e.descripcion,e.linea,e.columna])
            print(x)
    def imprimir_errores(errors):
            x = PrettyTable(errors)
            x.field_names = ["Descripcion"]
            for error_ in errors:
                x.add_row([error_])
            print(x)   

app_ventana = app()

'''
while True:
    a = analizador_lexico()
    entrada = input()
    a.analizar(entrada)
    a.imprimir_lista_de_tokens()
    a.imprimir_lista_de_error()
    errores_lexicos.extend(a.lista_de_Errores)

    if errores_lexicos != []:
        imprimir_lista_de_error(errores_lexicos)
        print(errores_lexicos.__len__())
    b = analizador_sintactico()
    print(b.analizar(a.lista_de_Tokens))
    b.imprimir_errores()
    errores_semanticos.extend(b.errors)

    if errores_semanticos !=[]:
        imprimir_errores(errores_semanticos)
        print(errores_semanticos.__len__())
'''
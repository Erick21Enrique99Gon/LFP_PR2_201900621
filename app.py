from analizador_lexico import analizador_lexico
from analizador_sintactico import analizador_sintactico
import csv
s2 = []
with open('LaLigaBot-LFP.csv',newline='',encoding="utf-8") as file_vsc:
    s = csv.reader(file_vsc,delimiter=',',quotechar='|')
    for row in s:
        s2.append(row)

while True:
    a = analizador_lexico()
    entrada = input()
    a.analizar(entrada)
    a.imprimir_lista_de_tokens()
    a.imprimir_lista_de_error()

    b = analizador_sintactico(a.lista_de_Tokens)
    print(b.analizar())
    b.imprimir_errores()
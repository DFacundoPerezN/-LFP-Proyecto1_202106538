try:
    from Backend.Operaciones import *
    from Backend.Diccionarios import *
except:
    from Operaciones import *
    from Diccionarios import *

import os

dirTXT='Graficos/ReporteGrafica.txt'
dirPNG='Graficos/ReporteGrafica.png'
dirPDF='Graficos/ReporteGrafica.pdf'

def EncontrarColorNodo(texto):
    color=''
    texto=texto[(texto.index('"Color-Fondo-Nodo":"')+20):len(texto)]
    for caracter in texto:
        if (caracter=='"'):
            break
        else:
            color+=caracter
    return color

def EncontrarColorFuente(texto):
    color=''
    texto=texto[(texto.index('"Color-Fuente-Nodo":"')+21):len(texto)]
    for caracter in texto:
        if (caracter=='"'):
            break
        else:
            color+=caracter
    return color

def EncontrarFormaNodo(texto):
    forma=''
    texto=texto[(texto.index('"Forma-Nodo":"')+14):len(texto)]
    for caracter in texto:
        if (caracter=='"'):
            break
        else:
            forma+=caracter
    return forma

def infoGrafica(texto):
    formaN=Formas[EncontrarFormaNodo(texto)]
    colorN=Colores[EncontrarColorNodo(texto)]
    colorF=colorL=Colores[EncontrarColorFuente(texto)]

    textoGrafica='digraph dot\n{\n'
    textoGrafica+='\tnode[shape='+formaN+', fontcolor='+colorL+', fillcolor='+colorN+', style=filled];\n'
    textoGrafica+='\n'

    for operacion in listaOperaciones:
        operacion : Operacion
        textoGrafica+='\t"'+ operacion.tipoOperacion +'\\n '+str(operacion.resultado)+'"\n'
        

        if operacion.numeroA!=None:
            textoGrafica+='\t"'+ operacion.tipoOperacion +'\\n '+str(operacion.resultado)+'"->'+str(operacion.numeroA)+'\n'

        if operacion.numeroB!=None:
            textoGrafica+='\t"'+ operacion.tipoOperacion +'\\n '+str(operacion.resultado)+'"->'+str(operacion.numeroB)+'\n'

    textoGrafica+='}'

    return textoGrafica
#print(infoGrafica(prueba+'"Texto":"RealizaciondeOperaciones"\n"Color-Fondo-Nodo":"Amarillo"\n"Color-Fuente-Nodo":"Rojo"\n"Forma-Nodo":"Circulo"\n}'))

def crearGrafica(ruta):
    archivo = open (ruta,'r')
    texto = archivo.read()
    archivo.close()
    
    contenido=infoGrafica(texto)

    newFile= open(dirTXT, 'w')    
    newFile.write(contenido)
    newFile.close()

    os.system("dot -Tpng "+ dirTXT +" -o "+dirPNG)
    os.system("dot -Tpdf "+ dirTXT +" -o "+dirPDF)

#crearGrafica('Archivo.lfp')
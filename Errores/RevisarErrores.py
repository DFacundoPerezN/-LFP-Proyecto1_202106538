
def revisar(ruta):
    
        archivo = open (ruta,'r')       #Se abre archivo segun la ruta indicada
        datos = archivo.read()          #Se extrae la informacion de este
        datosErrores = revisarErrores(datos)    #Devuelve si tiene errores con formato
        archivo.close()                 #cerramos ese archivo

        newFile = open ("Errores/ERRORES_202106538.json", "w")       #Creamos archivo con la ruta quemada para escribir
        newFile.write(datosErrores)                             #Escribimos los datos de los Errores
        newFile.close                                           #Cerramos el archivo
        

def revisarErrores(datos):
    info='{'

    nFila=0
    nError=0

    lineas =datos.split("\n")   #Se divide por lineas
    for linea in lineas:
            nFila=nFila+1
            nColumna =0

            for c in linea:     #se revisa caracter por caracter de la linea
                    nColumna=nColumna+1
                    
                    if not(c.isdigit()|c.isalpha() or c==" " or c == "{" or c=="}" or c == ":" or c=="," or c == "[" or c=="]" or c == "=" or c == "."or c == '"' or c == "-"):
                            nError=nError+1

                            print("Error #", nError, ". ",c, "Fila: ",nFila, "  Columna: ",nColumna)
                            if not(nError==1):
                                info+=','
                            
                                info+=formatoError(nError,c,nColumna,nFila)
    info+='}'
    if nError ==0:
           print('No hay errores')
    #print(info)
    return info                            
                                    
def formatoError(numero, lexema, columna, fila):
        text='\n\t{'
        text+='\n\t    "No.:"'+str(numero)
        text+='\n\t    "Descripcion-Token":{'
        text+='\n\t\t\t    "Lexema": '+lexema
        text+='\n\t\t\t    "Tipo": Error'
        text+='\n\t\t\t    "Columna": '+str(columna)
        text+='\n\t\t\t    "Fila": '+str(fila)
        text+='\n\t    }'
        text+='\n\t}'
        print('Errores en formato"'+text+'"')
        return text
        
        
        

def revisar(ruta):
    
        archivo = open (ruta,'r')
        datos = archivo.read()
        datosErrores = revisarErrores(datos)
        archivo.close()

        newFile = open ("ERRORES_202106538", "w")
        newFile.write(datosErrores)
        newFile.close
        

def revisarErrores(datos):
    info='{'

    nFila=0
    nError=0

    lineas =datos.split("\n")
    for linea in lineas:
            nFila=nFila+1
            nColumna =0

            for token in linea:
                    nColumna=nColumna+1
                    
                    if not(token.isdigit()|token.isalpha() or token==" " or token == "{" or token=="}" or token == ":" or token=="," or token == "[" or token=="]" or token == "=" or token == "."):
                            nError=nError+1

                            #print("Error # ", nError, ". ",token, "Fila: ",nFila, "  Columna: ",nColumna)
                            if not(nError==1):
                                    info+=','
                            
                            info=+formatoError(nError,token,nColumna,nFila)
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
        text='\n\t}'
        
        
        
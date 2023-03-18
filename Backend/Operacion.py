import EjecutarOperaciones
listaOperaciones=[]
class Operacion:
    def __init__(self, tipoOperacion , numeroA, numeroB, resultado, operadionPadre=None) -> None:
        self.operacionPadre=operadionPadre
        self.tipoOperacion = tipoOperacion
        self.numeroA = numeroA
        self.numeroB = numeroB
        self.resultado = resultado

def obtenerNumero(datos):
    numero=''
    if (datos[0]=='['): #Metodo si hay recursividad
        
        #print("datos entre corchetes: "+datos+"FIN")
        datos=obtenerEntreCorchetes(datos)
        return resultadoOperacion(datos)
    
    else:   #Metodo si solo son numeros

        for d in datos:

            if(d.isdigit())or(d=='.'):
                numero+=str(d)
            else:
                #print("break en:"+d)
                break

    numero = float(numero)
    return numero

def obtenerEntreCorchetes(texto):
    nuevo=''
    cont=pila=0
    while True:
        
        if(texto[cont]=='['):
            pila+=1
        elif(texto[cont]==']'):
            pila-=1
        cont+=1

        if(pila==0):
            break

        if(cont!=0|(len(texto)-1)):
            nuevo+=str(texto[cont])
    return nuevo

    
def ETipoOperacion(texto):
    tipo=''
    texto=texto[(texto.index('"Operacion":')+13):len(texto)]
    #print("texto para encontrar operacion: +++++"+texto+"++++++")
    for c in texto:
        if (c=='"'):
            break
        else:
            tipo+=c
    return tipo

def EV(texto,parametro):
    texto=texto[(texto.index(parametro)+9):len(texto)]
    #print("texto a buscar numero**"+texto+"**")
    v=obtenerNumero(texto)
    return v

def EV1(texto):
    return EV(texto,'"Valor1":')
def EV2(texto):
    return EV(texto,'"Valor2":')

def resultadoOperacion(text):

    tipoOp=ETipoOperacion(text)
    #print("Operacion: "+tipoOp)
    valor1=EV1(text)
    valor2=EV2(text)
    resultado =EjecutarOperaciones.hacer(tipoOp,valor1,valor2)
    print(resultado)
    return resultado

prueba= '{"Operacion":"Resta"\n"Valor1":4.5\n"Valor2":[\n"Operacion":"Potencia"\n"Valor1":10\n"Valor2":3\n]}'
print(resultadoOperacion(prueba))


'''def obtenerDatosOperacion(text : str):
    datosOp=[]   

    textInfo=text.split('\n')

    tipoOp = textInfo[1].split('"')
    tipoOp = tipoOp[4]
    datosOp.append(tipoOp)

    valor1 = textInfo[2]
    valor1 = valor1[1]
    datosOp.append(valor1)

    valor2 = textInfo[3].split(':')
    valor2 = valor2[1]
    datosOp.append(valor2)

    return datosOp'''
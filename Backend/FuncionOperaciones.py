import math

def hacer(operacion, a= None, b=None): #Metodo para todas las operaciones
    match operacion:
        case "SUMA"| "Suma":
            return a+b 
        case "RESTA" | "Resta":
            return a-b
        case "MULTIPLICACION" |"Multiplicacion":
            return a*b 
        case "DIVISION"|"Division":
            return a/b    
        case "POTENCIA"|"Potencia":
            print('Potencia de:',a,b)
            return a**b 
        case "RAIZ"|"Raiz":
            return a**(1/b)
        case "MOD"|"Mod":
            return a%b
        case "INVERSO"|"Inverso":
            return 1/a
        case "SENO"|"Seno":
            a=(a/180)*math.pi
            return math.sin(a)
        case "COSENO"|"Coseno":
            a=(a/180)*math.pi
            return math.cos(a) 
        case "TANGENTE"|"Tangente":
            a=(a/180)*math.pi
            return math.tan(a)
        case _:
            print("¡OPERACIÓN NO VÁLIDA: "+operacion+"!")

#print(hacer("Seno",90))
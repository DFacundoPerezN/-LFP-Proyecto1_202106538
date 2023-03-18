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
            return a**b 
        case "RAIZ"|"Raiz":
            return a^(1/b)
        case "MOD"|"Mod":
            return a%b
        case "INVERSO"|"Inverso":
            return 1/a
        case "SENO"|"Seno":
            return math.sin(a)
        case "COSENO"|"Coseno":
            return math.cos(a) 
        case "TANGENTE"|"Tangente":
            return math.tan(a)
        case _:
            print("¡OPERACIÓN NO VÁLIDA: "+operacion+"!")


#print(resultadoOperacion("TANGENTE",1))

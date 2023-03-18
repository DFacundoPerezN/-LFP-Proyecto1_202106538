import tkinter as tk
import Errores.RevisarErrores as RevisarErrores
import Guardar

def abrirArchivo(espacio, ruta):
    espacio.delete("1.0", "end")
    newFile = open (ruta, "r")
    info = newFile.read()
    espacio.insert("insert", info)

def revisionErrores(ruta):
    print('revisando los errores')
    RevisarErrores.revisar(ruta)

def guardarArchivo(datos,nombreArchivo = "Archivo.txt"):
    Guardar.guardar(datos, nombreArchivo)


def abrirWindowMA():
    windowP = tk.Tk()
    windowP.title("Menu Archivos")
    windowP.columnconfigure([0,8], minsize=100)
    windowP.rowconfigure([0,8], minsize=100)
    windowP.configure(background="#ffbe76")
    posicion="Linea X, Columna Y"

    label1 = tk.Label(windowP, text="Ruta del Archivo Con Nombre:" , bg="#ffbe76")
    label1.grid(row=0,column=1)

    textBox1 = tk.Entry(windowP, text="")
    textBox1.grid(row=0,column=2)

    textArea1= tk.Text(windowP, height=40)
    textArea1.grid(row=4,column=2, padx=10,pady=10)

    label2 = tk.Label(windowP, text=posicion , bg="#ffbe76")
    label2.grid(row=4,column=3)

    def llamado(event):
        x,y=textArea1.index(tk.INSERT).split(".")
        posicion=(f"Linea: {x}, Columna: {y}")
        label2 = tk.Label(windowP, text=posicion , bg="#ffbe76")
        label2.grid(row=4,column=3)

    textArea1.bind("<Key>",llamado)
    textArea1.bind("<Button-1>",llamado)

    button1= tk.Button(windowP, text ="Abrir Archivo", command=lambda: abrirArchivo(textArea1, textBox1.get()), bg="#686de0") #Abre el Archivo para poder editarlo
    button1.grid(row=1,column=1, padx=5,pady=10)

    button2= tk.Button(windowP, text ="Guardar Archivo", command=lambda: guardarArchivo(textArea1.get("1.0", "end")), bg="#686de0") #Guarda el archivo
    button2.grid(row=1,column=2, padx=10,pady=10)

    textBox2 = tk.Entry(windowP)  
    textBox2.grid(row=1,column=4)

    button3= tk.Button(windowP, text ="Guardar Archivo Como: ", command=lambda: guardarArchivo(textArea1.get("1.0", "end"), textBox2.get()) , bg="#686de0") #Guarda el Archivo con el nombre especificado
    button3.grid(row=1,column=3, padx=10,pady=10)

    button4= tk.Button(windowP, text ="Analisis del Archivo", bg="#7ed6df") #Imprime la informacion presente en el archivo
    button4.grid(row=2,column=1, padx=10,pady=10)

    button5= tk.Button(windowP, text ="Revisión de Errores",command=lambda: revisionErrores(textBox1.get()), bg="#7ed6df")   #Revisa los Errores del Archivo
    button5.grid(row=2,column=2, padx=10,pady=10)

    button7= tk.Button(windowP, text ="Salir",command=windowP.destroy, bg="#ff6b6b")   #Botón de regresar
    button7.grid(row=7,column=4)

    windowP.mainloop()

import tkinter as tk

def abrirMenuArchivos():
    import MenuArchivo
    MenuArchivo.abrirWindowMA()

def abrirMenuAyuda():
    import InterfazAyuda.MenuAyuda as MenuAyuda
    MenuAyuda.abrirWindowA()

windowInicio = tk.Tk()
windowInicio.title("Inicio") #Asignarle titulo a ala ventana
windowInicio.columnconfigure([0,4], minsize=200) #Columnas de la Ventana
windowInicio.rowconfigure([0,10], minsize=100) #Filas de la Ventana y su proporción
windowInicio.configure(background="#00d2d3")

button1= tk.Button(windowInicio, text ="Abrir Menu de Archivo", command=lambda: abrirMenuArchivos(),  bg="#25CCF7") #Boton redirecciona al menu de archivos
button1.grid(row=3,column=1, pady=10)

button2= tk.Button(windowInicio, text ="Ayuda", command=lambda: abrirMenuAyuda(), bg="#55E6C1") #Boton de redirrecionar al Menu de Ayuda
button2.grid(row=6,column=1, pady=10)

button4= tk.Button(windowInicio, text ="Salir", command=windowInicio.destroy, bg="#ee5253")   #Botón de salir
button4.grid(row=9,column=1)

windowInicio.mainloop()               #Llamamos a la ventana
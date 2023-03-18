import tkinter as tk

def abrirWindowTA():
    windowTA = tk.Tk()
    windowTA.title("Temas ayuda") #Asignarle titulo a ala ventana
    windowTA.columnconfigure([0,4], minsize=100) #Columnas de la Ventana
    windowTA.rowconfigure([0,4], minsize=100) #Filas de la Ventana y su proporción
    windowTA.configure(background="#9AECDB")

    label1 = tk.Label(windowTA, text="Nombre del curso: Lab Lenguajes Formales y de Programacion", bg="#9AECDB")
    label1.grid(row=0,column=1, pady=10)

    label2 = tk.Label(windowTA, text="Nombre del Estudiante: Diegno Facundo Pérez Nicolau", bg="#9AECDB")
    label2.grid(row=1,column=1, pady=10)

    label3 = tk.Label(windowTA, text="Carne del Estudiante: 202106538", bg="#9AECDB")
    label3.grid(row=2,column=1, pady=10)

    windowTA.mainloop()               #Llamamos a la ventana

#abrirWindowTA()
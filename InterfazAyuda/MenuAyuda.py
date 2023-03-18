import tkinter as tk
import subprocess
import webbrowser

aTecnico= "Manuales\MANUAL TECNICO.pdf"
aUsuario= 'Manuales\MANUAL USUARIO.pdf'

def TemasAyuda():
    import InterfazAyuda.TemasAyuda
    InterfazAyuda.TemasAyuda.abrirWindowTA()

def abrirWindowA():
    windowHelp = tk.Tk()
    windowHelp.title("Consultar Ayuda")
    windowHelp.columnconfigure([0,4], minsize=150)
    windowHelp.rowconfigure([0,8], minsize=100)
    windowHelp.configure(background="#10ac84")

    button1= tk.Button(windowHelp, text ="Manual de Usuario",command=lambda: subprocess.Popen([aUsuario], shell=True),  bg="#1dd1a1") #Abre el Manual de Usuario
    button1.grid(row=2,column=1, padx=10,pady=10)

    button2= tk.Button(windowHelp, text ="Manual Tecnico",command=lambda: subprocess.Popen([aTecnico], shell=True), bg="#1dd1a1") #Abre el Manual Tecnico
    button2.grid(row=4,column=1, padx=10,pady=10)

    button3= tk.Button(windowHelp, text ="Temas de ayuda", command=lambda: TemasAyuda(), bg="#1dd1a1") #Muestra una pagina de ayuda
    button3.grid(row=6,column=1, padx=10,pady=10)

    button5= tk.Button(windowHelp, text ="Regresar",command=windowHelp.destroy, bg="#ff6b6b")   #Botón de regresar
    button5.grid(row=7,column=2)

    windowHelp.mainloop()

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Pulse los botones Varón o Mujer:")
        self.label1.grid(column=0,row=0)

        self.boton1=tk.Button(self.ventana1, text="Varón", command=self.ingresarVaron)
        self.boton1.grid(column=1, row=0)

        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.ingresarMujer)
        self.boton2.grid(column=2, row=0)
        self.ventana1.mainloop()

    def ingresarVaron(self):
        self.ventana1.title("Varón")

    def ingresarMujer(self):
        self.ventana1.title("Mujer")

  

aplicacion1=Aplicacion()


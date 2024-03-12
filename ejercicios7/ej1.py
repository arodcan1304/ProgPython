import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="Google Chrome", variable=self.seleccion1)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="Opera", variable=self.seleccion2)
        self.check2.grid(column=0, row=1)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1,text="Firefox", variable=self.seleccion3)
        self.check3.grid(column=0, row=2)
        self.seleccion4=tk.IntVar()
        self.check4=tk.Checkbutton(self.ventana1,text="Edge", variable=self.seleccion4)
        self.check4.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana1, text="Visualizar", command=self.verificar)
        self.boton1.grid(column=0, row=4)
        self.label1=tk.Label(self.ventana1,text="Navegadores")
        self.label1.grid(column=0, row=5)
        self.ventana1.mainloop()

    def verificar(self):
        cant=''
        if self.seleccion1.get()==1:
            cant+='\nGoogle Chrome'
        if self.seleccion2.get()==1:
            cant+='\nOpera'
        if self.seleccion3.get()==1:
            cant+='\nFirefox'
        if self.seleccion4.get()==1:
            cant+='\nEdge'
        self.label1.configure(text="Navegadores:"+str(cant))


aplicacion1=Aplicacion()




aplicacion1=Aplicacion()

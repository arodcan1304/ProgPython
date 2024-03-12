import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"España")
        self.listbox1.insert(1,"Francia")
        self.listbox1.insert(2,"Alemania")
        self.listbox1.insert(3,"Inglaterra")
        self.listbox1.insert(4,"Holanda")
        self.listbox1.insert(5,"Italia")
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=2)
        self.label1=tk.Label(self.ventana1,text="Seleccionado:")
        self.label1.grid(column=0, row=3)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.label1.configure(text=self.dato1.get()+''+self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion()

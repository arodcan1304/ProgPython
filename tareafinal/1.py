import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.contador=0
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1)
        opciones1.add_separator()
        opciones1=tk.Menu(menubar1,tearoff=0)
        self.agregar_menu()
        self.aprobados_suspensos()



        
     

        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.label1=ttk.Label(text="Nombre")
        self.label1.grid(column=0, row=0)


        self.dato2=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry1.grid(column=1, row=1)


        self.label2=ttk.Label(text="Nota")
        self.label2.grid(column=0, row=1)


        self.dato3=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=20, textvariable=self.dato3)
        self.entry1.grid(column=1, row=2)


        self.label3=ttk.Label(text="Código")
        self.label3.grid(column=0, row=2)

        

        




        self.boton1=ttk.Button(self.ventana1, text="Insertar", command=self.insertar)
        self.boton1.grid(column=0,row=3)

        self.boton2=ttk.Button(self.ventana1, text="Eliminar", command=self.eliminar)
        self.boton2.grid(column=1,row=3)


        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=4,columnspan=2,sticky="we")


        self.ventana1.mainloop()

        

    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Salir", command=self.salir)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)   

    def insertar(self):
        dato=self.dato1.get()+"-"+self.dato2.get()+"-"+self.dato3.get()
        self.listbox1.insert(self.contador,dato)
        self.contador=self.contador+1
        
    def eliminar(self):
        if len(self.listbox1.curselection())!=0:
            item=self.listbox1.curselection()[0]
            self.listbox1.delete(item)
            self.contador=self.contador-1
        print()

    def aprobados_suspensos(self):

        if self.label2<5:
            
            print(self.label1, "está suspenso")

        else:

            print("El alumno", self.label1, "está aprobado")


  


    def salir(self):
        respuesta=mb.askyesno("Cuidado","¿Quiere salir del programa?")
        mb.showinfo("Información", "Este programa fue desarrollado para el aprendizaje de Python y tkinter.")


    
aplicacion1=Aplicacion()


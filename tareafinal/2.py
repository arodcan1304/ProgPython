import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.contador = 0
        self.alumnos = []  # List to store student data
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        self.agregar_menu()

        self.dato1 = tk.StringVar()
        ttk.Label(self.ventana1, text="Nombre").grid(column=0, row=0)
        self.entry1 = ttk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)

        self.dato2 = tk.StringVar()
        ttk.Label(self.ventana1, text="Nota").grid(column=0, row=1)
        self.entry2 = ttk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        self.dato3 = tk.StringVar()
        ttk.Label(self.ventana1, text="Código").grid(column=0, row=2)
        self.entry3 = ttk.Entry(self.ventana1, width=20, textvariable=self.dato3)
        self.entry3.grid(column=1, row=2)

        ttk.Button(self.ventana1, text="Insertar", command=self.insertar).grid(column=0, row=3)
        ttk.Button(self.ventana1, text="Eliminar", command=self.eliminar).grid(column=1, row=3)

        self.listbox1 = tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0, row=4, columnspan=2, sticky="we")

        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Salir", command=self.salir)
        opciones1.add_command(label="Generar Informe Aprobados", command=self.generar_informe_aprobados)
        opciones1.add_command(label="Generar Informe Suspensos", command=self.generar_informe_suspendidos)
        menubar1.add_cascade(label="Opciones", menu=opciones1)

    def insertar(self):
        nombre = self.dato1.get()
        nota = int(self.dato2.get())
        codigo = self.dato3.get()
        dato = f"{nombre}-{nota}-{codigo}"
        self.alumnos.append((nombre, nota, codigo))
        self.listbox1.insert(self.contador, dato)
        self.contador += 1

    def eliminar(self):
        if len(self.listbox1.curselection()) != 0:
            item = self.listbox1.curselection()[0]
            del self.alumnos[item]
            self.listbox1.delete(item)
            self.contador -= 1

    def generar_informe_aprobados(self):
        with open("aprobados.txt", "w") as file:
            for alumno in self.alumnos:
                if alumno[1] >= 5:
                    file.write(f"{alumno[0]} - Aprobado\n")

    def generar_informe_suspendidos(self):
        with open("suspendidos.txt", "w") as file:
            for alumno in self.alumnos:
                if alumno[1] < 5:
                    file.write(f"{alumno[0]} - Suspensos\n")

    def salir(self):
        respuesta = mb.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta:
            mb.showinfo("Información", "Este programa fue desarrollado para el aprendizaje de Python y tkinter.")


aplicacion1 = Aplicacion()

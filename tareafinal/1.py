import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.contador = 0
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
        ttk.Button(self.ventana1, text="Generar Informe Aprobados", command=self.generar_informe_aprobados).grid(column=0, row=5)
        ttk.Button(self.ventana1, text="Generar Informe Suspensos", command=self.generar_informe_suspensos).grid(column=1, row=5)

        self.listbox1 = tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0, row=4, columnspan=2, sticky="we")

        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Salir", command=self.salir)
        menubar1.add_cascade(label="Opciones", menu=opciones1)

    def insertar(self):
        dato=self.dato1.get()+"-"+self.dato2.get()+"-"+self.dato3.get()
        self.listbox1.insert(self.contador, dato)
        self.contador+= 1

    def eliminar(self):
        if len(self.listbox1.curselection()) != 0:
            item=self.listbox1.curselection()[0]
            self.listbox1.delete(item)
            self.contador-=1

    def generar_informe_aprobados(self):
        self.generar_informe("aprobados_anarodriguez.txt", 5)

    def generar_informe_suspensos(self):
        self.generar_informe("suspensos_anarodriguez.txt", 5, False)

    def generar_informe(self, filename, cutoff_grade, approved=True):
        with open(filename, "w") as file:
            file.write("Nombre\tNota\n")
            for i in range(self.listbox1.size()):
                entry = self.listbox1.get(i)
                nombre, nota, _ = entry.split("-")
                if (approved and float(nota) >= cutoff_grade) or (not approved and float(nota) < cutoff_grade):
                    file.write(f"{nombre}\t{nota}\n")

        mb.showinfo("Informe Generado", f"Informe de {'Aprobados' if approved else 'Suspensos'} generado en {filename}, mira en tu carpeta de descargas")

    def salir(self):
        respuesta = mb.askyesno("Cuidado", "¿Quiere salir del programa?")
        if respuesta:
            mb.showinfo("Información", "Este programa fue desarrollado para el aprendizaje de Python y tkinter, y creado por Ana Rodriguez Cano.")


aplicacion1 = Aplicacion()

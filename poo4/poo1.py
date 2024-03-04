# Clase Cuenta con nombre de titular y monto

class Cuenta:
    def __init__(self):
        self.nombre=input("Introduce nombre:")
        self.monto=int(input("Introduce monto:"))

# Visualizar una cuenta
    def imprimir(self):
        print(self.nombre,"tiene un monto de",self.monto)

class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()


# Visualizar datos de la Caja de Ahorros

    def imprimir(self):
        super().imprimir()


# Clase PlazoFijo que dispone de intereses y plazo de imposicion

class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.interes=float(input("Interés:"))
        self.imposicion=int(input("Plazo de imposicion:"))


# Visualizar datos de la clase PlazoFijo

    def imprimir(self):
        super().imprimir()
        print("Intereses:",self.interes)
        print("Plazo de imposición:",self.imposicion)

# Visualizar ganancia

    def ganancia(self):
        ganancia=self.monto*self.interes/100
        print("Ganancia:",ganancia)
        
#Principal

caja=CajaAhorro()
caja.imprimir()
plazo=PlazoFijo()
plazo.imprimir()
plazo.ganancia()

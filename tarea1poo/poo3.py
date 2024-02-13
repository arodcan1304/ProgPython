#Clase Operaciones con dos propiedades: numero1, numero2

class Operaciones:
    def __init__(self):
        self.numero1=int(input("Numero 1:"))
        self.numero2=int(input("Numero 2:"))




    def suma(self):
        resultado=self.numero1+self.numero2
        print("La suma es",resultado)

    def resta(self):
        resultado=self.numero1-self.numero2
        print("La resta es ",resultado)


    def multiplicar(self):
        resultado=self.numero1*self.numero2
        print("El producto es", resultado)


    def division(self):
        resultado=self.numero1/self.numero2
        print("La division es", resultado)

# Principal

operacion=Operaciones()
operacion.suma()
operacion.resta()
operacion.multiplicar()
operacion.division()


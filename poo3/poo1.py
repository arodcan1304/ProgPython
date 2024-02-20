class Socio:
    def __init__(self):
        self.nombre=input("Introduce nombre:")
        self.antiguedad=int(input("Introduce antiguedad:"))


#Visualizar un socio
    def imprimir(self):
            print(self.nombre,"tiene una antiguedad en años de ",self.antiguedad)


#Retornar antiguedad
    def verAntiguedad(self):
            return self.antiguedad

#Clase CLub con una lista de socios
class Club:
    def __init__(self):
        self.socios=[]

#Agregar un socio
    def agregarSocio(self):
        socio=Socio()
        self.socios.append(socio)


#Mostrar todos los socios
    def mostrarSocios(self):
        for socio in self.socios:
            socio.imprimir()

#Mostrar un socio
    def mostrarUnSocio(self):
        pos=int(input("Introduce la posicion del socio a visualizar:"))
        if(pos<len(self.socios)):
            self.socios[pos].imprimir()

#Visualizar el socio de mayor antiguedad
    def mostrarMayorAntiguedad(self):
        mayor=self.socios[0]
        for socio in self.socios:
            if socio.verAntiguedad>mayor.verAntiguedad:
                mayor=socio
        print("Socio de mayor antiguedad:")
        mayor.imprimir()
       
#Principal
club=Club()
club.agregarSocio()
club.agregarSocio()
club.agregarSocio()
club.mostrarSocios()
club.mostrarUnSocio()
club.mostrarMayorAntiguedad()

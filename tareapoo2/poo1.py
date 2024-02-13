# Clase Agenda con una lista con una sublista (nombre, telefono, email)


class Agenda:
    def __init__(self):
        self.listaAgenda=[]

#Cargar datos de un usuario en la agenda
    def cargar(self):
            nombre=input("Nombre:")
            telefono=input("Teléfono:")
            email=input("Email:")
            lista=[]
            lista.append(nombre)
            lista.append(telefono)
            lista.append(email)
            self.listaAgenda.append(lista)

            
# Listado completo de la agenda

    def listar(self):
        for usuario in self.listaAgenda:
            print(usuario[0],":",usuario[1],"-",usuario[2])


# Consultar por nombre
    def consultaNombre(self):
        nombre=input("Nombre a consultar:")
        encontrado=0
        longitud=len(self.listaAgenda)
        indice=0
        while encontrado==0 and indice<longitud:
            if self.listaAgenda[indice][0]==nombre:
                print("Telefono:",self.listaAgenda[indice][1])
                print("Email:",self.listaAgenda[indice][2])
                encontrado=1
            indice=indice+1
        if encontrado==0:
            print(nombre,"no se ha encontrado en la agenda")
        else:
            return indice-1

# Modificar teléfono y email

    def modificar(self):
        pos=self.consultaNombre()
        telefono=input("Teléfono:")
        email=input("Email:")
        self.listaAgenda[pos][1]=telefono
        self.listaAgenda[pos][2]=email

        
# Menu

    def menu(self):
        op=6
        while op!=5:
            print("1. Cargar datos en la agenda.")
            print("2. Listar datos de la agenda.")
            print("3. Consultar por nombre.")
            print("4. Modificar teléfono y email")
            print("5. Finalizar")
            op=int(input("Introduce una opción"))
            if op==1:
                self.cargar()
            if op==2:
                self.listar()
            if op==3:
                self.consultaNombre()
            if op==4:
                self.modificar()

# Principal

miagenda=Agenda()
miagenda.menu()

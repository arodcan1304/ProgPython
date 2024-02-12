# Agregar estudiante

def agregar(lista):
    codigo=int(input("Codigo:"))
    nombreYapel=input("Nombre y apellidos:")
    asignatura=input("Asignatura:")
    nota=float(input("Nota:"))
    lista.append((codigo,nombreYapel,asignatura,nota))
    return lista

# Eliminar estudiante por codigo

def eliminar(lista,codigo):
    indice=0
    estado=1
    while estado==1 and indice<len(lista):
        estudiante=lista[indice]
        if estudiante[0]==codigo:
            estado=0
        indice=indice+1
    if estado==0:
        lista.pop(indice-1)
    return lista





# Modificar estudiante

def modificar(lista,codigo):
    indice=0
    estado=1
    while estado==1 and indice<len(lista):
        estudiante=lista[indice]
        if estudiante[0]==codigo:
           nombreYapel=input("Nuevo nombre y apellidos:")
           asignatura=input("Nueva asignatura:")
           nota=float(input("Nueva nota:"))
           estado=0
        indice=indice+1
    if estado==0:
        lista.pop(indice-1)
        lista.insert(indice-1,(codigo,nombreYapel,asignatura,nota));
    return lista



# Modificar todos los estudiantes

def mostrarTodos(lista):
    for estudiante in lista:
        for datos in estudiante:
            print(datos,end=" ")
        print()

# Mostrar estudiantes por asignatura


def mostrarPorAsignatura(lista,asignatura):
    for estudiante in lista:
        if estudiante[2]==asignatura:
            for datos in estudiante:
                print(datos,end=" ")
            print()


# Mostrar aprobados por asignatura

def mostrarAprobadosPorAsignatura(lista,asignatura):
    for estudiante in lista:
        if estudiante[2]==asignatura and estudiante[3]>=5:
            for datos in estudiante:
                print(datos,end=" ")
            print()

# Menu
def menu():
    opcion=0
    print("1. Agregar estudiante")
    print ("2. Eliminar un estudiante (por código)")
    print("3. Modificar un nuevo estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Mostrar estudiantes por asignatura")
    print("6. Mostrar aprobados por asignatura")
    print("7. Salir")
    opcion=int(input("Elige una opción:"))
    return opcion

# Principal

op=0
lista=[]
while op!=7:
    op=menu()
    if op==1:
        lista=agregar(lista)
    if op==2:
        codigo=int(input("Codigo a eliminar:"))
        lista=eliminar(lista,codigo)
    if op==3:
        codigo=int(input("Codigo a modificar:"))
        lista=modificar(lista,codigo)
    if op==4:
        mostrarTodos(lista)
    if op==5:
        asignatura=input("Asignatura a consultar:")
        mostrarPorAsignatura(lista,asignatura)
    if op==6:
        asignatura=input("Asignatura a consultar:")
        mostrarAprobadosPorAsignatura(lista,asignatura)

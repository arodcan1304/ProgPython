#funcion creamos una lista de n empleados
def crearLista(n):
    lista=[]
    for x in range(n):
        sueldo=int(input("Introduce un sueldo:"))
        lista.append(sueldo)
    return lista

#funcion visualizar sueldos
def verSueldos(lista):
    print(lista)

#funcion sueldos superiores a 4000
def superior4000(lista):
    cantidad=0
    for x in range(len(lista)):
        if lista[x]>4000:
            cantidad=cantidad+1
        print("Sueldos superior a 4000:",cantidad)

#funcion sueldo medio
def sueldoMedio(lista):
    sueldo=0
    for x in range(len(lista)):
        sueldo=sueldo+lista[x]
    promedio=sueldo/len(lista)
    return promedio

#funcion sueldos por debajo de la media
def debajoMedia(lista):
    sueldoMedia=0
    media=sueldoMedia(lista)
    print("Los sueldos por debajo de la media son:")
    for x in range(len(lista)):
        if lista[x]<media:
            print(lista[x])

#Principal
n=int(input("Cuantos empleados hay?"))
lista=crearLista(n)
verSueldos(lista)
superior4000(lista)
print("El sueldo medio es ",sueldoMedio(lista))
debajoMedia(lista)

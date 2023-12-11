"""
Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema.

"""

num=0
suma=0
while num!=-1:
    num=int(input("Numero:"))
    if num!=-1:
        suma=suma+num
print("La suma total es ",suma)

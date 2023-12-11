# Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.

# Sumar 10 número

# Ana Rodríguez Cano

# 11 de diciembre de 2023

#Variable acumuladora, suma

suma=0
for x in range(10):
    num=int(input("Numero:"))#Lectura del número
    suma=suma+num #acumulamos el número

#Visualizamos el total
print("El suma total es ",suma)

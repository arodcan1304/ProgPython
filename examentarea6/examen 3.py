def suma_pares_hasta_n():
    n=int(input("Introduce un número: "))
    suma=0
    for i in range(2, n+1, 2):
        suma+=i

    print("La suma de todos los números pares hasta",n,"es:",suma)

suma_pares_hasta_n()

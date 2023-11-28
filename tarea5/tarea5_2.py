suma=0
producto=1
for x in range(10):
    numero=int(input("Numero:"))
    if x<5:
        suma=suma+numero

    else:
        producto=producto*numero

print("La suma de los cinco primeros numeros es",suma)
print("El producto de los cinco últimos numeros es",producto)

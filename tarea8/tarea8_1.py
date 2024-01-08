frase=input("Introduce una frase:")
cantidad=1
longitud=len(frase)
x=0
while x<longitud:
    if (frase[x]==" "):
        cantidad=cantidad+1

    x=x+1
print("Palabras:",cantidad)

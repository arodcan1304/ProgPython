oracion=input("Introduce una frase:")
vocales=0
frase = oracion.lower()
x=0
while x<len(frase):
    if oracion[x]=='a' or frase[x]=='e' or frase[x]=='i' or frase[x]=='o' or frase[x]=='u':
        vocales = vocales+1

    x=x+1
print("Cantidad de vocales:",vocales)

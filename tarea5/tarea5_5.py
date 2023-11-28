n=int(input("Puntos del plano?"))
primer=0
segundo=0
tercero=0
cuarto=0
for x in range(n):
    cordX=float(input("Coordenada X:"))
    cordY=float(input("Coordenada Y:"))
    if cordX>0 and cordY>0:
        print("Primer cuadrante")
        primer=primer+1

    else:
        if cordX<0 and cordY>0:
            print("Segundo cuadrante")
            segundo=segundo+1
        else:
            if cordX<0 and cordY<0:
                print("Tercer cuadrante")
                tercero=tercero+1
            else:
                print("Cuarto cuadrante")
                cuarto=cuarto+1

print("Primer cuadrante",primer)
print("Segundo cuadrante",segundo)
print("Tercer cuadrante",tercero)
print("Cuarto cuadrante",cuarto)


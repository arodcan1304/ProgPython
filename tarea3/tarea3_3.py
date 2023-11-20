cordX=int(input("Introduce coordenada X:"))
cordY=int(input("Introduce coordenada Y:"))
if cordX>0 and cordY>0:
    print("Primer cuadrante")
if cordX<0 and cordY>0:
    print("Segundo cuadrante")
if cordX<0 and cordY<0:
    print("Tercer cuadrante")
if cordX>0 and cordY<0:
    print("Cuarto cuadrante")

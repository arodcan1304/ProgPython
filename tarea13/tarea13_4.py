# Leer una lista de 3 candidatos
# candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]

def cargar_candidatos():
    candidatos=[]
    for x in range(3):
        nombre=input("Introduce nombre del candidato:")
        provincias=[]
        otraProvincia="si"
        while otraProvincia=="si":
            provincia=input("Introduce nombre de la provincia:")
            votos=int(input("Numero de votos de la provincia:"))
            provincias.append((provincia,votos))
            otraProvincia=input("Vas a introducir otra provincia(si/no)")
    candidatos.append((nombre,provincias))


    return candidatos

# Visualizar votos de los 3 candidatos

def visualizar_votos(candidatos):
    for candidato in candidatos:
        totalVotos=0
        for provincia in candidato[1]:
            totalVotos=totalVotos+provincia[1]

        print(candidato[0]," ha obtenido un total de votos de ",totalVotos)


# Programa principal
candidatos=cargar_candidatos()
visualizar_votos(candidatos)



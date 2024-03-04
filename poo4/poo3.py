# Clase Jugador con  una variable de clase juego
class Jugador:
    juego=30
    def __init__(self):
        self.nombre=input("Introduce un nombre:")
        self.puntaje=int(input("Introduce puntos:"))
    def __str__(self):
        cadena=self.nombre+" tiene un puntaje de "+str(self.puntaje)
        if self.puntaje>1000:
            cadena=cadena+" y es Experto"
        else:
            cadena=cadena+" y es Principiante"
        return cadena

# Principal

jugador1=Jugador()
jugador2=Jugador()
print(jugador1)
print(jugador2)

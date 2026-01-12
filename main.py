#SISTEMA DE REGISTRO DE VEHÍCULOS
#Creamos la clase Coche
class Coche:
    def __init__(self,marca,modelo, anio,color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
#pedimos datos a nuestro usuario
marca = input("Ingrese la marca del coche:")
modelo = input("Ingrese el modelo del coche:")
anio = int(input("Ingrese el año del coche:"))
color = input("Ingrese el color del coche:")

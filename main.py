# SISTEMA DE REGISTRO DE VEHÍCULOS

# Creamos la clase Coche
class Coche:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

# Pedimos datos al usuario
marca = input("Ingrese la marca del coche: ")
modelo = input("Ingrese el modelo del coche: ")
anio = int(input("Ingrese el año del coche: "))
color = input("Ingrese el color del coche: ")

# Creamos el objeto
coche = Coche(marca, modelo, anio, color)

# Verificamos si es nuevo o usado
if coche.anio >= 2022:
    print("El coche es NUEVO")
else:
    print("El coche es USADO")

# Menú interactivo
while True:
    print("\n--- Menú ---")
    print("1. Cambiar marca")
    print("2. Cambiar modelo")
    print("3. Cambiar año")
    print("4. Cambiar color")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
     coche.marca = input("Nueva marca: ")

    elif opcion == "2":
        coche.modelo = input("Nuevo modelo: ")

    elif opcion == "3":
        coche.anio = int(input("Nuevo año: "))

    elif opcion == "4":
        coche.color = input("Nuevo color: ")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")

    # Mostrar datos actualizados
print("\nDatos actuales del coche:")
print(coche.marca, coche.modelo, coche.anio, coche.color)



class Laptop:
    # Atributos de clase
    marca = "HP NOTER"
    color = "NEGRO"

    def __init__(self, modelo, precio, memoria_ram, almacenamiento, procesador):
        # Atributos de instancia
        self.modelo = modelo
        self.precio = precio
        self.memoria_ram = memoria_ram
        self.almacenamiento = almacenamiento
        self.procesador = procesador

    def mostrar_informacion(self):
        print(f"Marca: {Laptop.marca}")
        print(f"Color: {Laptop.color}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio: {self.precio}")
        print(f"Memoria RAM: {self.memoria_ram}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"Procesador: {self.procesador}")

    def encender(self):
        print("La laptop está encendiendo...")

    def apagar(self):
        print("La laptop se está apagando...")


# Crear una instancia de la clase Laptop
mi_laptop = Laptop("HP GAMER PLAYER", 1500, "16GB", "2TB", "Intel Core i7")

# Acceder a los atributos de instancia y llamar a las funcionalidades
mi_laptop.mostrar_informacion()
mi_laptop.encender()
mi_laptop.apagar()



    
     
     
     
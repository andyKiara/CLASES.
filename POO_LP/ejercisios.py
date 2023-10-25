# haciendo uso de la POO para cantidad celular
class Celular:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def llamar(self, numero):
        print(f"Llamando al número {numero}...")
    
    def enviar_mensaje(self, numero, mensaje):
        print(f"Enviando mensaje a {numero}: {mensaje}")

# Crear una instancia de la clase Celular
mi_celular = Celular("Samsung", "Galaxy S20", "Negro")

# Acceder a los atributos del celular
print(mi_celular.marca)  # Output: Samsung
print(mi_celular.modelo)  # Output: Galaxy S20
print(mi_celular.color)  # Output: Negro

# Llamar y enviar mensajes desde el celular
mi_celular.llamar("123456789")
mi_celular.enviar_mensaje("987654321", "Hola, ¿cómo estás?")

# haciendo uso de la POO crear un objeto para la cantidad vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El vehículo ha sido encendido.")
        else:
            print("El vehículo ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El vehículo ha sido apagado.")
        else:
            print("El vehículo ya está apagado.")

    def conducir(self):
        if self.encendido:
            print(f"Conduciendo el vehículo {self.marca} {self.modelo}.")
        else:
            print("Debes encender el vehículo antes de conducirlo.")

# Crear una instancia de la clase Vehiculo
mi_auto = Vehiculo("Toyota", "Corolla", "Azul")

# Acceder a los atributos del vehículo
print(mi_auto.marca)  # Output: Toyota
print(mi_auto.modelo)  # Output: Corolla
print(mi_auto.color)  # Output: Azul

# Encender, apagar y conducir el vehículo
mi_auto.encender()
mi_auto.conducir()
mi_auto.apagar()



# haciendo uso de la POO crear un objeto para la cantidad avion
class Avion:
    def __init__(self, modelo, capacidad, aerolinea):
        self.modelo = modelo
        self.capacidad = capacidad
        self.aerolinea = aerolinea
        self.en_vuelo = False

    def despegar(self):
        if not self.en_vuelo:
            self.en_vuelo = True
            print(f"El avión {self.modelo} ha despegado.")
        else:
            print("El avión ya está en vuelo.")

    def aterrizar(self):
        if self.en_vuelo:
            self.en_vuelo = False
            print(f"El avión {self.modelo} ha aterrizado.")
        else:
            print("El avión ya está en tierra.")

    def informacion(self):
        print(f"Avión {self.modelo} de la aerolínea {self.aerolinea}. Capacidad: {self.capacidad} pasajeros.")

# Crear una instancia de la clase Avion
mi_avion = Avion("Boeing 747", 400, "Airline X")

# Acceder a los atributos del avión
print(mi_avion.modelo)  # Output: Boeing 747
print(mi_avion.capacidad)  # Output: 400
print(mi_avion.aerolinea)  # Output: Airline X

# Despegar, aterrizar e imprimir información del avión
mi_avion.despegar()
mi_avion.aterrizar()
mi_avion.informacion()


# haciendo uso de la POO un objeto para un heroe de dota2
class HeroeDota2:
    def __init__(self, nombre, fuerza, agilidad, inteligencia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.inteligencia = inteligencia

    def mostrar_atributos(self):
        print(f"Atributos de {self.nombre}:")
        print(f"Fuerza: {self.fuerza}")
        print(f"Agilidad: {self.agilidad}")
        print(f"Inteligencia: {self.inteligencia}")

# Crear una instancia de la clase HeroeDota2
mi_heroe = HeroeDota2("Anti-Mage", 22, 22, 15)

# Acceder a los atributos del héroe
print(mi_heroe.nombre)  # Output: Anti-Mage
print(mi_heroe.fuerza)  # Output: 22
print(mi_heroe.agilidad)  # Output: 22
print(mi_heroe.inteligencia)  # Output: 15

# Mostrar los atributos del héroe
mi_heroe.mostrar_atributos()

# HACIENDO USO DEL POO CREAR UN OBJETO PARA UNA PC
python
class PC:
    def __init__(self, marca, modelo, ram, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.ram = ram
        self.almacenamiento = almacenamiento
        
    def encender(self):
        print("La PC se ha encendido.")
        
    def apagar(self):
        print("La PC se ha apagado.")
        
    def mostrar_especificaciones(self):
        print(f"Especificaciones de la PC:\nMarca: {self.marca}\nModelo: {self.modelo}\nRAM: {self.ram}GB\nAlmacenamiento: {self.almacenamiento}")


Luego puedes crear instancias de la clase y acceder a sus propiedades y métodos:

python
mi_pc = PC("Dell", "Inspiron", 8, "1TB")
mi_pc.encender()  # Output: La PC se ha encendido.
mi_pc.mostrar_especificaciones()  # Output: Especificaciones de la PC: Marca: Dell, Modelo: Inspiron, RAM: 8GB, Almacenamiento: 1TB
mi_pc.apagar()  # Output: La PC se ha apagado.

# HACIENDO USO DEL POOO CREAR UN OBJETO PARA UNA IMPRESORA
python
class Impresora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def imprimir(self, documento):
        print(f"Imprimiendo {documento}...")
        
    def escanear(self):
        print("Escaneando documento...")
        
    def copiar(self, cantidad):
        print(f"Copiando {cantidad} copias...")


Luego puedes crear instancias de la clase y acceder a sus propiedades y métodos:

python
mi_impresora = Impresora("HP", "Deskjet")
print(mi_impresora.marca)  # Output: HP
print(mi_impresora.modelo)  # Output: Deskjet
mi_impresora.imprimir("archivo.txt")  # Output: Imprimiendo archivo.txt...
mi_impresora.escanear()  # Output: Escaneando documento...
mi_impresora.copiar(5)  # Output: Copiando 5 copias..

# HACIENDO USO DEL POO CREAR UN OBJETO PARA EMITIR UNA FACTURA
python
class Factura:
    def __init__(self, numero, cliente, total):
        self.numero = numero
        self.cliente = cliente
        self.total = total

    def imprimir_factura(self):
        print("Factura número:", self.numero)
        print("Cliente:", self.cliente)
        print("Total:", self.total)

# Crear una instancia de la clase Factura
factura1 = Factura(001, "Cliente A", 100.50)

# Llamar al método imprimir_factura para mostrar los detalles de la factura
factura1.imprimir_factura()

# TKINTER - libreria de python para la creacion de interfacez graficas


## 1. crear un objeto laptop con dos
# atributos de clase y 5 atributos de instancia
# debera de tener hasta 3 funcionalidades como minimo
#ojo: solo utilizar lo que hemos echo en clase

python
class Laptop:
    # Atributos de clase
    marca = "Desconocida"
    color = "Negro"

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
mi_laptop = Laptop("HP Pavilion", 1500, "8GB", "1TB", "Intel Core i5")

# Acceder a los atributos de instancia y llamar a las funcionalidades
mi_laptop.mostrar_informacion()
mi_laptop.encender()
mi_laptop.apagar()

  
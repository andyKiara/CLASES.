class Usuario:
    def _init_(self, dni, nombre, edad, f_nacimiento, usuario, password):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.usuario = usuario
        self.password = password

    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def actualizar_datos(self, nuevo_nombre, nueva_edad):
        self.nombre = nuevo_nombre
        self.edad = nueva_edad


    @staticmethod
    def verificar_registro(usuarios, usuario, password):
        for usuario_registrado in usuarios:
            if usuario_registrado["usuario"] == usuario and usuario_registrado["password"] == password:
                return usuario_registrado
        return None


usuarios = [
    {
        "dni": "567657",
        "nombre": "emerson",
        "edad": 18,
        "usuario": "andy",
        "password": "12345"
    },
    
]


input_usuario = input("Ingresa tu nombre de usuario: ")
input_password = input("Ingresa tu contraseña: ")

usuario_verificado = Usuario.verificar_registro(usuarios, input_usuario, input_password)

if usuario_verificado:
    print(f"{input_usuario} está registrado en la base de datos.")

    
    nuevo_nombre = input("Ingresa el nuevo nombre: ")
    nueva_edad = int(input("Ingresa la nueva edad: "))


    usuario_verificado["nombre"] = nuevo_nombre
    usuario_verificado["edad"] = nueva_edad
    

    print(f"Los datos de {input_usuario} han sido actualizados.")
else:
    print(f"{input_usuario} no está registrado .")
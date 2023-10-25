
class Usuario:
    def _init_(self, dni, nombre, edad, f_nacimiento, usuario, password):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.f_nacimiento = f_nacimiento
        self.usuario = usuario
        self.password = password

    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def verificar_registro(self, usuario, password):
        for usuario_registrado in usuarios:
            if usuario_registrado["usuario"] == usuario and usuario_registrado["password"] == password:
                return True
        return False
    moises_data = None

for usuario_data in usuarios:
    if usuario_data["dni"] == "moises":
        moises_data = usuario_data
        break

if moises_data:
    moises = Usuario(moises_data["dni"], moises_data["nombre"], moises_data["edad"], moises_data["f_nacimiento"], moises_data["usuario"], moises_data["password"])


if moises:
    moises.actualizar_edad(33)

if moises.verificar_registro("moises", "12345"):
    print("moises está registrado.")
else:
    print("moises no está registrado.")
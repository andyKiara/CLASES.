# crear un sistema para gestion control de stockl de products


# entidad entitis
# averiguar formas normales(normalizacion de base de datos)
#la base de datos sobre la que voy a trabajar
producto=[ 
    {
        'id':"1",
        "CODIGO":"2023-A"
        'nombre':'arroz',
        'descripcion':'costeño costal x 100k',
        'stokc':"5",
        'unidad': "125",
        'moneda':'soles'
    }
]
# casos de uso
class producto:
    # atributos de instancia
    def _init_(self,nombre,descripcion,stock,
    unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.stock=unidad 
        self.precio=precio
        self.moneda=moneda
    #creacion de metodos
    def mostrar_productos(self):
        mensaje=f"""
        tienes {len(producto)} productos
        los productos son:
        {producto}
        """
        return mensaje
    
    def registrar_producto(self):
        nuevo_id=len(producto)+1
        codigo="2023-B"
        producto_nuevo={
            "id":nuevo_id,
            "codigo":codigo,
            "nombre":self.nombre,
            "descripcion":self.descripcion,
            "stock":self.stock,
            "unidad":self.unidad,
            "precio":self.precio,
            "moneda":self.moneda
        
        }
        registro_producto=producto.append
        (producto_nuevo)
        return f"el sieguiente producto se registro exitosamente{producto_nuevo}"
        
    def mostrar_producto(self,id):
        producto_buscar=producto[id-1]
        return producto_buscar
    
    def eliminar_producto(self,id):
        producto_eliminar=producto.pop(id-1)
        return f"el siguiente producto fue eliminado {producto_eliminar}"
        
    def actualizar_producto(self,id,clave,valor):
        ol=valor
        producto_actualizar=list(filter(lambda obje: obje[clave]==id,producto))[0].update
        ({clave:valor})
        return producto_actualizar
    
#list funcion para crear lista
# programacion funcional python  
# metodo funcional filteer retorna una lista con el elemento que se true de una lista
# funciones anonimos o autoejecutables en python se les conoce como funciones
#lambda -> funcion anonima
#su uso estructura
# lambda a,b:return a+b # esta funcion se autoejecuta no se llama
# suma=lambda a,b:return # para ejecutar esta funcion necesito llamar a la variable suma
# suma(3,4)
prod=producto("aceite","extra virgen",2,"botella x litro",12.50)
print(prod.registrar_producto())
print(prod.mostar_productos())


print(prod.actualizar_producto(125,"precio",130))
print(prod.mostar_productos())



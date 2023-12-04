import orm
from Tablas.productos import productos
from Tablas.clientes import clientes
db=orm.SQLiteORM("tiendita")
db.crear_tabla(productos)
db.crear_tabla(clientes)

#data={
    #"nombre":"detergente",
    #"precio":2.50,
    #"descripcion":"el que te lo limpia",
    #"cantidad":20
#}
#db.insertarUno("productos",data)

data=[
    {
        "nombre":"chinita",
    "dni":702324455
    "celular":92346758
    "f_nacimiento":"13/06/04"
    },
    {
    "nombre":"mochucha"
    "dni":735365463
    "celular":97465476
    "f_nacimiento":"12/12/2023"   
    }
]
#db.insertarVarios("clientes",data)

data={"nombre":"maria"}
db.actualizar("clientes",data,"dni=7998898")


print(db.mostrar("clientes", type="objeto"))
print(db.mostrar("clientes"))
print(db.mostrar("clientes",where="dni=756843849",type="objeto"))
print(db.mostrar("clientes",where="dni=756843849",type="objeto"))
print(db.mostrar("clientes",where="nombre LIKE `%chu`",type="objeto"))


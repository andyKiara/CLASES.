# Programacion Orientado a Objetos(POO)
## En ingles es object Orient Programing(OPP)
- Es un paradigma de programacion
***Paradigma***- es un modelo , patron o ejemplo que se debe seguir.

POO es un modelo de como programar
***objetivo*** - el objetivo es organizar el codigo de manera que se asemeje a como pensamos en la vida real.

se basa en objetos
y en la POO un objeto es toda entidad que se puede describir atravez de **atributos** y **funciones** que puede realizar la entidad.

# celulares
## class celular:

**atributos de tipo clase,que son iguales para todos los objetos que se creen**

```python
familia="smart phone
```

**atributos de instancias son atributos propios del objeto
creamos una funcion inicializadora**

    
    def _init_(self,marca,modelo,imei,nroCelular):
        self.marca=marca
        self.modelo=modelo
        self.imei=imei
        self.
        nrocelular=nrocelular"""
        
    
# funcionalidades
    """python

    def llamar(self,destino):
        return "llamando a {destino}"
# objeto celular jory

    llamandojory=celular("poco","x5","45893434","98473854756") 
    print(llamandojory.marca)
    print(llamandojory.familia)
    print(llamandojory.llamar("china"))
   

# objeto celular nadine
```
llamandoNadine=celular("alacatel","basico","5669567","984765656")
print(llamandoNadine.marca)
print(llamandojory.familia)
print(llamndoNadine.llamar("ollanta))
```
## tarea
crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
#### ejemplo:
```python

tiendas=[
    {
        "nombre":"el pichilon",
        "categoria":["bodega"]
        "horario_atencion":{
            "dia":7am-12m,
            "tarde":2pm-8pm

        }
        "gerente":"nadine"
    }
]
```
#### observacion: " las categorias sera 4: abarrrotes, farmacia, bodega, restaurant"

#### observacion:" los gerentes solo podran ser los siguientes: edwin, china, cristian,nadine"

#### realizar los siguientes ejercisios 
#### crear una clase para tiendas que tenga los siguientes metodos o casos de uso

1. crear un metodo que me filtre las tiendas que tiene cada gerente.

2. crear un metodo que me muestre los negocios que tienen mas de dos gerentes.

3. crear metodo que me muestre solo el nombre y ruc de las tiendas.


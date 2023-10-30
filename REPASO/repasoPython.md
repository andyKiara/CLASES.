# Repaso Python
# 1. Tipos de Datos
``"a"``  ***string cadena de texto***

``"hola"`` ***esto tambien es un string***

``"hola soy un string y te saludo"``  ***cadena larga***

### OBSERVACION :todo lo que ete entre comillas es un string
``"100"``

``"False"``

``"hola"``

### un string puede estar entre comillas simples o dobles

``100`` ***este es un tipo de dato numerico entero***

``2.1`` ***es un tipo de dato numerico de tipo flotante float.***

``False`` ***este es un tipo de dato booleano falso***

``True`` ***tipo de dato booleano verdadero***
# 2. Variables
 - ***Es donde almacenamos nuestro tipo de dato 
 esos datos pueden mutar cambiar o modificarse
como creamos una variable para almacenar nuestro datos. darle un nombre significativo o relacionado al dato que estamos almacenando***

-  ***Indiacarle a que dato esta relacionado -> asignacion =***

 - ***indicar el tipo de dato que se va almacenar -> darle el dato a guardar***

 ### primero el dato voy a pedir la edad de nadine
 ``edad_nadine=18``
 ### el nombre de un alumno
 ``nombre_alumno="edwin"``

# 3. Operadores

1. **operadores aritmeticos**
- *suma+*
- *resta-*
- *multiplicacion**
- *divicion /*


*suma* = ``45+12``

*resta* =``45-12``

*multi*=``2*5``

*divi*=``4/2``

*operacion*=``(45+12+23)/4``

**op**=``15+12+14+13/4``
### operadores de uso especial
#### - suma=45+42   *operador suma resultado 87*

#### - suma="45"+12 *operador concatenacion resultado 4512*

#### - saludo="hola"+"mundo" *concatenacion holamundo*

#### - saludo2="hola"+" "+"mundo"  *concatenar hola mundo*

#### - saludos="hola"*2 *holahola*


# 4. Datos Estructurados
### listas
#### puede alamacenar distintos tipos de datos en una sola lista separados por comas
``lista=["nombre",10,False]``

``lista-amigos=["jory","edwin","adan","chinita"]``
### objetos



- tambien al igual que las listas alamacenan distintos tipos de datos con un orden.
- para almacenar datos en un objeto necesitamos especificar un indice y un valor clave->valor
```python
alumno={
     "nombre":"jory",
    "edad":52,
    "sexo":"todos los dias"

}
```

### combinar ambas estructuras de datos
```python
``alumno={

    "nombre":"jory",
    "edad":30,
    "amigos":["anthony","edwin","china"],
    "direccion":{
        "departamento","ayacucho",
        "provincia","lucanas",
        "distrito","puquio",
        "jiron","san piter",
        "numero",152
    }

}
```
``alumnos=[{},{},{}]

# 5. Controles de flujo
## - Decisiones
***solo se ejecuta el codigo si cumple o si la condicion es verdadera, podemos hacer que si la condiciciòn sea falsa se ejecuta otro codigo***
## Sintaxis
***primero especificar el codigo que se ejecutara si cumple una condicion***

``if <condicion>:``

**el codigo que deseamos ejecutar si la condicion es verdadera**
print("ejecuta esto")
**aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende del if**
``print("esto siempre ejecutara")``

### si queremos que se ejecute un codigo en caso sea falso 
```python
if <condicion falsa>:
  print("solo imprime si es verdad")
else:
  print("solo imprime  si es falso")

```
**ejemplito**
```python
if 15>18:
    print("si es verdad imprime esto")
    else:
        print("si es falso imprime esto")

condicion=True
if condicion:
    print("si es verdad imprime esto")
    else:
        print("si es falso imprime esto")

    
        
```
## - Ciclos

***existen dos tipos:***
## - cuando sabes la cantidad de veces que vamos a repetir 

- *para este caso existe el for*
- *sintaxis despues de la palabra reservada for deberemos crear una variable que almacene el numero que iremos iterando*
- *luego tendremosque indicar el rango interar a los elementos a itear*
```python 
vocales=("a","e","i","o","u")
for i in vocales:
    print(i)
```
# FUNCIONES 
 ## existen dos tipos 

 ### 1. propias de lenguaje
 ## que ya vienen creadas e insertadas en python y estan listas para ser usadas
 ## estructura de uso de una funcion
 ## tiene el nombre seguido de parentesis podremos pasarle datos que necesita la funcion para ejecutarse 

 ## esta es una funcion que nos sirve para mostrar por consola datos 
 print('hola') 

 ## esta funcion nos saber la longitud de una lista o un string
***len nos devuelve un numero***
```python
print(len([1, 5, 6, 7, 8]))
```

# es una funcion que se detiene a esperar que el usuario introdusca informacion 
# entre parentesis podremos escribr un mensaje que indique que accion realizara el usuario 
```python
input('ingresa ingresa')
```

#### Esta funcion nos muestra el numero mayor de una lista:
```python
lista=[45,12,78,3,24,50]
numero_mayor=max(lista)
print(numero_mayor)
```
#### esta funcion nos muestra el numero menor de una lista:
```python
lista=[45,12,78,9,6,12]
numero_menor=min(lista)
print(numero_menor)
```

#### funcion para convertir de un string a un numero entero:
```python
int("100") ->> 100 ->> entero

numero_string="100"
print(type(numero_string))
numero_entero=int(numero_string)
print(type(numero_entero))
```
#### funcion para convertir un entero a un string:
```python
int(100) ->> "100" ->> string
```
#### Funcion de python que nos permite agregar elementos al final de una lista
```python
lista=[15,12,78]
lista.pop()
print(lista)
```
#### funcion de python que nos permite eliminar los elementos que se encuentran al final de una lista
```python
lista=[15,12,78]
lista.pop()
print(lista)
```
#### funcion de python que nos permite agregar elementos en cualquier posicion de mi lista para eso se le tiene que pasar dos parametros, primero indicarle el indice y segundo el dato que se va agregar
```python
lista_nombre=["jory","nadine","bichoota"]
lista_nombre.insert(1,"satan")
print(lista_nombres)
```
#### funciòn de python que nos permite eliminar elemntos de cualquier posicio de lista, esta funcion recibe solo el elemnto que deseasmos eliminar:
```python
lista=[4,5,6,8,7]
lista.remove(6)
print(lista)
```
#### funcion que nos permite dividir en una lista una cadena
```python
cadena="hola como estas"
lista=cadena.split()
print(lista)
url="www.golle.com/id=701333573
id=url.split("=").pop()
print(id)
```

## 2- Funciones creadas
- una duncion son mini programas tambien se le conoce como modulos o fragmentos de codigo de uso exclusivo

## funciones propias
### pasos para crear una funcion propia:
**1: hacer uso de la palabra reservada def**

**2: definir un nombre de funcion que describa que tarea va a realizar**

**3: establecer que valor o dato que resivira la funcion entre parentesis ().**

**4: establecer que valor o dato va retornar mi funcion con la palabra reservada return**

#### ***> Observacion => tambien podemos hacer uso de la funcion print() para retornar un mensaje en nuestra funcion.***
#### ***existen dos tipos de funciones los que no resiven ningun parametro y los que resiven parametros***
```python
def saludo():
    print("hola este es un saludo")
```
## como hacemos uso de la funcion?
## nombre de la funcion y parentesis
## funcion con parametros:
```python
def mi_print(texto):
    print(texto)

print("hola este es print de python")
mi_print("hola este es mi print creado")

def suma(a,b):
    total=a+b
    return total

    suma(45,12) ##==>>>>> 57
```

## ejemplo
#### para que se usa esta funcion ?
#### para mostrar el valor maximo de una lista
```python
lisat=[12,4,45,78,3,1]
mi_print(max(lista))

def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
    return numero_mayor
    mi_print(mi_max(lista))
    ```

## funciones con muchos parametros
```python
def funcion(*muchos_parametros):
    total=0
    for numero in muchos parametros
    total=total+numero
    return
    print(funcion(1,2,3,4,5))

    def datos(*arg):
        nombre=args[0]
        apellido=args[1]
        edad=args[2]
        return f"mi nombre es,{nombre},{apellido}y mi edad es,{edad}"
        print(datos("edwin","apellido","50"))
        


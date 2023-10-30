#1 . import tkinter -> libreria para la creacion de interfaces grafica
from tkinter import*
# la libreria tkinter tiene 3 clases para la creacion de interfaces 
#tk() -> el mas usado
# tkk()
# tcl()

#2. instanciar tk() como generador de interfaz grafica 
nueva_ventana=Tk()
#3. frame es tambien una clase frame() para crear un frame tengo que primero instanciarlo
menu_principal=Frame()
#montamos o inicializamos el frame
menu_principal.pack()
#haciendo uso del metodo config le damos un tamaño
menu_principal.config(width="200",height="200")
#haciendo uso del metodo config le asignamos un color
menu_principal.config(bg="red")
# metodo de tk() que mantiene la ejecucion del programa en un bucle
nueva_ventana.mainloop()
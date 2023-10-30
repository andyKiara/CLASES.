#importamos tkinter
from tkinter import *
#instanciar la clase Tk()
ventana=Tk()
ventana.geometry("400x500")
#creo mid dos widget de orden con la clase Flame()
widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width=150,height=50)

#creacion de etiquetas
etiqueta=Label(ventana,text="ingressa tu nombre oe hjp")
etiqueta.grid(row=1,column=0)


#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=1,column=1)


etiqueta=Label(ventana,text="dni")
etiqueta.grid(row=5,column=0)
#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=5,column=1)


etiqueta=Label(ventana,text="celular")
etiqueta.grid(row=7,column=0)
#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=7,column=1)


ventana.geometry('400x400')

cuadro_rojo = Frame(ventana, bg='red', width=200, height=200)
cuadro_rojo.grid(row=100, column=1, columnspan=9)

#usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()



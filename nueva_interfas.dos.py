#importamos tkinter
from tkinter import *
#instanciar la clase Tk()
ventana=Tk()
ventana.geometry("400x500")
#creo mid dos widget de orden con la clase Flame()
widget_uno=Frame()
widget_uno.grid(row=0,column=0)
widget_uno.config(width=400,height=50)

#creacion de etiquetas
etiqueta=Label(ventana,text="ingressa tu nombre oe hjp")
etiqueta.grid(row=1,column=0)


#creacion de cuadros de texto
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=0)

#usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()
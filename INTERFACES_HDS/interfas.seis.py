
#primero importar la libreria
from tkinter import*

#instanciamos nuestra clase TK()
ventana=Tk() # clase para crear una ventana
ventana.title("clase radiobuttons") # haciendo uso del metodo para el titulo de mi ventana
ventana.geometry("400x300")# haciendo uso del metodo geometry para un tamaño de ventana

#instanciar mi clase Label
etiqueta=Label(ventana,text="radio buttons") # clase para crear una etiqueta
#indicar la parete de mi ventana que deseo que se muestre
# puedo usar los metodos grid o pack
etiqueta.config(fg="blue",font=50)
etiqueta.pack()

info=IntVar()
def mostrar_radio():
    print(info.get())
#instanciar la clase Radiobutton
radioMasculino=Radiobutton(ventana,text="Masculino",value=1,variable=info)
radioMasculino.pack()
radioFemenino=Radiobutton(ventana,text="Femenino",value=0)
radioFemenino.pack()
# instanciar la clase Button
boton=Button(ventana,text="Enviar",command=mostrar_radio)
boton.pack()

# llamar el metodo de Tk que me permite tener persistencia al mostrar la ventana 
ventana.mainloop()

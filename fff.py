from tkinter import *

ventana = Tk()
ventana.title("La Clase Radiobutton")
ventana.geometry("400x300")

etiqueta = Label(ventana, text="Radio buttons")
etiqueta.config(fg="red", font=50)
etiqueta.pack()

info = IntVar()

def mostrar_radio():
    seleccion = info.get()
    if seleccion == 1:
        mensaje = "Eres masculino"
    elif seleccion == 0:
        mensaje = "Eres mujer"
    else:
        mensaje = "Selecciona una opción"
    resultado.config(text=mensaje)

radioMASCULINO = Radiobutton(ventana, text="MASCULINO", value=1, variable=info)
radioMASCULINO.pack()

radioFEMENINO = Radiobutton(ventana, text="FEMENINO", value=0, variable=info)
radioFEMENINO.pack()

boton = Button(ventana, text="ENVIAR", command=mostrar_radio)
boton.pack()

resultado = Label(ventana, text="", fg="blue")
resultado.pack()

ventana.mainloop()


#programacion orientada a objetos -tarea

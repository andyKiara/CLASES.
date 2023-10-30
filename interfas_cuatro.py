from tkinter import*
ventana=Tk()
ventana.geometry("300x350")
ventana.title("vetana suma")

def captura_dato():
   text=text_nombre.get()
   mensaje=Label(ventana,text=f",{text}")
   mensaje.pack()

etiqueta=Label(ventana,text="ingresa tu nombre")
etiqueta.grid(row=0,column=0)
etiqueta.pack()


text_nombre=Entry(ventana)
text_nombre.config(bg="blue",fg="red")
text_nombre.pack()

boton_capturar=Button(ventana,text="enviar",command=captura_dato)
boton_capturar.pack()

ventana.mainloop()





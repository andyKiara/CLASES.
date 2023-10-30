# ejemplo practico

import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x300")

etiqueta = tk.Label(ventana, text="¡Hola, bobo!")
etiqueta.pack()

boton = tk.Button(ventana, text="Haz enter")
boton.pack()

ventana.mainloop()
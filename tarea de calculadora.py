import tkinter as tk

def sumar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 + num2)

def restar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 - num2)

def multiplicar():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    resultado_var.set(num1 * num2)

def dividir():
    num1 = float(numero1_entry.get())
    num2 = float(numero2_entry.get())
    if num2 == 0:
        resultado_var.set("No se puede dividir por cero")
    else:
        resultado_var.set(num1 / num2)

def limpiar():
    numero1_entry.delete(0, tk.END)
    numero2_entry.delete(0, tk.END)
    resultado_var.set("")

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x250")

numero1_label = tk.Label(ventana, text="Primer número:")
numero1_label.pack(pady=10)

numero1_entry = tk.Entry(ventana)
numero1_entry.pack()

numero2_label = tk.Label(ventana, text="Segundo número:")
numero2_label.pack(pady=10)

numero2_entry = tk.Entry(ventana)
numero2_entry.pack()

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()
boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.pack()
boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.pack()
boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack()

resultado_var = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_var)
resultado_label.pack(pady=10)

ventana.mainloop()
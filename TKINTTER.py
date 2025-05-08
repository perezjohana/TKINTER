import tkinter as tk  

def saludar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    etiqueta_resultado.config(text=f"Hola {nombre} y tienes {edad} años")
    
ventana = tk.Tk()
ventana.title("Saludo")
9
ventana.geometry("350x150")
(ventana.config(bg="brown"))

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta = tk.Label(ventana, text="Ingresa tu edad:")
etiqueta.pack()

entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar saludo y edad", command=saludar)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

etiqueta = tk.Label(ventana, text="Johana Poleth Perez Ramirez :)")
etiqueta.pack()

ventana.mainloop()

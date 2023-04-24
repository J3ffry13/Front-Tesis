import tkinter as tk

def imprimir_datos():
    print("El dato 1 es:", input1.get())
    print("El dato 2 es:", input2.get())
    print("El dato 3 es:", input3.get())

# Crear la ventana principal
ventana = tk.Tk()

# Crear los inputs con tamaño de letra de 14 puntos
input1 = tk.Entry(ventana, font=("Arial", 14))
input2 = tk.Entry(ventana, font=("Arial", 14))
input3 = tk.Entry(ventana, font=("Arial", 14))

# Posicionar y personalizar los inputs en la ventana usando place
input1.place(x=25, y=80, height=45, width=500)
input2.place(x=25, y=130, height=45, width=500)
input3.place(x=25, y=180, height=45, width=500)


####################################### PORCENTAJES #######################################
# Crear los inputs para los porcentajes del primer porcentaje
porcentaje1_1 = tk.Entry(ventana, font=("Arial", 14))
porcentaje1_2 = tk.Entry(ventana, font=("Arial", 14))
porcentaje1_3 = tk.Entry(ventana, font=("Arial", 14))

# Posicionar y personalizar los inputs en la ventana usando place
porcentaje1_1.place(x=550, y=80, height=45, width=50)
porcentaje1_2.place(x=550, y=130, height=45, width=50)
porcentaje1_3.place(x=550, y=180, height=45, width=50)

# Crear los inputs para los porcentajes del segundo porcentaje
porcentaje2_1 = tk.Entry(ventana, font=("Arial", 14))
porcentaje2_2 = tk.Entry(ventana, font=("Arial", 14))
porcentaje2_3 = tk.Entry(ventana, font=("Arial", 14))

# Posicionar y personalizar los inputs en la ventana usando place
porcentaje2_1.place(x=620, y=80, height=45, width=50)
porcentaje2_2.place(x=620, y=130, height=45, width=50)
porcentaje2_3.place(x=620, y=180, height=45, width=50)
#############################################################################################


# Crear un widget Label y colocarlo en una posición específica
label1 = tk.Label(ventana, text="Ingrese las desciones a analizar:", font=("Arial", 18))
label1.place(x=20, y=20)


# Crear el botón y posicionarlo en la ventana
boton = tk.Button(ventana, text="Procesar datos", command=imprimir_datos ,font=("Arial", 12))
boton.place(x=600, y=250)

# Establecer las dimensiones de la ventana
ventana.geometry("800x400")

# Iniciar la ventana
ventana.mainloop()

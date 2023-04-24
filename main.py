import tkinter as tk
from validaciones import validate_entry
from procesamiento import Process

def imprimir_datos():
    options = [input1.get(),input2.get(),input3.get()]
    a = [float(porcentaje1_1.get())/100,float(porcentaje2_1.get())/100,float(porcentaje3_1.get())/100]    
    b = [float(porcentaje1_2.get())/100,float(porcentaje2_2.get())/100,float(porcentaje3_2.get())/100]    
    c = [float(porcentaje1_3.get())/100,float(porcentaje2_3.get())/100,float(porcentaje3_3.get())/100]
    weights = [a,b,c]
    network = Process(weights,options)
    decision = network.make_decision()
    # Crear Label de la respuesta:
    labelRpta = tk.Label(ventana, text="La desición correcta es :", font=("Arial", 14))
    labelRpta.place(x=25, y=250)
    # Mostrar la respuesta:
    inputRtpa = tk.Entry(ventana,font=("Arial", 14), takefocus=True)
    inputRtpa.insert(0, decision)
    inputRtpa.place(x=250, y=250, height=45, width=500)


# Crear la ventana principal
ventana = tk.Tk()

# Crear los inputs con tamaño de letra de 14 puntos
input1 = tk.Entry(ventana, font=("Arial", 14))
input2 = tk.Entry(ventana, font=("Arial", 14))
input3 = tk.Entry(ventana, font=("Arial", 14))

# Posicionar y personalizar los inputs en la ventana usando place
input1.place(x=25, y=75, height=45, width=500)
input2.place(x=25, y=135, height=45, width=500)
input3.place(x=25, y=195, height=45, width=500)


######################################## PORCENTAJES ########################################
# Crear los inputs para los porcentajes del primer porcentaje
porcentaje1_1 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))
porcentaje1_2 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))
porcentaje1_3 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))

# Posicionar y personalizar los inputs en la ventana usando place
porcentaje1_1.place(x=550, y=75, height=45, width=55)
porcentaje1_2.place(x=550, y=135, height=45, width=55)
porcentaje1_3.place(x=550, y=195, height=45, width=55)

# Crear los inputs para los porcentajes del segundo porcentaje
porcentaje2_1 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))
porcentaje2_2 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))
porcentaje2_3 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))

# Posicionar y personalizar los inputs en la ventana usando place
porcentaje2_1.place(x=625, y=75, height=45, width=55)
porcentaje2_2.place(x=625, y=135, height=45, width=55)
porcentaje2_3.place(x=625, y=195, height=45, width=55)

# Crear los inputs para los porcentajes del tercer porcentaje
porcentaje3_1 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))
porcentaje3_2 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))
porcentaje3_3 = tk.Entry(validate="key",validatecommand=(ventana.register(validate_entry), "%S", "%P"), font=("Arial", 14))

# Posicionar y personalizar los inputs en la ventana usando place
porcentaje3_1.place(x=700, y=75, height=45, width=55)
porcentaje3_2.place(x=700, y=135, height=45, width=55)
porcentaje3_3.place(x=700, y=195, height=45, width=55)
#############################################################################################

########################################### LABELS ###########################################
# Crear un Label y colocarlo en una posición específica
label1 = tk.Label(ventana, text="DESCICIONES", font=("Arial", 18))
label1.place(x=185, y=35)

# Crear Label para el primer porcentaje  
labelPor1 = tk.Label(ventana, text="P%", font=("Arial", 18))
labelPor1.place(x=555, y=35)

# Crear Label para el segundo porcentaje  
labelPor2 = tk.Label(ventana, text="S%", font=("Arial", 18))
labelPor2.place(x=630, y=35)

# Crear Label para el tercer porcentaje  
labelPor3 = tk.Label(ventana, text="T%", font=("Arial", 18))
labelPor3.place(x=705, y=35)
#############################################################################################


# Crear el botón y posicionarlo en la ventana
boton = tk.Button(ventana, text="Procesar datos", command=imprimir_datos ,font=("Arial", 12))
boton.place(x=600, y=250)

# Establecer las dimensiones de la ventana
ventana.geometry("800x400")

# Iniciar la ventana
ventana.mainloop()


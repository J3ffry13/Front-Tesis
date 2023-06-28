from tkinter import *

def abrir_ventana_bienvenida():
    # Crear la ventana de bienvenida
    ventana_bienvenida = Tk()
    ventana_bienvenida.title("Bienvenido")

    # Crear el texto de bienvenida
    label_bienvenida = Label(ventana_bienvenida, text="¡Hola!")
    label_bienvenida.pack()

    ventana_bienvenida.mainloop()

# Esta parte se ejecutará solo si ejecutas el archivo directamente
if __name__ == "__main__":
    abrir_ventana_bienvenida()

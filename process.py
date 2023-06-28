import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import threading
import time
import ctypes

def regresar(ventana):
    ventana.destroy()
    import main
    
def cerrarse(ventana):
    ventana.destroy()
    import login

def proceso_simulado(progress_bar, ventana, lab, desi, fram):
    # Simulación de un proceso que tarda 10 segundos
    for i in range(10):
        time.sleep(1)  # Simulando 1 segundo de procesamiento
        progress_bar.step(10)  # Avanzar la barra de progreso
        ventana.update()  # Actualizar la ventana
    ventana.after(0, lambda: resultado(progress_bar, ventana, lab, desi, fram))

def resultado(progress_bar, ventana, label, desi, fram):
    # Borrar los elementos anteriores
    progress_bar.destroy()
    label.destroy()
    # Mostrar el resultado
    font_label = ("Arial", 18)
    label_resultado = tk.Label(fram, text=f"La mejor desicion es : {desi}",bg="#1466c3",fg="white",font=font_label)
    # label_resultado.size(14)
    label_resultado.pack()

    # Crear botón para analizar las decisiones  
    font_style = tkFont.Font(family="Open Sans", size=12)
    style = ttk.Style()
    style.configure("RoundedButton.TButton", borderwidth=12, relief="flat", background="#D9D9D9", foreground="black",
                    font=font_style, padding=(0, 1))
    style.map("RoundedButton.TButton", background=[("active", "#1466c3")])

    # Botón de inicio de sesión
    btn_back = ttk.Button(fram, text="Regresar", command=lambda: regresar(ventana), style="RoundedButton.TButton", width=8)
    btn_back.pack(pady=5)
    btn_logout = ttk.Button(fram, text="Cerrar Sesión", command=lambda: cerrarse(ventana), style="RoundedButton.TButton", width=12)
    btn_logout.pack(pady=5)


def principal(desicion):
    # Obtener el tamaño de la mitad de la pantalla
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    window_width = int(screen_width / 2)
    window_height = int(screen_height / 2)

    # Posicionar la ventana en el centro de la pantalla
    position_top = int((screen_height - window_height) / 2)
    position_left = int((screen_width - window_width) / 2)

    # Crear la ventana y establecer su tamaño
    ventana = tk.Tk()
    ventana.title("Toma de Decisiones")
    
    # Configurar el tamaño y la posición de la ventana
    ventana.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
    ventana.configure(bg="#1466c3")
    ventana.resizable(False, False)

    # Crear el marco para el spinner y el texto
    frame = tk.Frame(ventana)
    frame.pack(expand=True)
    frame.configure(bg="#1466c3")

    # Crear la barra de progreso
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TProgressbar", thickness=50)
    progress_bar = ttk.Progressbar(frame, style="TProgressbar", length=int(window_width/3), mode="determinate")
    progress_bar.pack(pady=5)

    # Crear el texto "Procesando..."
    label_procesando = tk.Label(frame, text="Procesando...")
    label_procesando.pack()

    # Centrar el marco en la ventana
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Iniciar el proceso simulado en un hilo separado
    thread = threading.Thread(target=proceso_simulado(progress_bar, ventana, label_procesando, desicion, frame))
    thread.start()

    ventana.mainloop()


# principal('asd')

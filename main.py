import tkinter as tk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import Perceptron
from PIL import ImageTk, Image
import process

def analyze_decisions():
    decision1 = entry1.get("1.0", tk.END)  # Obtener todo el contenido del widget Text
    decision2 = entry2.get("1.0", tk.END)
    decision3 = entry3.get("1.0", tk.END)
    decisions = [decision1, decision2, decision3]

    # Crear la matriz de características utilizando CountVectorizer
    vectorizer = CountVectorizer(stop_words=['a', 'an', 'the'])
    X = vectorizer.fit_transform(decisions)

    # Definir las ponderaciones y el margen de error
    weights = [float(entry4.get()), float(entry5.get()), float(entry6.get())]
    margin_of_error = float(entry7.get("1.0", tk.END))

    # Aplicar margen de error a las ponderaciones
    min_weight = min(weights)
    max_weight = max(weights)
    for i in range(len(weights)):
        if weights[i] == min_weight:
            weights[i] -= margin_of_error
        elif weights[i] == max_weight:
            weights[i] += margin_of_error

    # Convertir las etiquetas a cadenas de texto
    labels = [str(label) for label in weights]

    # Crear el modelo del Perceptrón y entrenarlo
    perceptron = Perceptron()
    perceptron.fit(X, labels)

    # Obtener la mejor decisión
    best_decision_index = perceptron.predict(X).argmax()
    best_decision = decisions[best_decision_index]

    # Crear una ventana aparte para mostrar la mejor decisión
    # result_window = tk.Toplevel()
    # result_window.title("Mejor Decisión")
    # result_label = tk.Label(result_window, text=f"La mejor decisión es: {best_decision}")
    # result_label.pack()
    window.destroy() 
    process.principal(best_decision)

# Crear la ventana principal de la interfaz gráfica
window = tk.Tk()
window.title("Toma de Decisiones")

# Obtener el tamaño de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcular el tamaño de la ventana
window_width = int(screen_width / 2)
window_height = int(screen_height / 2)

# Posicionar la ventana en el centro de la pantalla
position_top = int((screen_height - window_height) / 2)
position_left = int((screen_width - window_width) / 2)

# Configurar el tamaño y la posición de la ventana
window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
window.configure(bg="#1466c3")
window.resizable(False, False)


# Crear etiquetas y campos de entrada
font_label = ("Arial", 18)
font_entry = ("Arial", 16)

# Crear etiquetas y campos de entrada
label1 = tk.Label(window, text="Problemática :",bg="#1466c3",fg="white",font=font_label)
label1.grid(row=0, column=0, sticky="E")
entry1 = tk.Text(window, height=2, width=65)
entry1.grid(row=0, column=1, columnspan=3)

# Crear etiquetas y campos de entrada
label1 = tk.Label(window, text="Decisión 1:",bg="#1466c3",fg="white",font=font_label)
label1.grid(row=1, column=0, sticky="E")
entry1 = tk.Entry(window)
entry1 = tk.Text(window, height=1.4, width=25)
entry1.grid(row=1, column=1)

label2 = tk.Label(window, text="Decisión 2:",bg="#1466c3",fg="white",font=font_label)
label2.grid(row=2, column=0, sticky="E")
entry2 = tk.Entry(window)
entry2 = tk.Text(window, height=1.4, width=25)
entry2.grid(row=2, column=1)

label3 = tk.Label(window, text="Decisión 3:",bg="#1466c3",fg="white",font=font_label)
label3.grid(row=3, column=0, sticky="E")
entry3 = tk.Entry(window)
entry3 = tk.Text(window, height=1.4, width=25)
entry3.grid(row=3, column=1)

label4 = tk.Label(window, text="Ponderación 1:",bg="#1466c3",fg="white",font=font_label)
label4.grid(row=1, column=2, sticky="E")
entry4 = tk.Entry(window)
entry4.grid(row=1, column=3)

label5 = tk.Label(window, text="Ponderación 2:",bg="#1466c3",fg="white",font=font_label)
label5.grid(row=2, column=2, sticky="E")
entry5 = tk.Entry(window)
entry5.grid(row=2, column=3)

label6 = tk.Label(window, text="Ponderación 3:",bg="#1466c3",fg="white",font=font_label)
label6.grid(row=3, column=2, sticky="E")
entry6 = tk.Entry(window)
entry6.grid(row=3, column=3)

label7 = tk.Label(window, text="Margen de error:",bg="#1466c3",fg="white",font=font_label)
label7.grid(row=4, column=0, sticky="E")
entry7 = tk.Entry(window)
entry7 = tk.Text(window, height=1.4, width=25)
entry7.grid(row=4, column=1)

# Crear botón para analizar las decisiones
button_width = window_width // 30
button_font = ("Arial", 16, "bold")
analyze_button = tk.Button(window, text="Analizar", command=analyze_decisions, font=button_font,width=button_width)
analyze_button.grid(row=5, column=0, columnspan=4, padx=10, pady=20)

# Centrar el contenido en las columnas y filas
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)

# Ejecutar la ventana principal de la interfaz gráfica
window.mainloop()

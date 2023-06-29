import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as tkFont
from tkinter import ttk


def login():
    usuario = entry_username.get()
    contrasena = entry_password.get()
    
    if usuario == "admin" and contrasena == "admin123":
        messagebox.showinfo("Login", "Inicio de sesión exitoso")
        window.destroy() 
        # Abrir la ventana principal
        import main
    else:
        messagebox.showerror("Login", "Nombre de usuario o contraseña incorrectos")

# Crear ventana
window = tk.Tk()
window.title("SmartDecider")

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
# Crear el marco para el spinner y el texto

frame = tk.Frame(window, bg="#1466c3")
frame.pack(expand=True)

# Estilo de la fuente
font_style = tkFont.Font(family="Open Sans", size=14)

# Cargar y redimensionar la imagen
image = Image.open("logo.png")
image = image.resize((150, 150), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

# Etiqueta de imagen
label_image = tk.Label(frame, image=image, bg="#1466c3")
label_image.pack(pady=5)

# Etiqueta de usuario
label_username = tk.Label(frame, text="Usuario:", bg="#1466c3",fg="white", font=font_style)
label_username.pack(pady=10)

# Entrada de usuario
entry_username = tk.Entry(frame, bg="#D9D9D9",font=font_style,width=25)
entry_username.pack()
# entry_username.place(x=int(screen_width/3),y=20,height=35,width=350)

# Etiqueta de contraseña
label_password = tk.Label(frame, text="Contraseña:", bg="#1466c3",fg="white", font=font_style)
label_password.pack(pady=10)

# Entrada de contraseña
entry_password = tk.Entry(frame, show="*", bg="#D9D9D9", font=font_style,width=25)
entry_password.pack()
# entry_password.place(relx=0.5,rely=0.5,anchor=tk.CENTER,height=35,width=350)

# Estilo para el botón redondeado
style = ttk.Style()
style.configure("RoundedButton.TButton", borderwidth=50, relief="flat", background="#D9D9D9", foreground="black",
                font=font_style, padding=(0, 3))
style.map("RoundedButton.TButton", background=[("active", "#1466c3")])


# Botón de inicio de sesión
btn_login = ttk.Button(frame, text="Iniciar Sesión", command=login, style="RoundedButton.TButton",width=20)
btn_login.pack(pady=20)

# Centrar el marco en la ventana
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Ejecutar ventana
window.mainloop()
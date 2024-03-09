import tkinter as tk
from tkinter import colorchooser
import pyperclip

def choose_color():
    color = colorchooser.askcolor(title="Selecciona un color")
    color_hex = color[1]
    label_color.config(bg=color_hex, text=f"Color seleccionado: {color_hex}")
    btn_copy.config(state="normal")  # Habilitar el botón de copiar

def copy_color():
    color_hex = label_color.cget("text").split()[-1]  # Obtener el código hexadecimal del texto de la etiqueta
    pyperclip.copy(color_hex)

# Crear la ventana principal
ventana = tk.Tk()
ventana.geometry("300x150")

# Crear el botón para seleccionar el color
btn_color = tk.Button(ventana, text="Seleccionar color", command=choose_color)
btn_color.pack(pady=10)

# Crear una etiqueta para mostrar el color seleccionado
label_color = tk.Label(ventana, text="Color no seleccionado", font=("Arial", 12), padx=10, pady=5)
label_color.pack()

# Crear un botón para copiar el código hexadecimal al portapapeles
btn_copy = tk.Button(ventana, text="Copiar código", command=copy_color)
btn_copy.pack()

ventana.mainloop()

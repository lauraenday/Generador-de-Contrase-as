import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog

def generar_contraseña(longitud, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

class GeneradorContraseñasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas")
        
        # Longitud de la contraseña
        self.label_longitud = tk.Label(root, text="Longitud de la contraseña:")
        self.label_longitud.grid(row=0, column=0, pady=5)
        self.entry_longitud = tk.Entry(root)
        self.entry_longitud.grid(row=0, column=1, pady=5)
        
        # Incluir mayúsculas
        self.incluir_mayusculas = tk.BooleanVar()
        self.check_mayusculas = tk.Checkbutton(root, text="Incluir mayúsculas", variable=self.incluir_mayusculas)
        self.check_mayusculas.grid(row=1, column=0, columnspan=2, pady=5)
        
        # Incluir números
        self.incluir_numeros = tk.BooleanVar()
        self.check_numeros = tk.Checkbutton(root, text="Incluir números", variable=self.incluir_numeros)
        self.check_numeros.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Incluir símbolos
        self.incluir_simbolos = tk.BooleanVar()
        self.check_simbolos = tk.Checkbutton(root, text="Incluir símbolos", variable=self.incluir_simbolos)
        self.check_simbolos.grid(row=3, column=0, columnspan=2, pady=5)
        
        # Botón para generar la contraseña
        self.boton_generar = tk.Button(root, text="Generar Contraseña", command=self.mostrar_contraseña)
        self.boton_generar.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Área para mostrar la contraseña generada
        self.label_contraseña = tk.Label(root, text="")
        self.label_contraseña.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Botón para copiar la contraseña al portapapeles
        self.boton_copiar = tk.Button(root, text="Copiar al Portapapeles", command=self.copiar_al_portapapeles)
        self.boton_copiar.grid(row=6, column=0, columnspan=2, pady=5)
        
        # Botón para guardar la contraseña en un archivo
        self.boton_guardar = tk.Button(root, text="Guardar en Archivo", command=self.guardar_en_archivo)
        self.boton_guardar.grid(row=7, column=0, columnspan=2, pady=5)
        
    def mostrar_contraseña(self):
        try:
            longitud = int(self.entry_longitud.get())
            if longitud <= 0:
                raise ValueError("La longitud debe ser un número positivo.")
            
            self.contraseña_generada = generar_contraseña(longitud, self.incluir_mayusculas.get(), self.incluir_numeros.get(), self.incluir_simbolos.get())
            self.label_contraseña.config(text=f"Contraseña: {self.contraseña_generada}")
        except ValueError as e:
            messagebox.showerror("Error de entrada", str(e))
    
    def copiar_al_portapapeles(self):
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.contraseña_generada)
            self.root.update()  # Actualiza el portapapeles
            messagebox.showinfo("Copiado", "La contraseña ha sido copiada al portapapeles.")
        except AttributeError:
            messagebox.showerror("Error", "Primero genera una contraseña.")
    
    def guardar_en_archivo(self):
        try:
            if not hasattr(self, 'contraseña_generada'):
                raise AttributeError("Primero genera una contraseña.")
            
            archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
            if archivo:
                with open(archivo, 'a') as f:
                    f.write(f"Contraseña: {self.contraseña_generada}\n")
                messagebox.showinfo("Guardado", "La contraseña ha sido guardada en el archivo.")
        except AttributeError as e:
            messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
app = GeneradorContraseñasApp(root)
root.mainloop()

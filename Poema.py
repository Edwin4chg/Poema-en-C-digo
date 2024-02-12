import tkinter as tk
from PIL import Image, ImageTk, ImageFont

def amor_en_codigo(nombre):
    def escribir_poema():
        texto = f"\nTe quiero, {nombre}, más que a mi código\nEres el bug que me encanta, el algoritmo perfecto\nContigo no hay errores, solo soluciones\nEres mi variable constante, mi función principal\nEres el lenguaje que me habla, el compilador ideal\nCon tus besos me activas, con tus abrazos me optimizas\nEres el código que me inspira, el programa que me completa\n..."
        for i in range(len(texto)):
            poema.insert(tk.END, texto[i])
            ventana.update()
            ventana.after(100)
            if texto[i] == nombre[0]:
                poema.tag_add("nombre", f"1.{i}", f"1.{i+len(nombre)}")
                poema.tag_config("nombre", foreground="#FF1493")

    def centrar_texto():
        poema.tag_configure("center", justify="center")
        poema.tag_add("center", "1.0", "end")

    ventana = tk.Tk()
    ventana.geometry("900x620")
    ventana.title("Poema en código")

    loader = tk.Label(ventana)
    loader.pack(fill=tk.BOTH, expand=True)

    imagen_loader = Image.open("inicio.png")
    imagen_loader = ImageTk.PhotoImage(imagen_loader)

    loader.config(image=imagen_loader)
    loader.image = imagen_loader

    # Fuente
    fuente = ImageFont.truetype("ValentineMemories.otf", 55)

    titulo = tk.Label(ventana, text=nombre, font=(fuente, 45))
    titulo.pack()

    corazon = tk.Label(ventana)
    corazon.pack()

    imagen_corazon = Image.open("fondo.png")
    imagen_corazon = ImageTk.PhotoImage(imagen_corazon)

    corazon.config(image=imagen_corazon)
    corazon.image = imagen_corazon

    poema = tk.Text(ventana, font=(fuente, 16))
    poema.pack()

    # Destruir el loader
    ventana.after(3000, loader.destroy)
    # Escribir poema
    ventana.after(3000, escribir_poema)
    # Centrar
    ventana.after(3000, centrar_texto)

    ventana.mainloop()

# Nombre de Ella
nombre = "******"
# Correr
amor_en_codigo(nombre)

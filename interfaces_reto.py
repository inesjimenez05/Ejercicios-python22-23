from tkinter import *
from tkinter import ttk

from pytube import YouTube


def descargarcancion ():
    url=datosEntrada.get()
    youtube= YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()


ventana= Tk()
ventana.title("Descargar canción")
ventana.geometry("300x100")
ventana.resizable(False, False)
ventana.config(background="turquoise")


datosEntrada= ttk.Entry(ventana)
datosEntrada.place(x=70, y=15)

botonDescargar= ttk.Button(ventana, text="Descargar canción", command= descargarcancion)
botonDescargar.place(x=85, y=65)

label_Titulo=ttk.Label(ventana, text="Introduce la url:")
label_Titulo.place(x=105, y=40 )
label_Titulo.config(background="Ivory", border=2, font=("Arial",10))

ventana.mainloop()
from tkinter import *
from tkinter import ttk

def saludar():

    texto= campoTexto.get()
    textoLabel.set(texto)
    


#Generar la ventana para pintar componentes
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("200x300")
ventana.resizable(width=False, height=False)
ventana.config(background="turquoise")


#Genera lienzo para pintar componentes

frm = ttk.Frame(ventana, padding=10).pack()


#Componentes label y button

textoLabel=StringVar()
textoLabel.set("Hola Tkinter")
LabelTexto= ttk.Label(frm, textvariable=textoLabel)
LabelTexto= ttk.Label(frm, text="Hola Tkinter!", background="Light green", border=5, font=("Arial",15))

LabelTexto.pack()


#Componente cuadro de texto 
campoTexto= ttk.Entry(frm)
campoTexto.pack()


ttk.Button(frm, text="Saludo", command=saludar).pack()

ttk.Button(frm, text="Salir", command=ventana.destroy).pack()


ventana.mainloop()
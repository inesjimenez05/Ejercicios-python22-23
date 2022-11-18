from tkinter import *
from tkinter import ttk

#Generar la ventana para pintar componentes
ventana = Tk()
ventana.title("Primer ejercicio")
ventana.geometry("200x300")
ventana.resizable(width=False, height=False)
ventana.config(background="purple")


#Genera lienzo para pintar componentes

frm = ttk.Frame(ventana, padding=10).pack()


#Componentes label y button
LabelTexto= ttk.Label(frm, text="Hola Tkinter!")
LabelTexto.config(background="Green", border=5, font=("Arial",15))
LabelTexto.pack()

ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()
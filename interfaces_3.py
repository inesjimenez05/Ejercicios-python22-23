from tkinter import *
from tkinter import ttk

def guardar_datos():
    print("Guardado")


ventana = Tk ()
ventana.title ("ALimentos")
ventana.geometry("380x300")
ventana.resizable(False, False)
ventana.config(background="Ivory")


alimentos=ttk.Combobox (ventana,values=["Carne", "Pescado", "Verduras"], state="readonly")
alimentos.place(x=5,y=5)
alimentos.set("Elige un sexo")

alimentos_2=ttk.Combobox (ventana,values=["", "", ""], state="readonly")
alimentos_2.place(x=180,y=5)
alimentos_2.set("Elige un sexo")


boton_guardar= ttk.Button(ventana,text="Guardar", command=guardar_datos)

boton_salir= ttk.Button(ventana, text="Salir", command=ventana.destroy)

boton_guardar.grid(row=4, column=0, pady=25)

boton_salir.grid(row=4, column=1, pady=25)

ventana.mainloop()
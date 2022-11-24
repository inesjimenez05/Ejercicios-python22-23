#Aplicación que pida el nombre de usuario, apellido, teléfono, correo , password y botón de guardar

from tkinter import *
from tkinter import ttk

ventana = Tk ()
ventana.title ("Pedir datos")
ventana.geometry("350x300")
ventana.resizable(False, False)
ventana.config(background="Ivory")

label_titulo=ttk.Label(ventana,text="Inroduce los datos:")


label_usuario=ttk.Label(ventana,text="Usuario:")


entry_usuario= ttk.Entry(ventana)


label_contraseña=ttk.Label(ventana, text="Contraseña")


entry_contraseña=ttk.Entry(ventana)


label_repetirContraseña=ttk.Label(ventana, text="Repetir contraseña: ")



entry_repetirContraseña=ttk.Entry(ventana)



boton_guardar= ttk.Button(ventana,text="Guardar")


boton_salir= ttk.Button(ventana, text="Salir")



label_titulo.grid(row=0, column=0)
label_usuario.grid(row=1, column=0)
entry_usuario.grid(row=1, column=1)
label_contraseña.grid(row=2, column=0)
entry_contraseña.grid(row=2, column=1)
label_repetirContraseña.grid(row=3, column=0)
entry_repetirContraseña.grid(row=3, column=1)
boton_guardar.grid(row=4, column=0)
boton_salir.grid(row=4, column=1)

ventana.mainloop()
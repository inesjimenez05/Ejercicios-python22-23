#Aplicación que pida el nombre de usuario, apellido, teléfono, correo , password y botón de guardar

from tkinter import *
from tkinter import ttk

from tkinter import messagebox

usuario=""
contraseña=""
vUsuario= []
repetircontraseña=""

def guardar_datos():
    usuario= entry_usuario.get()
    contraseña=entry_contraseña.get()
    repetircontraseña=entry_repetirContraseña.get()

    if (contraseña==repetircontraseña):
        vUsuario.append(usuario)
        vUsuario.append(contraseña)
        entry_usuario.delete(0, len(usuario))
        entry_contraseña.delete(0, len(contraseña))
        entry_repetirContraseña.delete(0, len(repetircontraseña))
        messagebox.showinfo("Usuario guardado", f"Usuario {usuario} guardado")

    else:
        messagebox.showerror("Las contraseñas no coinciden", f"usuario {usuario} no guardado")
    
    print(vUsuario)


ventana = Tk ()
ventana.title ("Pedir datos")
ventana.geometry("350x300")
ventana.resizable(False, False)
ventana.config(background="Ivory")

label_titulo=ttk.Label(ventana,text="Inroduce los datos:")


label_usuario=ttk.Label(ventana,text="Usuario:")


entry_usuario= ttk.Entry(ventana)


label_contraseña=ttk.Label(ventana, text="Contraseña")


entry_contraseña=ttk.Entry(ventana, show="*")


label_repetirContraseña=ttk.Label(ventana, text="Repetir contraseña: ")



entry_repetirContraseña=ttk.Entry(ventana, show="*")



boton_guardar= ttk.Button(ventana,text="Guardar", command=guardar_datos)


boton_salir= ttk.Button(ventana, text="Salir", command=ventana.destroy)


sexo=ttk.Combobox (ventana,values=["Hombre", "Mujer"], state="readonly")
sexo.place(x=145,y=160)
sexo.set("Elige un sexo")




label_titulo.grid(row=0, column=0, pady=10)

label_usuario.grid(row=1, column=0, pady=10)
entry_usuario.grid(row=1, column=1, pady=10)

label_contraseña.grid(row=2, column=0, pady=10)
entry_contraseña.grid(row=2, column=1, pady=10)

label_repetirContraseña.grid(row=3, column=0, pady=10,padx=7)
entry_repetirContraseña.grid(row=3, column=1, pady=10)

boton_guardar.grid(row=4, column=0, pady=25)
boton_salir.grid(row=4, column=1, pady=25)

ventana.mainloop()
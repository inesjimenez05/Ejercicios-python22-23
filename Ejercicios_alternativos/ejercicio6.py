import flet as ft

#Aplicacion que sirva para hecer la lista de la compra

def main (page: ft.Page):
    page.title= "FRUTERIA"

    def cambiar_color (e):
        t.value= textField_Nombre.value
        page.update()
    
    t= ft.Text(value="Fruteria", color="blue", size=40)
    page.add(t) 

    t.value="FRUTERIA"
    page.update()

    #Boton:

    bt=ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiar_color)
    page.add(bt)

    #Menu:

    drop_Down_Menu= ft.Dropdown(width=300, options=[ft.dropdown.Option("Fruta")])
    drop_Down_Menu.options.append(ft.dropdown.Option("Carne"))
    drop_Down_Menu.options.append(ft.dropdown.Option("Pescado"))
    page.update()

    #Nombre:

    textField_Nombre= ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    textField_Nombre.focus

    fila=ft.Row(controls=[textField_Nombre,drop_Down_Menu])
    page.add(fila)

ft.app(target=main)
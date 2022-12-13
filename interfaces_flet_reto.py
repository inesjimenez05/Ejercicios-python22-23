import flet as ft

cesta=[]

#Aplicacion que sirva para hecer la lista de la compra

def main (page: ft.Page):
    page.title= "FRUTERIA"


    def añadir(e):
        cesta.append(drop_Down_Menu.value)
        tex2.value=""
        for i in cesta:
            tex2.value+=i + "\n"
        print (cesta)
        page.update()
    
    
    t= ft.Text(value="Fruteria", color="blue", size=40)
    page.add(t) 


    t.value="FRUTERIA"
    page.update()

    #Boton:

    page.add(ft.ElevatedButton("Añadir a la cesta", icon="add", on_click=añadir))

    tex=ft.Text(value="Añadir a la cesta", size=35)
    page.add(tex)

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

    tex2=ft.Text(value="", size=23)
    page.add(tex2)

ft.app(target=main)
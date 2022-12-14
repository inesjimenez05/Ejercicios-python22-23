import flet as ft

cesta=[]


#Aplicacion que sirva para hecer la lista de la compra

def main (page: ft.Page):
    page.title= "FRUTERIA"
    

    def button_clicked(e):

        if c1.value==True:
            cesta.append(c1.label)
        if c2.value==True:
            cesta.append(c2.label)
        if c3.value==True:
            cesta.append(c3.label)
        if c4.value==True:
            cesta.append(c4.label)

        page.snack_bar = ft.SnackBar(ft.Text("Añadido"))
        page.snack_bar.open = True
        
        '''tex2.value=""
        for i in cesta:
            tex2.value+=i'''
        page.update()
        return cesta
        
    def guardar(e):
        page.banner.open = False
        text3.value= f"{textField_Nombre.value} has comprado {cesta}"
        page.update()

    def close_banner(e):
        page.banner.open = False
        page.update()

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.LIGHT_BLUE_50,
        leading=ft.Icon(ft.icons.ADMIN_PANEL_SETTINGS_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text("¿Guardar datos de compra?"),actions=[
            ft.TextButton("Guardar", on_click=guardar),
            ft.TextButton("Cancelar", on_click=close_banner),],)

    def show_banner_click(e):
        page.banner.open = True
        page.update()


    t= ft.Text(value="Fruteria", color="blue", size=40)
    tex2=ft.Text(value="", size=23)
    c1 = ft.Checkbox(label="Fruta", value=False)
    c2 = ft.Checkbox(label="Verdura", value=False)
    c3 = ft.Checkbox(label="Pescado", value=False)
    c4 = ft.Checkbox(label="Carne", value=False)
    b = ft.ElevatedButton("Añadir a la cesta", on_click=button_clicked)
    d=ft.ElevatedButton("Guardar",icon="add",on_click=show_banner_click)
    text3=ft.Text(value="", size=13)

    page.snack_bar = ft.SnackBar(content=ft.Text("Hello, world!"),action="Alright!")


    #Nombre:

    textField_Nombre= ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    textField_Nombre.focus

    dlg = ft.AlertDialog(
        title=ft.Text(value=f"{textField_Nombre.value} has comprado {cesta}"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    fila=ft.Row(controls=[b,d])

    page.add(t,textField_Nombre,fila,c1, c2, c3, c4,tex2,text3,ft.ElevatedButton("Open dialog", on_click=open_dlg))
    
ft.app(target=main)


'''Aplicacion que sirva para hecer la lista de la compra'''

import flet as ft

cesta=[]


def main (page: ft.Page):
    page.title= "FRUTERIA"

    def añadirCesta (src2):
        #Guardar en la lista /cesta/
        if fruta.value==True:
            cesta.append(fruta.label)
            src2=f"/imagenes/fruta.png"
        if verdura.value==True:
            cesta.append(verdura.label)
            src2=f"/imagenes/verdura.png"
        if pescado.value==True:
            cesta.append(pescado.label)
            src2=f"/imagenes/logo.png"
        if carne.value==True:
            cesta.append(carne.label)
            src2=f"/imagenes/logo.png"

        #Funcion imagenes
    def imagenes ():
            
        #Mostrar mesnaje de /articulo añadido en cesta/
        page.snack_bar = ft.SnackBar(ft.Text("Añadido"))
        page.snack_bar.open = True
        page.update()
        return cesta

    def close_banner(e):
        #Cerrar alerta de compra
        page.banner.open = False
        page.update()

    def borrar(e):
        textField_Nombre.value=""
        cesta.clear()
        fruta.value=False
        verdura.value=False
        pescado.value=False
        carne.value=False
        textField_Nombre.clean
        page.update()

    def open_dlg_modal(e):
        #Cerrar aviso /desea guardar?/
        page.banner.open = False
        page.dialog = dlg_modal
        #Mostrar usuario + cesta
        dlg_modal.open = True
        dlg_modal.title=ft.Text(f"Usuario: {textField_Nombre.value}, compra: {cesta}")
        page.update()

    def close_dlg(e):
        #Cerrar aviso al pulsar /cancelar/
        dlg_modal.open = False
        page.update()  

    def guardar(e):
        page.banner.open = True
        page.update()

       

    t= ft.Text(value="Fruteria", color="blue", size=40)
    fruta = ft.Checkbox(label="Fruta", value=False)
    verdura = ft.Checkbox(label="Verdura", value=False)
    pescado = ft.Checkbox(label="Pescado", value=False)
    carne = ft.Checkbox(label="Carne", value=False)
    botonCesta = ft.ElevatedButton("Añadir a la cesta",on_click=añadirCesta,icon=ft.icons.ADD_SHOPPING_CART_ROUNDED)
    botonGuardar=ft.ElevatedButton("Guardar",icon="add",on_click=guardar)
    botonBorrar=ft.ElevatedButton("Borrar",icon="delete", on_click=borrar)

    page.banner = ft.Banner(
    bgcolor=ft.colors.LIGHT_BLUE_50,
    leading=ft.Icon(ft.icons.ADMIN_PANEL_SETTINGS_ROUNDED, color=ft.colors.AMBER, size=40),
    content=ft.Text("¿Guardar datos de compra?"),actions=[
        ft.TextButton("Guardar", on_click=open_dlg_modal),
        ft.TextButton("Cancelar", on_click=close_banner)])

    #Nombre usuario
    textField_Nombre= ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    textField_Nombre.focus

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        on_dismiss=lambda e: print("Dialog dismissed!"),
        actions=[
            ft.TextButton("Cerrar", on_click=close_dlg)])

    #Avatar
    avatar = ft.Stack(
        [
            ft.CircleAvatar(
                foreground_image_url="https://d1csarkz8obe9u.cloudfront.net/posterpreviews/fruit-logo-design-template-80e6d069757f94e82d8f8003edd6238b_screen.jpg?ts=1614334276"
                
            ),
            ft.Container(
                content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=5),
                alignment=ft.alignment.bottom_left,
            ),
        ],
        width=40,
        height=40,
    )

    #Imagenes

    img = ft.Image(
        src=f"/imagenes/logo.png",
        width=100,
        height=100,
    )

    imagen2= ft.Image(
        src2="",
        width=100,
        height=100,
    )


    #Fila botones añadir a cesta & guardar
    fila=ft.Row(controls=[botonCesta,botonGuardar,botonBorrar])
    fila2=ft.Row(controls=[avatar,t])

    #Añadir a página principal
    page.add(fila2,textField_Nombre,fila,fruta, verdura, pescado, carne,img,imagen2)
    
ft.app(target=main, assets_dir="imagenes"
)
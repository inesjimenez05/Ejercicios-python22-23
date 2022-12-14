import flet as ft

def main(page: ft.Page):

    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Añadir a la cesta"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Eliminar"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Guardar",
            ),
        ]
    )
    page.add(ft.Text("Body!"))

ft.app(target=main)
import flet as ft

def main(page: ft.Page):
    page.title = "AlertDialog examples"

    dlg = ft.AlertDialog(
        title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dlg)
    )

ft.app(target=main)
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
        
        tex2.value=""
        for i in cesta:
            tex2.value+=i
        page.update()
        
    def guardar(e):

        text3.value= f"{textField_Nombre.value} has comprado {tex2.value}"
        page.update()


    t= ft.Text(value="Fruteria", color="blue", size=40)
    tex2=ft.Text(value="", size=23)
    c1 = ft.Checkbox(label="Fruta", value=False)
    c2 = ft.Checkbox(label="Verdura", value=False)
    c3 = ft.Checkbox(label="Pescado", value=False)
    c4 = ft.Checkbox(label="Carne", value=False)
    b = ft.ElevatedButton(text="Añadir a la cesta", on_click=button_clicked)
    d = ft.ElevatedButton(text="Guardar", icon="add", on_click=guardar)
    text3=ft.Text(value="", size=13)

    #Nombre:

    textField_Nombre= ft.TextField(label="Nombre",hint_text="Escribe tu nombre")
    textField_Nombre.focus

    fila=ft.Row(controls=[b,d])

    page.add(t,textField_Nombre,fila,c1, c2, c3, c4,tex2,text3)
    
ft.app(target=main)
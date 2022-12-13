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
            tex2.value+=i  + "\n"
        print (cesta)
        page.update()

    t= ft.Text(value="Fruteria", color="blue", size=40)
    tex2=ft.Text(value="", size=23)
    c1 = ft.Checkbox(label="Fruta", value=False)
    c2 = ft.Checkbox(label="Verdura", value=False)
    c3 = ft.Checkbox(label="Pescado", value=False)
    c4 = ft.Checkbox(label="Carne", value=False)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(t,c1, c2, c3, c4, b,tex2)

    
ft.app(target=main)
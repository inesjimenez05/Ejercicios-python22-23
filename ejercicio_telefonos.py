#Función que pinta el menú del 1 al 5


def menuNumeros():
    num=9
    while(num<1 or num>5):
        print("1. Insertar contacto")
        print("2. Borrar contactos")
        print("3. Buscar contactos")
        print("4. Ver todos los contactos")
        print("5. Salir del programa")
        try:
            num=int(input("Di un numero : "))
        except:
            print("Introduce un numero valido")

menuNumeros()
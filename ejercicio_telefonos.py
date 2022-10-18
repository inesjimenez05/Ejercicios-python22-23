#Función que pinta el menú del 1 al 5

def menuNumeros():
    num=3

    while(num<1 or num>5):
        print("1. Insertar contacto")
        print("2. Borrar contactos")
        print("3. Buscar contactos")
        print("4. Ver todos los contactos")
        print("5. Salir del programa")
        try:
            num=int(input("Di un número: \n"))
        except:
            print("Dime un numero del 1 al 5")
    return num

num=menuNumeros()
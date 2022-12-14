num=0
while (num<1 or num>5):
    try: 
        print("1. Insertar contacto")
        print("2. Borrar contactos")
        print("3. Buscar contactos")
        print("4. Ver todos los contactos")
        print("5. Salir del programa")
        num=int(input("Di un numero: "))

    except:
        print("Tienes que introducir números")
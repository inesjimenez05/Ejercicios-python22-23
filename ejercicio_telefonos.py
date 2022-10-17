vContactos=[]
num=3
while(num!=5):

    print("1. Insertar contacto")
    print("2. Borrar contactos")
    print("3. Buscar contactos")
    print("4. Ver todos los contactos")
    print("5. Salir del programa")

    try:
        num=int(input("Diga un numero: \n"))
    except:
        print("Las opciones son de la 1 a la 5")
    
    '''
    if(num==1):
        print("Insertar contacto")
    if(num==2):
    '''
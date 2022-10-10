'''
Opción 1
Lista para nombres
Lista para teléfonos

'''

'''
Opción 2
Lista para nombres y teléfonos
Ejemplo (Juan - Teléfono)

'''

#Opción 1

vNombres=[]
vTelefonos=[]


nombre=(str)(input("Dime un nombre \n"))
telefono=(int)(input("Dime un número \n"))

vNombres.append(nombre)
vTelefonos.append(telefono)

print(vNombres.pop(0), "-", vTelefonos.pop(0))


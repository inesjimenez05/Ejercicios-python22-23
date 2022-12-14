'''
Ejercicio 20
Mostrar en pantalla los N primeros número primos. Se pide por teclado la cantidad
de números primos que queremos mostrar
'''

def primos(num):
    for i in range (2,num):
        if (num%i==0):
            return False
    return True

cantidadnumeros=int(input("Cantidad de numeros a mostrar: "))
vNumprimos=[]

for i in range (1,cantidadnumeros+1):
    if primos(i):
        vNumprimos.append(i)

print(vNumprimos)
    


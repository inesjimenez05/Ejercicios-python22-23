'''
Requerir al usuario que ingrese un número entero e
informar si es primo o no, utilizando una función booleana que lo decida.
'''


def numPrimo(num:int):
    for i in range (2,num):
        if num%i==0:
            return False
    return True
             

numero=int(input("Ingresa un numero entero: "))

if numPrimo(numero):
    print ("Es primo")
else:
    print ("No es primo")

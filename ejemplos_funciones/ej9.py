'''
Requerir al usuario que ingrese un número entero e
informar si es primo o no, utilizando una función booleana que lo decida.
'''

def primos(num):
    for i in range (2,num):
        if (num%i==0):
            return(False)
    return(True)

num=int(input("Dime un numero: "))

if primos(num):
    print(f"Es primo")
else:
    print("No es primo")
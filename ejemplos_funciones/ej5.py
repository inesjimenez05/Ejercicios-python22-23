'''
Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de 
dígitos fue mayor y la cantidad de números cuya sumatoria de 
dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.
'''

def sumadigitos(num:int):
    sumadigitos= (int(num/10)+(num%10))
    return(sumadigitos)

numero=1
vlista=[]
mayor=0
menor=0

while numero>0:
    numero=int(input("Dime un numero: "))
    vlista.append(sumadigitos(numero))

    if sumadigitos(numero)>10:
        mayor+=1
    else:
        menor+=1
    
print(max(vlista))
print (f"{menor} numeros cuya suma es menor a 10, {mayor} numeros cuya suma es mayor4 a 10")

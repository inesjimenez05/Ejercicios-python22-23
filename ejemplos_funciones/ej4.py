'''
Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, 
al finalizar, la cantidad total de números leídos en total.
Utilizar una o más funciones, según sea necesario.
'''

def factorial(num:int):
    factorial=1
    for num in range (1,num+1):
        factorial*=num
    
    return(factorial)



num=0
contador=0

while num!=-1:
    num=int(input("Número (-1 para cortar): "))
    print(factorial(num))
    contador+=1

print(f"Se han leido {contador} numeros")

'''
Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando 
ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. 
También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número 
(frecuencia).
 Al finalizar el programa, mostrar el factorial del mayor número ingresado.
 '''

def primos (numero:int):
    vNum=[]
    for i in range(2,numero):

        if (numero%i==0):
            return False
    return True

num=3
vLista=[]
while(primos(num)):
    num=int(input("Di un numero: "))
    vLista.append(num)

print(vLista)




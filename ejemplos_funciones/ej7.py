'''
Ejercicio 8
Escribe un programa que pida el limite inferior y superior de un 
intervalo. Si el límite inferior es mayor que el superior lo tiene 
que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos
el 0.
Cuando termine el programa dará las siguientes informaciones:
1 La suma de los números que están dentro del intervalo 
  (intervalo abierto).
2 Cuantos números están fuera del intervalo.
3 He informa si hemos introducido algún número igual a los límites 
del intervalo
'''

limitesuperior=0
limiteinferior=2

while limiteinferior>limitesuperior:
    try:
        limiteinferior=int(input("Introduce el limite inferior: "))
        limitesuperior=int(input("Introduce el limite superior: "))
    
    except:
        print("Introduce un numero valido \n")

def pedirNumeros ():
    vNum= []
    num=2
    while num!=0:
        num=int(input("Di un numero: "))    
        vNum.append(num)
    return(vNum)

def operacionesLimites(limitesuperior,limiteinferior,vNumeros):
    listaNum=list(range (limiteinferior+1,limitesuperior))
    i=0
    suma=0
    numigual=0
    numfuera=0
    numdentro=0
    for i in (vNumeros):

        if i in (listaNum):
            suma+=i
            numdentro+=1
        
        else:
            numfuera+=1

        if (i==limiteinferior or i==limitesuperior):
            numigual+=1
        
    
    print(f"Hay {numdentro} numeros dentro, {numfuera} numeros fuera y la suma: {suma}")



vNumeros=pedirNumeros()
operacionesLimites(limitesuperior, limiteinferior, vNumeros)
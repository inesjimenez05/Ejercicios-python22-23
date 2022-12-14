'''
Calcular un menu que calcule la ecuacion de segundo grado
'''

def pedirDatos ():
    #ax2+bx+c
    vDatos=[]
    a=int(input("Dime el valor de a: "))
    b=int(input("Dime el valor de b: "))
    c=int(input("Dime el valor de c: "))
    vDatos.append(a)
    vDatos.append(b)
    vDatos.append(c)

    return(vDatos)

def fdeterminante(numero):
    a=numero[0]
    b=numero[1]
    c=numero[2]
    determinante= (b**2)-(4*a*c)
    return(determinante)


numero=3

while (numero!=2):
    print("¿Quieres calcular la ecuación?")
    print("1.Sí")
    print("2-No")
    numero=int(input(""))
    if numero==1:
       lista=pedirDatos()
       det=fdeterminante(lista)
       if det<0:
            print("La raíces no son reales")
       else:
            solucion1= (-lista[1]+(det)**(1/2))/(2*lista[0])
            solucion2= (-lista[1]-(det)**(1/2))/(2*lista[0])
            print(f"Solución 1: {solucion1}, solución 2: {solucion2}")


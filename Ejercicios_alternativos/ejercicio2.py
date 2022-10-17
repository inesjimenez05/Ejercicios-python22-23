#2_Algoritmo que pida un número y diga si es positivo, negativo o 0.

num=0

num=(int)(input("Di un número \n"))

if(num<0):
    print("El número ",num,"es negativo")
elif(num==0):
    print("El número es 0")
else:
    print("El número ",num,"es positivo")
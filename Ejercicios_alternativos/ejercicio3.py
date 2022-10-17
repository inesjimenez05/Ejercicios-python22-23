#3_Escribe un programa que lea un número e indique si es par o impar.

num=0

num=(int)(input("Di un número \n"))

if(num%2!=0):
    print("El número ", num,"es impar")
else:
    print("El número ", num, "es par")
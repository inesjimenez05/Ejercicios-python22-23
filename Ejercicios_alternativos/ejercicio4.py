#4_Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1=0
num2=0

num1=(int)(input("Di un número \n"))
num2=(int)(input("Di un número \n"))

if(num2!=0):
    print(num1/num2)
else:
    print("Aviso, no se puede dividir entre 0")
#ejercicio contraseña con intentos

codigo= "hola"
valor=""
intentos=0

while(intentos <= 2):
    intentos = intentos + 1 
    print("Error repita la contraseña")
    valor=input("Diga la contraseña \n")
    if(codigo == valor ):
       intentos=4
       print("Contraseña correcta")
       
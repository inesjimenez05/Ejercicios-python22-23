#5_Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error._

usuario=""
contraseña=""

usuario=input("Di el usuario \n")
contraseña=input("Di la contraseña \n")



'''if(usuario!="pepe"):
    print("Error vuelve a introducir el usuario y la contraseña")
elif(contraseña!="asdasd"):
    print("Error vuelve a introducir el usuario y la contraseña")
else:
    print("Has entrado al sistema")
'''
while(usuario!="Pepe" and contraseña!="asdasd"):
    print("Error vuelve a introducir el usuario y la contraseña")
    usuario=input("Di el usuario \n")
    contraseña=input("Di la contraseña \n")
print("Has entrado al sistema")


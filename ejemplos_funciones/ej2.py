'''
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección 
es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si 
contiene el símbolo "@"
'''

def pideGmail ():
    gmail=input("Di el gmail: ")

    if "@" in gmail:
        print (f"¨{gmail} Es valida")
    else:
        print (f"¨{gmail} No es valida")


pideGmail()

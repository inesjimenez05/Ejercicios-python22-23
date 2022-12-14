#2_Calcular el perímetro y área de un rectángulo dada su base y su altura.

def pedirArea (base,altura):
    area=base*altura
    return(area)

def pedirPerimetro(base,altura):
    perimetro=(2*base)+(2*altura)
    return(perimetro)

def pedirAreaYPerimetro(base,altura):
    area=pedirArea(base,altura)
    perimetro=pedirPerimetro(base,altura)
    areayperimetro=[]
    areayperimetro.append(area)
    areayperimetro.append(perimetro)
    return(areayperimetro)

base=int(input("Base: "))
altura=int(input("Altura: "))
vNumeros=pedirAreaYPerimetro(base,altura)
print(f"El area es {vNumeros[0]} y el perimetro {vNumeros[1]}")
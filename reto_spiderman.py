from ast import If


puntoa=0
puntob=0
distancia=0

puntoa= (int)(input("Dime la distancia del punto A \n"))
puntob= (int)(input("Dime la distancia del punto B \n"))

if (puntoa > 0) and (puntob >0):
    print("distancia=",  (puntoa + puntob)*2)

elif (puntoa < 0) and (puntob <0):
    puntoa= abs(puntoa) 
    puntob= abs(puntob)
if(puntoa>puntob):
    print("Distancia=", (puntob*2)+puntoa)
else:
    print("Distancia=", (puntoa*2)+puntob)
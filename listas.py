#listas Python ej.
#Definición e incialización

vNombres=[]

#Insertar un dato
vNombres.insert(0,"Juan")
vNombres.insert(1,"Pepe")
vNombres.insert(2,"Inés")
vNombres.append("Minerva") #Final lista
vNombres.insert(1,"Julián")

#Eliminar elementos
vNombres.remove("Pepe")

#Ordenar una lista
vNombres.sort(reverse=True)

#Contar nº elementos
print("El número de veces que aparece Inés es:", vNombres.count("Inés"))
print("La lista tiene: ", len(vNombres))

print(f"El nombre borrado es {vNombres.pop(1)}")
print(vNombres)
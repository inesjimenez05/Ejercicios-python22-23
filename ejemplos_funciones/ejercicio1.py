'''
Producto de los n primeros numeros pares
'''
num=int
producto=1

for i in range (1,7):
    if (i%2==0):
        producto*=i

print(producto)
import math
import random 
lista =[]
sum=0
cont=0
mayor=0
menor=100000 
moda= 0
media=0
resta=0
cuadrado=2
division= 0
rep=0
tam = random.randint (10,20)
print (tam)
def llenarLista(tam,rango):
    for i in range (tam):
        num=random.randrange (100)
    lista.append (num)
print (lista )

for i in lista:
        sum+=i
        cont+=1
if i > mayor:
        mayor= i
if i < menor:
        menor = i
if i in lista:
        sum/cont
print ("La suma es: ",sum)


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
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista
l1=llenarLista(5,20)
print(l1)

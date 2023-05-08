import random

lista=[]

lista2=[]

cont=0

sum1=0

sum2=0

mayor=0

menor=10000

promedio1=0

promedio2=0

pares1=0

pares2=0

impares1=0

impares2=0

f = random.randint (10,20)
print (f)

for f in range (f):
    num=random.randrange (25)
    lista.append (num)
print (lista )

for f in lista:
    sum1 = sum1 + f
    cont+=1
    if f % 2 == 0:
        pares1 += 1
    else:
        impares1 += 1
   
print ('La suma de la lista es: ',sum1)

for f in lista:
    if f > mayor: 
        mayor = f
    if f < menor:
        menor = f

promedio1=sum1/len(lista)

print ('El numero mayor de la lista es: ',mayor)
print ('El numero menor de la lista es: ',menor)
print('El promedio de la lista es: ',promedio1)

if f % 2 == 0:
    print ('Cantidad de numeros pares: ',f)
else:
    print ('Cantidad de numeros impares: ',f)

a = random.randint (20,30)
print (a)

for a in range (f):
    num=random.randrange (35)
    lista2.append (num)
print (len(lista2))
print (lista2)

for a in lista2:
    sum2 = sum2 + a
    cont+=1
    if a % 2 == 0:
        pares2 += 1
    else:
        impares2 += 1

print ("La suma de la lista 2 es: ",sum2)

if sum1 > sum2:
    print ('La suma mayor entre las dos es lista: ',sum1)
else:
    print ('La suma mayor entre las dos es lista 2: ',sum2)

for a in lista2:
    if a > mayor: 
        mayor = a
    if a < menor:
        menor = a

promedio2=sum2/len(lista2)

print ('El numero mayor de la lista 2 es: ',mayor)
print ('El numero menor de la lista 2 es: ',menor)
print ('El promedio de la lista 2 es: ',promedio2)

promedioConjunto = (promedio1 + promedio2)/2
print ('El promedio conjunto es: ',promedioConjunto)

if pares1 < pares2:
    print ('La lista 2 tiene mas pares que la lista: ', pares2)
else: 
    print ('La lista tiene mas pares que la lista 2: ', pares1)

if impares1 < impares2:
    print ('La lista 2 tiene mas impares que la lista: ', impares2)
else: 
    print ('La lista tiene mas impares que la lista 2: ', impares1)

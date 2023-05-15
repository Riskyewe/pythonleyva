import random

def llenList(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for a in range(tam)]
    return lista

def sumList(lista):
    sum=0
    for b in lista:
        sum+=b
    return sum

def promList(lista):
    return sumList(lista)/len(lista)

def mayorLista(lista):
    mayor=0
    for a in lista:
        if a > mayor:
            mayor = a
    return mayor
        
def menorLista(lista):
    menor=10000
    for a in lista:
        if a < menor:
            menor = a
    return menor

def modaLista(lista):
    cont=0
    rep=0
    for modaLista in lista:
        for a in lista:
            if modaLista == a:
                cont+=1
            if cont > rep:
                modaLista= a
    return modaLista

def ascendenteLista(lista):
    auxiliar=0
    for a in range(len(lista)):
        for c in range (a+1,len(lista)):
            if lista[a]>lista[c]:
                auxiliar=lista[a]
                lista[a]=lista[c]
                lista[c]=auxiliar
    return lista

def descendenteLista(lista):
    auxiliar=0
    for a in range(len(lista)):
        for c in range (a+ 1,len(lista)):
            if lista[a]<lista[c]:
                auxiliar=lista[a]
                lista[a]=lista[c]
                lista[c]=auxiliar
    return lista
   
def medianaLista(lista):
    mediana=(len(lista))
    if mediana % 2==0:
        medianaLista = (lista[mediana//2-1]+lista[mediana//2])/2
    else:
        medianaLista=lista[mediana//2]
    return medianaLista

list1=llenList(10,15)
print(list1)

print("La suma de la lista es: ", sumList(list1))

print("El promedio de la lista es: ", promList(list1))

print("El número mayor de la lista es:" , mayorLista(list1))

print("El número menor de la lista es: " ,menorLista(list1))

print("La moda de la lista es: ", modaLista(list1))

print("Forma ascendente: ", ascendenteLista(list1))

print("La forma descendente: ", descendenteLista(list1))

print("La mediana de la lista es: ", medianaLista(list1))

#:3

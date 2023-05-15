import random

def llenList(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for a in range(tam)]
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def compararSumas(list1,list2):
    if sumaLista(list1) > sumaLista(list2):
        print ('La suma mayor entre las dos es lista: ',list1)
    else:
        print ('La suma mayor entre las dos es lista 2: ',list2)
    return list1,list2
    


list1=llenList(10,15)
list2=llenList(10,15)
print(list1)
print(list2)
print(sumaLista(list1))
print(sumaLista(list2))
print(compararSumas(list1,list2))



import random

tamaño_lista = random.randint(10, 20)

lista_icfes = [random.randint(100, 500) for _ in range(tamaño_lista)]

lista_icfes.sort()

cuartil_1 = lista_icfes[int(len(lista_icfes) * 0.25)]
cuartil_2 = lista_icfes[int(len(lista_icfes) * 0.50)]
cuartil_3 = lista_icfes[int(len(lista_icfes) * 0.75)]

quintil_1 = lista_icfes[int(len(lista_icfes) * 0.20)]
quintil_2 = lista_icfes[int(len(lista_icfes) * 0.40)]
quintil_3 = lista_icfes[int(len(lista_icfes) * 0.60)]
quintil_4 = lista_icfes[int(len(lista_icfes) * 0.80)]

print(tamaño_lista)
print(lista_icfes)

print("Cuartiles:")
print(cuartil_1, cuartil_2, cuartil_3)

print("Quintiles:")
print(quintil_1, quintil_2, quintil_3, quintil_4)

listCuartil=cuartil_1,cuartil_2,cuartil_3
listQuintil=quintil_1,quintil_2,quintil_3,quintil_4

def cuartil(lista_icfes):
    formula=0
    n = len (lista_icfes)
    listaCuartil=[]
    formula2=0
    for k in range(1, 4):
        if len( lista_icfes) % 2!=0:
            formula=(k*(n+1)) / 4
            formula2=round(formula)
            posicion=lista_icfes [formula2-1]
            print(f"Q{k} = posicion {formula} valor en lista {posicion}")
            listaCuartil.append(formula)
            print(listaCuartil)
            
        else:
            formula = (k*n)/4
            conv=round(formula)
            posicion= lista_icfes[formula2]
            print(f"Q{k} = {formula} en lista {posicion}")
            listaCuartil.append(formula)
            print(listaCuartil)
print(cuartil(lista_icfes))

def quintil(lista_icfes):
    formula=0
    tamaño = len(lista_icfes)
    listaCuartil=[]
    formula2=0
    for b in range(1, 5):
        if len(lista_icfes) % 2!=0:  
            formula=(b*(tamaño+1)) / 5
            formula2=round(formula)
            pos=lista_icfes[formula2-1]
            print(f"k{b} = posicion {formula} valor en lista {pos}")
            listaCuartil.append(formula)
            print(listaCuartil)
        else:
            formula = (b*tamaño)/5
            conv=round(formula)
            print(f"k{b} = {formula}")
            listaCuartil.append(formula)
            print(listaCuartil)
            
print(quintil(lista_icfes))       
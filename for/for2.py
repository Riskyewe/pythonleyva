primero=int(input("Ingrese el número con el que quieres comenzar: "))
segundo=int(input("Ingrese el número con el que quieras acabar la lista: "))
tercero=int(input("Ingrese el número con el que quieres incrementar y para decrementar escribe el número en negativo "))
for j in range (primero, segundo, tercero):
    if j%primero==0:
        print(j, "Es multiplo de ", primero)
    else:
        print(j)
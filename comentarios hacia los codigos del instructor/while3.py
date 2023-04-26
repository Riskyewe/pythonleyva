n=int(input('ingrese numero'))
#Se debera ingresar un numero para la variable n la cual debe ser un entero
i=1
#La variable de i es 1 el cual es un contador
while i<n:
#Mientras que el contador sea menor que el numero de la variable n:
    if i%7==0:
#Si el numero de la lista es 7 o su residuo termine en 0 se imprimira el print de la linea 9
        print(f'{i} es multiplo de 7')
#Se muestra el print de la lista
    else:
        print(i)
    i+=1
#El contador aumenta con cada iteracion
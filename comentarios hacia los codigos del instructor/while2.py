x,y=3,5
#Los valores de las variables
cont=1
#El contador empieza desde 1
while not(x%y==0 or y%x==0):
#Aqui se crea un While con los valores de las variables anteriormente escritas y se les sacara el promedio sin importar el orden
    print(f'intento numero {cont}')
#Se imprime la cantidad de intentos que haga el usuario
    x=int(input('ingrese numero'))
    y=int(input('ingrese numero'))
#Ingresar el valor de las variables
    cont+=1
#Mientras mas veces el usuario intente, mas el numero de intentos aumentara
print(f'{x} y {y} son factor')
#Se imprimira los dos numeros que son factores
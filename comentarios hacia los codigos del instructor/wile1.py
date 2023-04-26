# num=1
# print(type(num))
# num="sena"
# print(type(num))
num=1
cont=0
sum=0
menor=1000000
mayor=0
#Aqui estan las variables 
while num!=0:
    num=int(input('ingrese numero'))
#El usuario tendra que digitar varios numeros hasta que digite un 0 y empezara con una suma
    cont=cont+1
    sum=sum+num
#Despues con el promedio de la suma
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num
#Y finalemnte seleccionando el numero mayor y el numero menor de la lista de digitos que escribio el usuario
print(f'fueron ingresados {cont-1} numeros')
#Se mostraran los numeros digitados
print(f'La suma es {sum}')
#Se mostrara la suma de los numeros digitados
print(f'El promedio es {sum/(cont-1)}')
#Se mostrara el promedio de la suma de los numeros digitados
print(f'El mayor es {mayor}')
#Se mostrara el numero mayor de la lista
print(f'El menor es {menor}')
#Se mostrara el numero menor de la lista

numeros = input("Ingrese una lista de números separados por comas: ")
numeros_lista = numeros.split(",")
suma = 0
for numero in numeros_lista:
    suma += int(numero)
print("La suma de los números es", suma)

x=int(input('ingrese numero'))
y=int(input('ingrese numero'))
z=int(input('ingrese numero'))
#indentación
if x>y:
    if x>z:
        print(f'el mayor es {x}')
    else:
        print(f'el mayor es {z}')
else:
    if y>z:
        print(f'el mayor es {y}')
    else:
        print(f'el mayor es {z}')

#Aqui se mostrara por base de inputs, prints y los simbolos '<>' cual es el mayor numero de los 3 sin usar otras funciones.

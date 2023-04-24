primero=int(input("Digitar el primer número: "))
segundo=int(input("Digitar el segundo número: "))
tercero=int(input("Digitar el tercer número"))

print("Los números son: ",primero,",",segundo,",",tercero)

if (primero>segundo<tercero):
 print("El número ", primero," Es el número mayor")
elif(primero<segundo>tercero):
    print("El número ", segundo," Es el número mayor")
elif(primero<segundo<tercero):
    print("El número ", tercero, " Es el número mayor")
    
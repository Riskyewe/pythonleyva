numero1,numero2=100,50
print("1-sumar")
print("2-restar")
print("3-multiplicar")
print("4-dividir")
print("5-residuo")
op=int(input("qué operacion?"))
match op:
    case 1:
        print(numero1+numero2)
match op:
    case 2:
        print(numero1-numero2)
match op:
    case 3:
        print(numero1*numero2)
match op:
    case 4:
        print(numero1/numero2)
match op:
    case 5:
        print(numero1%numero2)        
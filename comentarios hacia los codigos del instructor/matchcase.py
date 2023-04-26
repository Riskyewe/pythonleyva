num1,num2=100,50
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
op=int(input('que operacion?'))
match op:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)# //  /
    case 5:    
        print(num1%num2)
#En este por medio de la funcion "del" y "caso" se pueden hacer varias operaciones matematicas sin tener que usar tantos if y elif, en este se pueden ver que operacion quiere el ususario y al elegir un numero el programa hara aquella operacion sin pasar por las otras.

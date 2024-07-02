
num1 = int(input('digita un numero: '))
num2 = int(input('digita otro numero: '))

if num1 == num2:
    print('los numeros son iguales')
elif num1 > num2:
    print(f'{num1} es mayor que {num2}')
else:
    print(f'{num2} es mayor que {num1}')
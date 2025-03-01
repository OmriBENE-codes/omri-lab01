#Custom Modulo Function

def custom_modulo():
    num1 = int(input('please enter a number you want to modulo: '))
    num2 = int(input('please enter a number you want as divisor: '))
    answer = num1 - num2 * (num1 // num2)
    print(f'the answer is: {answer} ')

custom_modulo()
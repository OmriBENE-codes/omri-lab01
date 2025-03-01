#Custom Exponentiation Function 
def Exponentiation():
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number as an exponent: "))
        num3 = pow(num1,num2)
        print(f'The solution is {num3}.')
        
Exponentiation()
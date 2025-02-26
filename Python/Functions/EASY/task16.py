#Find the Remainder

def Find_remainder():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num2 > num1:
        print("Please enter the higher number first.")
    else:    
        print(f" {num1 % num2} ")
    
Find_remainder()
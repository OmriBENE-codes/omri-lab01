import math
num1 = int(input('Enter a number to check if its prime: '))


if (num1 <=1):
    print(f'{num1} - Is not a prime number.\n')
else:
    is_prime = True
    if (num1 % 2 == 0): #Handle edge cases
            print(f'{num1} - Is not a prime number.\n')
    elif num1 == 2: #2 is a prime number
        print(f"{num1} is a prime number.\n")
    else:
        is_prime = True #Check divisibility up to the square root of num1
        for i in range(3, int(math.sqrt(num1)) + 1, 2): #Only check odd numbers
            if num1 % i == 0:
                is_prime = False
                break      
    if is_prime:
        print(f"{num1} is a prime number.\n")
    else:
        print(f'{num1} - Is not a prime number.\n')

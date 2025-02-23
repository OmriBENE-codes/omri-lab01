#Tuple Basics
tuple = ()
num1 = int(input("enter the length of the tuple: "))
for i in range(num1):
    num1 = input('Enter a number: ')
    num3 = int(num1) #converts the unput into integer
    tuple += (num3,) #adds the integers to the tuple

print(f"The tuple is: {tuple}" )

#Prime Factorization
import math
def factorize():
    num1 = int(input("enter a number: "))
    while num1 % 2 ==0:
        print(2)
        num1  //= 2
    #n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(num1))+1,2):
        while num1 % i ==0:
            print(i)
            num1 //= i
        
    if num1 > 2:
            print(num1)

factorize()
#Fibonacci sequence
def Fibonacci_sequence(s):
    fib_sequence = [] #creates an empty list
    a , b = 0 , 1 #variables 
    for i in range(s):
        fib_sequence.append(a) #adds a number to the list  
        a , b = b, a + b  #Update a and b for the next Fibonacci numbers
    return fib_sequence

print(Fibonacci_sequence(10)) #my input request
#miltipule functions 



def greet(name):
    return f"Hello, {name}! Welcome!"

def countdown(num):
    for i in range(num, -1 , -1):  
        print(i)

def string_slice(word):
    for i in range(len(word)):
        print(f"{word[i]},")
        
    
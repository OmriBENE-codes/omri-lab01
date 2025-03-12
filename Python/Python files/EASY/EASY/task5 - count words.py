#Counting Words in a File 
with open('example.txt', "r") as file:
    data = file.read() #using the read() function and storing them in a new variable
    lines = data.split() #Splitting the data into separate lines
    count = len(lines) #the length of the lines as words.

print(count)


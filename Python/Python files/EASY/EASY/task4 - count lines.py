#Counting Lines in a File
with open('example.txt', "r") as file:
    lines = len(file.readlines()) #using length to mesure how many lines there are in the file
    print(f"This file has {lines} lines. ")

#Reading a File Line by Line 
import os

def read_lines():
    file_name = input("Enter the path of the file to read: ")
    if not os.path.isfile(file_name): #check if the file exists and stops if not.
            print(f"The file '{file_name}' does not exist.")
            return
    
    with open(file_name, 'r') as file:
        for line in file:
            print(line, end='')# prints a line with space


read_lines()
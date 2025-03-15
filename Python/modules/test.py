from simple_module import greet #importing the function from another file
from import_specific import string_slice 
import module_alias as game #imports the module_alias module and gives it the alias game
import sys

sys.path.append('./modules/files')
import module
print(module.countdown(input('enter a number: ')))




# name = input('Enter your name: ')
# message = greet(name) #new variable containing the function and requested variable
# print(message) #print said variable

# greeting = game.genre("action", "survival")
# print(greeting)


# print("----------------------")
# word = input("Enter a word to slice:")
# slice = string_slice(word)
# print(slice)
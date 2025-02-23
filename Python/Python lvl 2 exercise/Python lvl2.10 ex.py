#Palindrome Checker 
def is_palindrom(s):
    #function that flips a string and check if its the same (palindrom)
    return s ==s[::-1] 

pali = input("Please enter a sentence here to see if its a palindrom: ")
if is_palindrom(pali): #the string goes through the function above.
    print(f"{pali} is a palindrom!")
else:
    print(f"{pali} is not a palindrom.")

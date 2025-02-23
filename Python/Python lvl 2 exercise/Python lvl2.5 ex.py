#Dictionary Manipulation

dictionary_manipulation = {}

while True:
    key = input("Wold you like to enter a key or stop? (key name \ stop) ")
    if key == "stop":
        print("Stopping..")
        break
    else:
        value = input(f"Enter a value for {key}: ")
        dictionary_manipulation[key] = value
print(f"your dictionary is: {dictionary_manipulation}")
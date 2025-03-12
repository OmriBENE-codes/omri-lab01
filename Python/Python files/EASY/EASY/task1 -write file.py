#write a file

def text_file():
    file = open("example.txt", "a")
    while True:
        data = input("\nEnter what you want to the file: ")
        file.write(data)
        cont = input('Would you like to stop? (yes/no): ')
        if cont == 'yes': break
    file.close()




text_file()

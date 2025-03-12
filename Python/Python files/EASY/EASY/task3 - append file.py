#Appending to a File 

append_file = open('example.txt', 'a')
while True: #loop for entering a text into the file.
        append_file.writelines(input('Add Text here to the file: ')) #writing lines into text
        append_file.write(' ') #giving an \n to the lines.
        cont = input('Would you like to stop? (yes/no): ')
        if cont == 'yes': break
append_file.close()
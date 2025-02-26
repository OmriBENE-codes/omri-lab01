#Find the Maximum

def find_max():
    num_list = []
    for num in range(3):
        num = int(input('Enter a number: '))
        num_list.append(num)
    print(num_list)
    print(f'the largest number in the list is: {max(num_list)}')
    

find_max()
    

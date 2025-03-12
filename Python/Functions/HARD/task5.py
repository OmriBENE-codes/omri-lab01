#Find Missing Number

num_list = []
new_list= []
def miss_number():
    for num1 in range(5):
        num1 = int(input("add 5 numbers to the list,\n the list must be consecutive with one number missing: ")) 
        num_list.append(num1)
        num_list.sort()
    print(f'The list now is {num_list}')

    for i in range(len(num_list) -1):    
        if num_list[i] +1 != num_list[i +1]:
            new_list = num_list[:i+1] + [num_list[i]+1] + num_list[i+1:]
            break
    print(new_list)

miss_number()

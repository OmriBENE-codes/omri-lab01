#Custom Sorting Algorithm 

def custom_sort():
    sort_list = []
    new_list = []
    for num1 in range(10):
        num1 = int(input("add a number to the list: "))
        sort_list.append(num1)
        print(sort_list)
    
    while sort_list: # Continue as long as the original list is not empty
        min_num = min(sort_list)
        new_list.append(min_num)
        sort_list.remove(min_num) # Remove the minimum value from the original list
        print(new_list)

custom_sort()

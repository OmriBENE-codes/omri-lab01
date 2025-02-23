num1_list = []
num2_list = []
for i in range(3):
    num1 = int(input('Please enter series of numbers: '))
    num1_list.append(num1) 
for j in range(3):
    num2 = int(input('Please enter series of numbers: '))
    num2_list.append(num2) 
set1 = set(num1_list)
set2 = set(num2_list)
print(f"The first list: {num1_list}")
print(f"The second list: {num2_list}")
union = list(set1| set2)
intersection = list(set1 & set2)
difference = (set1 - set2)
print(f"The union of all lists is:  {union}")
print(f"The intersection of all lists is: {intersection}")
print(f"The difference of all lists is:  {difference}")
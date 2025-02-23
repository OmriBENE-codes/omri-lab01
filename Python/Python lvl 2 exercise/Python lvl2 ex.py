#converts temperature from Celsius to Fahrenheit and vice versa
Celsius = 0
Fahrenheit = 0
Convert_choice=input('Select a temperature you like to convert to: Celsius\Fahrenheit ')
if Convert_choice == Celsius:
    Celsius = float(input('Please enter the temperature: '))
else:
    Fahrenheit = float(input('Please enter the temperature: '))

Formula_Fahrenheit = (Celsius * 9/5) + 32
Formula_Celsius = (Fahrenheit - 32) * 5/9

if Convert_choice == 'Celsius':
    Fahrenheit = (Celsius * 9/5) + 32
    print(f'The convertion from Celsius to Fahrenheit is: {Fahrenheit} ')
else:
    Celsius = (Fahrenheit - 32) * 5/9
    print(f'The convertion from Fahrenheit to Celsius is: {Celsius} ')

################ 2 ########################
#Word Frequency Counter 
from collections import Counter
sentence = input('Please enter a sentence here: ')
words = sentence.split()
word_count = Counter(words)
for word, count in word_count.items():
    print (f"{word} : {count}")
        

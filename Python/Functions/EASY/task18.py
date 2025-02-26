#Count Words in a Sentence
def count_words():
    words = input('Enter a scentence: ').split()# Split the sentence into words
    print("Words:", words)
    count = 0 # Initialize count variable to zero
    for i in words:
        count += 1
    print (count)        

count_words()
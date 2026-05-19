# Write a Python Program to Sort Words in Alphabetic Order.
# Python program to sort words in alphabetic order (case-insensitive)

# Taking input from user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Sort the words ignoring case
words.sort(key=str.lower)

# Print sorted words
print("The sorted words are:")
for i in words:
    print(i)


# Write a program to delete ith occurrence of word in list
# where words repeat using del function and store result in new list

words = input("Enter words separated by space: ").split()

new_list = words.copy()

word = input("Enter word to delete occurrence: ")
occ = int(input("Enter occurrence number to delete: "))

count = 0

for i in range(len(new_list)):
    if new_list[i] == word:
        count += 1

        if count == occ:
            del new_list[i]
            break

print("New List:")
print(new_list)


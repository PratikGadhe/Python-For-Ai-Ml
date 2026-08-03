"""
14. Sort List of Dictionaries
Problem Statement:
Write a program to sort a list of dictionaries based on a given key.
Input:
 List of dictionaries
 Key
Output:
 Sorted list
Example:
Input: [{"age":25}, {"age":20}]
Output: [{"age":20}, {"age":25}]
"""
data = [{"age": 25}, {"age": 20}]

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i]["age"] > data[j]["age"]:
            data[i], data[j] = data[j], data[i]     #swap

print(data)
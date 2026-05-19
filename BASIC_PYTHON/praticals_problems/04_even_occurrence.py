"""
WAP to remove every even occurrence of repeated words from a list
"""

lst = input("Enter elements : ").split()
count = {}
result = []
for i in lst:
    if(i in count):
        count[i]+=1
    else:
        count[i]=1

    if(count[i]%2 != 0):
        result.append(i)
print("List after removing even occurrences:")
print(result)
#1. list.append(4) #adds one element at the end
list=[1,2,3,4]
list.append(5)
# print(list)

#2. list.sort() #sorting is in ascending order / discending order
list1=[2,6,1,8,7,9] 
list1.sort() #ascending order
# print(list1)
list1.sort(reverse = True)
# print(list1)

list2=["apple","banana","mango","lichi"]
list2.sort()
# print(list2)
list2.sort(reverse=True)
# print(list2)

#3. list.reverse()

list3=['a','b','c','d','e']
list3.reverse()
# print(list3)

#4. list.insert(idx,element)
list4=[1,5,3,7]
list4.insert(2,4)
# print(list4)

#5. list.remove() : remove the first occurence number from list 
list5=[1,3,5,7,1,2,5]
list5.remove(1) #this will remove the 1st one from the list
print(list5)

#6. list.pop(idx) : this will remove the value from the given index
list6=[1,3,5,7,9,0]
list6.pop(5)
# print(list6)
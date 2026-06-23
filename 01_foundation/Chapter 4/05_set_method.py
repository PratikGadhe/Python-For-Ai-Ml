#1. set.add() : inserting value inside set

set=set()   #empty set
set.add(1)
set.add(2)
set.add(2)

print(set)
# print(len(set))


#2. set.remove(): remove element  from set

set1={1,1,2,3,5,"pratik","python","python"}
set1.remove("python")
print(set1)

#3. set.clear() : it clear whole set element 
set2={1,2,3,4,5}
# set2.clear()
# print(len(set2))
# print(set2)

#4. set.pop() : remove random element from set
set3={"Pratik","python","roll_number","prn_number","learning"}
print(set3.pop())

#5 set1.union(set2) : combine both set and return new unique set

set3={1,2,3}
set4={2,3,4,5}
print(set3.union(set4))

#6. set1.interesect(set2) 

print(set3.intersection(set4))
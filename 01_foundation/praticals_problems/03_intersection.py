# wap to find the intersection of two list 
import numpy as np 
# 1. set1.intersection(set2)
n1 = [2,1,1]
n2 = [1,2,3]
final = list(set(n1).intersection(set(n2)))
print(final)

# 2. using '&' operator

n1 = [2,1,1]
n2 = [1,2,3]
final = list(set(n1) & set(n2))
print(final)

# 3. list comprehension
n1 = [2,1,1]
n2 = [1,2,3]
final = [x for x in (set(n1) & set(n2))]
print(final)

# 4. list comprehension another method
n1 = [2,1,1]
n2 = [1,2,3]
final = list(set([x for x in n1 if x in n2]))
print(final)

# 5. using numpy as np
# import numpy as np 
n1 = [2,1,1]
n2 = [1,2,3]
final = np.intersect1d(n1,n2)
print(final)
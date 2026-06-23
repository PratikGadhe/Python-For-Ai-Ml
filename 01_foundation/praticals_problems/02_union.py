"""
wap to find the union of two lists
"""
import numpy as np
# 1. Set union method
n1 = [2,1,1]
n2 = [2,2,3]
final = list(set(n1).union(set(n2)))
print(final)

# 2. '|' operator method
n1 = [2,1,1]
n2 = [2,2,3]

final = list(set(n1) | set(n2))
print(final)

# 3. list concatenation
n1 = [2,1,1]
n2 = [2,2,3]

final = list(set(n1 + n2))
print(final)

# 4. list comprehension

n1 = [2,1,1]
n2 = [2,2,3]
final = list(set([x for x in n1+n2]))
print(final)

# 5. using numpy union1D()

n1 = [2,1,1]
n2 = [2,2,3]
final = np.union1d(n1,n2)
print(final)

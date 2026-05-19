# creating array from scratch using different build in methods 
import numpy as np

# 1. zeroes array 
zero = np.zeros((3,4))
print(zero)

# 2. ones array 
one = np.ones((2,3))
print(one)

# 3. constant array using full()
constant_value = np.full((3,3),63)
print(constant_value)

# 4. array with random value using random class
random = np.random.random((3,3))
print(random)
# remember .random is class having lots of methods in it

# 5. creating squence array using arange() method
sequence = np.arange(0,11,2)
print(sequence)
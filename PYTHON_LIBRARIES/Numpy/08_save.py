# SAVING NUMPY ARRAYS 
import numpy as np
import matplotlib.pyplot as plt
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.random.random((3,3))
arr3 = np.zeros((2,4))

np.save('arr1.npy',arr1)
np.save('arr2.npy',arr2)
np.save('arr3.npy',arr3)

# loading data on numpy from the files
load = np.load('arr1.npy')
print(load)

try :
    logo = np.load('numpy-logo.npy')
    # display
    plt.figure(figsize = (10,5))
    plt.subplot(121)
    plt.imshow(logo)
    plt.title("Numpy logo")
    plt.grid(False)

    dark_logo = 1 - logo
    plt.subplot(122)
    plt.imshow(dark_logo)
    plt.title("Numpy dark logo")
    plt.grid(False)

except FileNotFoundError:
    print("numpy logo error")
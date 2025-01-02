#Difference between the memory allocation of list in python and array in numpy
import sys
import time
import pandas as pd
import numpy as nm

#difference in time taken
# start = time.time()
# l = list(range(10000))
# print(l)
# end = time.time()
# print(end-start)       #prnting the time taken for a list

# start1 = time.time()
# arr = nm.array(range(10000))
# print(arr)
# end1 = time.time()
# print(end1-start1)

#difference between memory
# print(sys.getsizeof(1)) #bytes taken by 1 character
# l = list(range(100))
# print(sys.getsizeof(1) * len(l))
# arr = nm.arange(100)
# print(arr.itemsize*arr.size)

'''
difference is clearly mentioned 2800 and 800
'''

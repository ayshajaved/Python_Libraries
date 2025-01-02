'''
NumPy (Numerical Python) is a powerful open-source library in Python that is widely used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays. Here are some key features and components of the NumPy library:
Key Features of NumPy:
Multi-Dimensional Arrays (ndarray):
The core of NumPy is its ndarray object, a versatile and efficient multi-dimensional array that can store elements of the same data type. This allows you to work with large datasets efficiently.
Mathematical Operations:
NumPy provides a wide range of mathematical operations, including basic arithmetic (addition, subtraction, multiplication, division), linear algebra, Fourier transforms, and more.
Broadcasting:
Broadcasting allows NumPy to perform element-wise operations on arrays of different shapes, making operations more efficient and intuitive without requiring explicit loops.
Vectorization:
NumPy allows you to perform operations on entire arrays without writing explicit loops, which is much faster and more efficient than using traditional Python loops.
Random Number Generation:
The numpy.random module provides functions to generate random numbers, which is useful for simulations, statistical sampling, and testing.
Integration with Other Libraries:
NumPy is foundational for many other scientific computing libraries in Python, such as SciPy, Pandas, and TensorFlow, making it an essential tool for data science and machine learning.
Memory Efficiency:
NumPy arrays are more memory-efficient than Python lists, especially for large datasets, because they store elements of the same type and use a fixed amount of memory for each element.
'''
import numpy as nm
# array = nm.array([2,4,5,2,1,89])
# print(array)
# array_2d = nm.array([[2,3], [4,5]])
# print(array_2d)  #2d array
# result = array_2d +10 #addition in 2d array
# print(result)

# result = array_2d *2 #multiplication in 2d array
# print(result)

# result = array_2d /2 #division in 2d array
# print(result)

#random array
# ran_arr = nm.random.rand(3,3)
# print(ran_arr)

'''
dtype returns the type of array that can be int8, int16, int32
size returns the size and shape returns the shape like (3,3)
'''
# arr = nm.array([[2, 4], [7,1]], dtype="int8") #if i remove the dtype, by default it is int64
# print(arr) 
# print(nm.size(arr)) #4
# print(nm.shape(arr)) #(2,2)
# print(arr.dtype)
# arr[0][0] = 99 #we can change the vale
# print(arr)
'''
zeros, ones, arange
'''
# zeros = nm.zeros(4)
# print(zeros)
# ones = nm.ones(4)
# print(ones)
# a_arr =nm.arange(10)
# print(a_arr)
# a_arr =nm.linspace(1, 10, 4) #difference between the numbers is same
# print(a_arr)
'''
empty, is used to create a 2d array as zeros or ones is used to create the 1d arry
'''
# em = nm.empty((2,2), dtype="int16")
# print(em, em.dtype)

#identity
# arr = nm.identity(5)
# print(arr)

#reshaping 1D arr to 2D
# arr = nm.arange(12) 
# print(arr)
# print(arr.reshape(2,6)) #the number of elements must be same

'''
axis; the vertical columns have zero axis and horizontal rows have 1 axix
'''
# arr = nm.array([[1,2,3], [2,3,1]])
# print(nm.sum(arr, axis= 0))
# print(nm.sum(arr, axis= 1))

'''
ndim, retrns the dimension
'''
# arr = nm.array([2,3,4])
# print(arr.ndim)

# arr = nm.array([[2,3,4],[2,4,5]])
# print(arr.ndim)

'''
max min number
'''
# arr = nm.array([[2,3,1], [4,6,7], [1,2,3]])
# print(arr)
# print(arr.argmax()) #considering 1d, index is returned
# print(arr.argmin()) #considering 1d, index is returned
#we can pass axis as argument
# print(arr.argmax(axis=0)) #considering 1d, index is returned
# print(arr.argmin(axis=0)) #considering 1d, index is returned
# print(arr.argmax(axis=1)) #considering 1d, index is returned
# print(arr.argmin(axis=1)) #considering 1d, index is returned

# arr.sort()
# print(arr)

'''
aritmetic operation
'''
arr1 = nm.array([[1,2,3], [4,2,3]])
arr2 = nm.array([[2,2,0], [1,7,4]])
# x =arr1 * arr2
# print(x)   #similarl -, +, / all can happen
# x = nm.sqrt(arr1)
# print(x)

# x = nm.sum(arr1)
# print(x)
# x = nm.max(arr2)
# print(x)
# x = nm.min(arr2)
# print(x)
x = nm.where(arr2>2)
print(x)
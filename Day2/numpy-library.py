# Numpy is used for Fast Mathematical Operations & to work with arrays.


# Creating Arrays using Numpy
# Importing the numpy library with alias np
import numpy as np


arr = np.array([1, 2, 3])
print(arr)


# Creating a matrix or 2D array using Numpy, 2*2 matrix
arr2 = np.array([[1, 2], [3, 4]])
print(arr2)


# 2D array: 3*3 matrix
arr3 = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])
print(arr3)


# Mathematical Operations with Array
a = np.array([2, 5, 8])
b = np.array([3, 7, 11])


# Sum of 2 arrays
print(a + b)


# Difference of 2 arrays
print(a - b)


# Product of 2 arrays
print(a * b)


# Division for Quotient of 2 arrays
print(a / b)


# np.arange()
# np.arange(start, end, step)
evenArr = np.arange(0, 20, 2)
print(evenArr)


mulOf3 = np.arange(0, 30, 3)
print(mulOf3)


# np.linspace()
# np.linspace(start, end, number-of-partitions)
arr = np.linspace(0, 1, 5)
print(arr)


arr = np.linspace(0, 5, 10)
print(arr)


# np.zeros()
# np.zeros((rows, columns))
arr = np.zeros((2, 3))
print(arr)


arr = np.zeros((3, 5))
print(arr)


# np.ones()
# np.ones((rows, columns))
arr = np.ones((3, 2))
print(arr)


arr = np.ones((5, 4))
print(arr)


# shape
# Returns Number of Rows & Columns
arr = np.array([[1, 2], [3, 4]])
print(arr.shape)


arr = np.array([[2, 5, 5], [6, 10, 4]])
print(arr.shape)


arr = np.array([[2, 5, 5, 8, 3], [6, 10, 4, 2, 3]])
print(arr.shape)


# ndim - Num of Dimensions
arr = np.array([[2, 5, 5, 8, 3], [6, 10, 4, 2, 3]])
print(arr.ndim)


arr = np.array([6, 10, 4, 2, 3])
print(arr.ndim)


# size - Number of items (rows*columns)
arr = np.array([6, 10, 4, 2, 3])
print(arr.size)


arr = np.array([[2, 5, 5, 8, 3], [6, 10, 4, 2, 3]])
print(arr.size)


# reshape
# Number of rows & columns to divide the items
arr = np.arange(6)
print(arr.reshape(2, 3))
print(arr.reshape(3, 2))


arr = np.arange(16)
print(arr.reshape(4, 4))
print(arr.reshape(2, 8))
print(arr.reshape(8, 2))


# flatten
# Multiple Rows & Columns will be brought down to single row or dimension
arr = np.array([[ 0,  1,  2,  3],[ 4,  5,  6,  7],[ 8,  9, 10, 11],[12, 13, 14, 15]])
print(arr.flatten())


arr = np.array([[2, 4, 6], [3, 6, 9]])
print(arr.flatten())


# mathematical operations using array
# sum()
arr = np.array([2, 5, 7, 11, 16, 20])
print(arr.sum())


# mean() or average
print(arr.mean())


# min() & max()
print(arr.max(), arr.min())


# std()
print(arr.std())


# Basic Indexing
arr = np.array([2, 7, 14, 5, 6])
print(arr[3])


# 2D Indexing
arr = np.array([[2, 4, 6], [3, 6, 9]])
# 0 stands for 1st row/column, 1 stands for 2nd row/column
print(arr[1, 2])
print(arr[0, 1])


# Boolean Indexing
arr = np.array([1, 3, 2, 5, 6, 8])
print(arr[arr > 3])
print(arr[arr < 3])
print(arr[arr % 2 == 0])


# random.rand()
# rand(rows, cols)
arr = np.random.rand(3, 3)
print(arr)


# random.randint()
# randint(start, end, number-of-values)
arr = np.random.randint(0, 9, 6)
print(arr)


# concatenate()
a = np.array([2, 3, 6])
b = np.array([3, 6, 10, 15, 19])
print(np.concatenate((a,b)))


# unique()
arr = np.array([2, 4, 2, 3, 5, 4, 3, 6])
print(np.unique(arr))


# sort()
arr = np.array([5, 3, 1, 2, 6, 3, 7, 4])
print(np.sort(arr))

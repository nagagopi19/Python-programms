#2D Array
#By using array() function
'''>>> from numpy import *
>>> arr = array ([[3,4,5] , [7,6,2], [1,7,2]])
>>> print(arr)
[[3 4 5]
 [7 6 2]
 [1 7 2]]
>>> '''

#By using ones()and zeros() function
'''>>> x = ones((3,4), int)
>>> x
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
>>> x = zeros((3,4), int)
>>> x
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])
>>> x = zeros((3,4), float)
>>> x
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> type(x)
<class 'numpy.ndarray'>
>>> '''

#By using eye() function
'''>>> x = eye(5, dtype=int)
>>> x
array([[1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1]])
>>> '''

#indexing & Slicing
#indexing
'''>>> from numpy import *
>>> arr = array([[5,4,3].[6,7,8],[3,1,2]])
  File "<stdin>", line 1
    arr = array([[5,4,3].[6,7,8],[3,1,2]])
                         ^
SyntaxError: invalid syntax
>>> arr = array([[5,4,3],[6,7,8],[3,1,2]])
>>> arr
array([[5, 4, 3],
       [6, 7, 8],
       [3, 1, 2]])
>>> arr[0]
array([5, 4, 3])
>>> arr[1]
array([6, 7, 8])
>>> arr[0][1]
4
>>> arr[0][0]
5
>>> arr[0,2]
3
>>> arr[1,1]
7
>>> arr[2,0]
3
>>>

#Slicing

>>> arr
array([[5, 4, 3],
       [6, 7, 8],
       [3, 1, 2]])
>>> arr[1:3,1:3]
array([[7, 8],
       [1, 2]])
>>> arr[1:,1:]
array([[7, 8],
       [1, 2]])'''

# Creation of matrix in different ways
#1. matrix(str)
'''>>> str = '1,2,3,4,5,6'
>>> m1 = matrix(str)
>>> m1
matrix([[1, 2, 3, 4, 5, 6]])
>>>'''

#2.matrix(2darray)
'''>>> arr
array([[5, 4, 3],
       [6, 7, 8],
       [3, 1, 2]])
>>> m = matrix(arr
... )
>>> m
matrix([[5, 4, 3],
        [6, 7, 8],
        [3, 1, 2]])
>>>'''
#3. Transpose matrix
'''>>> m.T
matrix([[5, 6, 3],
        [4, 7, 1],
        [3, 8, 2]])
>>>
>>> m.transpose()
matrix([[5, 6, 3],
        [4, 7, 1],
        [3, 8, 2]])
#4. Diagonal matrix
>>> diagonal(m)
array([5, 7, 2])
>>> m
matrix([[5, 4, 3],
        [6, 7, 8],
        [3, 1, 2]])
#5. max matrix
>>> m.max()
8
#6. min matrix
>>> m.min()
1
#7. sum matrix
>>> m.sum()
39
#8. mean matrix
>>> m.mean()
4.333333333333333
>>> m.median()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'matrix' object has no attribute 'median'
>>> m.mode()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'matrix' object has no attribute 'mode'
#9. sort  matrix
>>> sort(m)
matrix([[3, 4, 5],
        [6, 7, 8],
        [1, 2, 3]])
>>>
#10. column-wise sorting
>>> sort(m, axis=0)
matrix([[3, 1, 2],
        [5, 4, 3],
        [6, 7, 8]])
>>>'''


'''# Matrix Multiplication

>>> m
matrix([[5, 4, 3],
        [6, 7, 8],
        [3, 1, 2]])
>>> m1 = m.T
>>> m1
matrix([[5, 6, 3],
        [4, 7, 1],
        [3, 8, 2]])
>>> print(m*m1)
[[ 50  82  25]
 [ 82 149  41]
 [ 25  41  14]]
# Matrix Addition
>>> print(m+m1)
[[10 10  6]
 [10 14  9]
 [ 6  9  4]]
# Matrix division
>>> print(m/m1)
[[1.         0.66666667 1.        ]
 [1.5        1.         8.        ]
 [1.         0.125      1.        ]]
# Matrix subtraction
>>> print(m-m1)
[[ 0 -2  0]
 [ 2  0  7]
 [ 0 -7  0]]
>>>'''

# find transport of a matrix
from numpy import *
r,c=[int(i) for i in input('How many rows, cols?').split(',')]
arr = zeros((r,c), int)
print('Enter elements:')
for i in range(r):
    arr[i] = [int(i) for i in input().split()]
m = matrix(arr)
print('Transpose matrix:')
m1=m.transpose()
print(m1)


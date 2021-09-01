#Array
#array: It represents a group of elements of same data type.
#Diff between list and array
# list's are stored in diffeent types of data where as array is stored in only one type of data
#Arry using list[]
'''import numpy as np
arr = np.array([20,30,45,10,-5])
print(arr, '\n', type(arr))''''

#Arry using string()
'''>>>import numpy as np
>>>names  =  np.array(['Rishi', 'Vani', 'Lakshmi', 'Gopi'])# This line not working at editor, work's at IDLE 
>>>print((names[2]))'''

#Arry using linspace()
'''>>>import numpy as np
>>>x = np.linspace(0,10,5)# This line not working at editor, work's at IDLE 
>>>print(x)'''

#Arry using logspace()
'''>>>import numpy as np
>>> x = np.logspace(1,4,5)
>>> x'''

#Arry using arange() ----> arange() means array range
'''>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a = np.arange(10,20)
>>> a
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
>>>
>>> a = np.arange(10,20,2)
>>> a
array([10, 12, 14, 16, 18])
>>> s''' 

#Arry using zeros() and ones()
'''>>> a = np.zeros(5,int)
>>> a
array([0, 0, 0, 0, 0])
>>> a = np.zeros(5,float)
>>> a
array([0., 0., 0., 0., 0.])
>>> a = np.zeros(10)#by Default of zeros() is float values print
>>> a
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
>>> a = np.ones(10)#by Default of ones() is float values print
>>> a
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
>>> print(a)
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
>>> '''

# Array operations
'''>>> arr
array([20, 30, 45, 10, -5])
>>> arr+5
array([25, 35, 50, 15,  0])
>>> arr/2
array([10. , 15. , 22.5,  5. , -2.5])
>>> arr*2
array([ 40,  60,  90,  20, -10])
>>> arr%2
array([0, 0, 1, 0, 1], dtype=int32)
>>> 

>>> np.sqrt(arr)
Warning (from warnings module):
  File "<pyshell#30>", line 1
RuntimeWarning: invalid value encountered in sqrt
array([4.47213595, 5.47722558, 6.70820393, 3.16227766,        nan])----> nan means not a  number
>>> 


>>> arr
array([20, 30, 45, 10, -5])
>>> pow(arr,3)
array([ 8000, 27000, 91125,  1000,  -125], dtype=int32)
>>> sum(arr)
100
>>> np.prod(arr)----> Cumulative product
-1350000
>>> np.min(arr)
-5
>>> np.max(arr)
45
>>> np.mean(arr)
20.0
>>> np.argmin(arr)
4
>>> np.argmax(arr)
2
>>> np.sort(arr)
array([-5, 10, 20, 30, 45])---> Assending order
>>> np.sort(arr)[::-1]
array([45, 30, 20, 10, -5])--->descending order
>>> '''


'''>>> from numpy import *
>>> arr = array([10,20,30,40,55])
>>> print(arr)
[10 20 30 40 55]
>>> b = arr
>>> b
array([10, 20, 30, 40, 55])
>>> b[0]=99
>>> b
array([99, 20, 30, 40, 55])
>>> arr
array([99, 20, 30, 40, 55])
>>>'''
#shallow copying---> It will change one array, automatically changed another arry.
'''>>> arr
array([99, 20, 30, 40, 55])
>>> x = arr.view()
>>> x
array([99, 20, 30, 40, 55])
>>> arr
array([99, 20, 30, 40, 55])
>>> x[0]
99
>>>
>>> x[0] = 100
>>> x
array([100,  20,  30,  40,  55])
>>> arr
array([100,  20,  30,  40,  55])'''

#deepcopying---> It will not effected another array
'''>>> y = arr.copy()
>>> y
array([100,  20,  30,  40,  55])
>>> y[0]
100
>>> y[0]=222
>>> y
array([222,  20,  30,  40,  55])
>>> arr
array([100,  20,  30,  40,  55])
>>>'''

# Indexing
'''>>> arr[0]
100
>>> arr[4]
55
>>> arr[-1]
55
>>> arr[-3]
30
>>>'''
#Slicing
'''>>> arr[0:3]
array([100,  20,  30])
>>> arr[4:1:-1] # Reverse slicing
array([55, 40, 30])
>>>'''

#Repetition----> Not supported for python
'''>>> arr*2  ---> Wrong answer
array([200,  40,  60,  80, 110])
>>>'''

#Attrributes or properties of an array
#ndim
'''>>> arr
array([100,  20,  30,  40,  55])
>>> arr.ndim
1
>>>
>>> x = array([[1,2,3],[3,4,5]])
>>> x.ndim
2'''

#shape
'''>>> arr
array([100,  20,  30,  40,  55])
>>> arr.shape
(5,)
>>> x = array([[1,2,3],[3,4,5]])
>>> x.shape
(2, 3)'''
#size
'''>>> x = array([[1,2,3],[3,4,5]])
>>> x.size
6
>>>'''
#itemsize
'''>>> arr
array([100,  20,  30,  40,  55])
>>> arr.itemsize
4 bytea
>>> y = array([4.5,6.1,-6.1,9])
>>> y.itemsize
8 bytes
>>>'''
#dtype
'''>>> y.dtype
dtype('float64')
>>> arr.dtype
dtype('int32')
>>>'''
#nbytes
'''>>> y = array([4.5,6.1,-6.1,9])
>>> y.nbytes
32
>>>'''
#reshape()---> 1D to 2D
'''>>> arr
array([100,  20,  30,  40,  55])
>>> arr = array([10,20,30,40,50,60])
>>> arr
array([10, 20, 30, 40, 50, 60])
>>> arr.reshape(2,3)
array([[10, 20, 30],
       [40, 50, 60]])
>>> arr.reshape(3,2)
array([[10, 20],
       [30, 40],
       [50, 60]])'''
>>>
#flatten() ---> 2D to 1D
'''>>> arr = array([10,20,30,40,50,60])
>>> x=arr.reshape(3,2)
>>> x
array([[10, 20],
       [30, 40],
       [50, 60]])
>>> x.flatten()
array([10, 20, 30, 40, 50, 60])
>>>'''

































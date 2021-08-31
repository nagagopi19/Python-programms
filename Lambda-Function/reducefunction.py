#reduce() function --> It reduces a group of elements into a single value bases on a lambda
#Syntax --->reduce(lambda,seq)
#Create a lambda function to calculate products of elements of a list.
#lst = [1,2,4,6,-6,7,7.5,8]
lst = [1,2,3,4]
from functools import *
result = reduce(lambda x,y: x*y, lst)
print("Cumulative product = ",result)


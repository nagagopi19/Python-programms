# Understanding the command line args
'''import sys
n=len(sys.argv)
print('No. of args= ', n)

print("The args are:")
for i in sys.argv:
    print(i)
print ("Another way: ")
for i in range(n):
    print(sys.argv[i])'''

'''from sys import *
n=len(argv)
print('No. of args= ', n)

print("The args are:")
for i in argv:
    print(i)
print ("Another way: ")
for i in range(n):
    print(argv[i])'''

'''from sys import *
a = argv[1]
b = argv[2]

print("sum = ", a+b)'''

'''from sys import *
a = int(argv[1])
b = int(argv[2])

print("sum = ", a+b)'''


#to check if a given year is leap or not

from sys import *

y = int(argv[1])
if y%100!=0 and y%4==0 or y%400==0:
    print("%d is leap year" %y)
else:
    print("%d is not leap year" %y)





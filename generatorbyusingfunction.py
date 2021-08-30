# A function to generates nos from m to n
'''def mygen(m, n):
    while m<=n:
        print(m)
        m+=1 #m = m+1
mygen(100,200)'''
'''res = mygen(10,20)
print(res)'''

# By using generator function
'''def mygen(m,n):
    while m <= n:
        yield m
        m+=1 #m = m+1
obj = mygen(10,20)
print(list(obj))'''

#  generator function By using for loop
def mygen(m,n):
    while m <= n:
        yield m
        m+=1 #m = m+1
obj = mygen(10,20)
for i in obj: print(i)

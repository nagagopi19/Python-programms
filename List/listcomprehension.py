# Create a list comprehension to find squares of numbers from 1 to 10

lst=[]
for i in range(1,11):
    lst.append(i*i)
print(lst)

#The below is the equivalent list comprehension

lst=[i*i for i in range(1,11) ]
print(lst)

# write a list comprehension to get even nos upto 10.
#Normal Code
'''lst = []
for i in range(2,11,2):
    lst.append(i)
print(lst)'''

lst = []
for i in range(2,11):
    if i%2==0:
        lst.append(i)
print(lst)

# list comprehension
'''lst =[i for i in range(2,11,2)]
print(lst)'''

lst =[i for i in range(2,11) if i%2==0]
print(lst)

#Add corresponding elements of two lists and store them in another list.
a = [10,20,-5,6,7,11]
b = [5,15,5,16,11,12]
c = []
for i in range(6):
    c.append(a[i]+b[i])
print(c)

# list comprehension
c =[a[i]+b[i] for i in range(6)]
print(c)

#Retrieve common elements in two lists.
a = [10,11,25,33,12,-5]
b = [-5,55,10,33,0,11]
c = []
for x in a:
    if x in b:
        c.append(x)
print(c)

# list comprehension
c = [x for x in a if x in b]
print(c)

# Retrieve only the first letter of each word in the list.
#Normal code
words = ["Gopi",'Lakshmi',"Vignitha","Rishi"]
lst = []
for word in words:
    lst.append(word)
print(lst)

words = ["Gopi",'Lakshmi',"Vignitha","Rishi"]
lst = []
for word in words:
    lst.append(word[0])
print(lst)

# list comprehension
lst = [word[0] for word in words]
print(lst)


# to accept multiple integers from keyboard
'''a,b,c = [int(i) for i in input('Enter three nos:').split(',')]
#print(a,b,c)
sum = a+b+c
print("sum is:", sum)'''

lst= [int(i) for i in input('Enter nos:').split(',')]
#print(a,b,c)
total = sum(lst)
print("sum is:", total)




'''x=input("Enter a string:")
def ispalindrome(x):
    return x == x[: : -1]
y = ispalindrome(x)
if y:
    print('True')
else:
    print('False')'''

'''str=input("Enter a string:")
ASCII_SIZE=256
def getmaxoccuringorigin(str):
    count = [0] * ASCII_SIZE
max = -1
c = ''
for i in str:
    count[ord(i)]+=1;
for i in str:
    if max<count[ord(i)]:
        max=count[ord(i)]
        c=i
return c
print(getmaxoccuringorigin(str))'''

'''#x =int(input("Enter a list:"))
#list.append(x)
list=[1,3,4,7,9]
print(list)
print("Second smallest nos",list[1])
print("Second Largest no: ",list[3])
print("difference:",list[3]-list[1])'''


'''def getRightBySides(x,y,z):
    a,b,c=x**2,y**2,z**2
if max(a,b,c)==(a+b+c-max(x,y,z)):
    print("True")
else:
    print("False")'''

'''x=int(input("Enter a side1 :"))
y=int(input("Enter a side2 :"))
z=int(input("Enter a side3 :"))'''
'''def getRightBySides(x,y,z):
    a,b,c = x**2, y**2, z**2
    if max(a,b,c)==(a+b+c-max(a,b,c)):
        print("True")
    else:
        print("False")
x=int(input("Enter a side1 :"))
y=int(input("Enter a side2 :"))
z=int(input("Enter a side3 :"))
getRightBySides(x,y,z)'''


x = int (input("Enter a list:"))
list=[]
list.append(x,end='')
print(list)







'''# A function to calculate arithmetic operations by using return

def add_sub(x,y):
    res1 = x+y
    res2 = x-y
    return res1, res2
r1 , r2 = add_sub(10,12.5)
print('Result of addition=', r1)
print('Result of subtraction=', r2)'''

# Local variable
'''def display():
    x =10 # local var
    print(x)
display()

#print(x) # error'''

# Global variable
'''g = 22 # global vars
def display():
    x=10
    print(x)
    print(g)
display()
print(g)'''

# Global varible and local variable name is same
'''x = 22
def display():
    x = 10
    print(x) # It prints local variable value
display()
print(x) # It prints global variable value'''


#How to retrive global variables into local variable
# by using globals() function

x = 22
def display():
    x= 45
    print(x)
    y = globals()['x']
    print(y)
display()
            
            

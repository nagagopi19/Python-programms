# Functions are first class objects.
# ===> Functons and objects are same.
#object ===> It means a block of memory. Examples are: int(),float(),str(),list[],tuple().
#1. We can assign a function to a variable
'''def square(x):
    return x*x
x = square(4)
print(x)'''

#2. We can assign a function to another function
'''def display(msg):
    res = msg() # msg is function name, () is calling
    print(res+'Rishi')
def msg():
    return 'Hello'
display(msg)'''

#3. We can write a function inside another function
'''def display():
    def msg(): # msg() ---> Inner function / Nested function
        return 'Rishi'
    return 'Hello' + msg()
str = display()
print(str)'''

#4. We can return a function from another function
def display():
    def msg(): # msg() ---> Inner function / Nested function
        return 'Rishi'
    return 'Hello' + msg()
str = display()
print(str)


#Types of Arguments
# 1. Positional arguments ----> Arguments passed in the correct order
'''def join(s1,s2):
    str = s1+s2
    print(str)
join("Hyder", 'bad') # Positional Arguments'''

# 2. Keyword arguments ----> Arguments passed in the function by the parameter names
'''def join(s1,s2):
    str = s1+s2
    print(str)
#join(s1="Hydera", s2='bad')# Keyword Arguments
join(s2='bad',s1="Hydera")# Keyword Arguments
#Advantages of KA----> if you want change the order, then result is print correct order.'''

#3 . Default arguments ---> The arguments with default values
#Type-1:
'''def grocery(item, price):
    print("Item Name = %s" %item)
    print("Price = %.2f" %price)
grocery('Sugar',65.5555)'''
#Type-2:
'''def grocery(item, price=50.00):
    print("Item Name = %s" %item)
    print("Price = %.2f" %price)
grocery('oil')'''
#Type-3:
'''def grocery(item, price=50.00):
    print("Item Name = %s" %item)
    print("Price = %.2f" %price)
grocery('oil',57.75)'''

#Combined Type-1 + Type-2 + Type-3 in one function
'''def grocery(item, price=50.00):  # Here ---> Price is a default argument
    print("Item Name = %s" %item)
    print("Price = %.2f" %price)
grocery('Sugar',65.5555)
grocery('oil')
grocery('oil',57.75)'''
'''def grocery(item='Rice', price=50.00):  # Here ---> Item and Price is a default argument
    print("Item Name = %s" %item)
    print("Price = %.2f" %price)
grocery('Sugar',65.5555)
grocery('oil')
grocery('oil',57.75)
grocery()'''

#4. varargs arguments ---> It is also known as variable length arguments. They store 0 or more values.It working internally like as tuple.
'''def add(*x): # *x represents---> variable length argument.
    print(x)
add(10,11)'''
#sum
def add(*x):
    res = sum(x)
    print("Sum = ", res)
add(10,11)
add(10,11,20)
add(10,11,20,30)
add() #default value'0' will be print 
    




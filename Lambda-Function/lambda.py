#lambda Function
# write a lambda function to find square value of a number
'''def square(x):
    return x*x
res = square(4)
print("square value = ", res)

# to following is equivalent lambda
f = lambda x: x*x
print('Square value=',f(4))'''

# write a lambda function to add two numbers
def sum(a,b):
    return a+b
result=sum(10,20)
print("addition is =", result)

#lambda function
f = lambda a,b: a+b
print("addition is =", f(20,30))

# write a lambda to test if a given number is even or odd
def even_odd(num):
    if num%2==0:
        return 'Even'
    else:
        return 'Odd'
str = even_odd(5)
print(str)

#lambda function
str = lambda num: 'Even' if num%2==0 else 'Odd'
print('Result is :', str(4))

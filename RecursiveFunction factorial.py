#Recursive Function---> A function calls it self
# Examples of Recursive Function ---> Factorial Value, lcf,gcd,towers of hanoi
# To find the factorial value using recursion
'''def fact(n):
    if n ==0: res =1
    else: res = n*fact(n-1)
    return res
res = fact(4)
print(res)'''

#To find the factorial value using recursion & forloop
def fact(n):
    if n ==0: res =1
    else: res = n*fact(n-1)
    return res
for i in range(10):
    res = fact(i)
    print('Factorial value of {} is {} '.format(i, res))

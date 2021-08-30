# A decorator to increment the result of a function by 10
'''def decor(fun):
    def inner():
        res = fun()
        res = res + 10
        return res
    return inner
def myfun():
    return 100
x = decor(myfun) # x --> inner
print("Result = ",x())'''

def decor(fun):
    def inner():
        res = fun()
        res = res + 10
        return res
    return inner
@decor
def myfun():
    return 100
res=myfun()
print("Result = ",res)

#map function ---> it acts on each element and perhaps modifies the element based on lambda
#syntax ---> map(lambda,sequence)
#create a lambda that returns squares of all elements in a list.
mylst = [1,2,3,4,5,-4,10,15]
obj = map(lambda x: x*x, mylst)
print(list(obj))
#print(tuple(obj))
#print(set(obj))


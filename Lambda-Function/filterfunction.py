#filter --> it filters out required elements based on a lambda expression
# Syantax : filter(lambda,seq)
#Create a lambda that returns even numbers from a list of numbers.
mylst = [1,2,3,4,5,-4,10,15]
obj = filter(lambda x: x%2==0, mylst)
print(list(obj))

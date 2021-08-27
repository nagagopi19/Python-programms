# List comprehension

#a,b,c=[int(i) for i in input('Enter three nos: ').split()]
#a,b,c=[int(i) for i in input('Enter three nos: ').split(",")]
a,b,c=[float(i) for i in input('Enter three nos: ').split(",")]
sum= a+b+c
print('Sum of three nos =', sum)
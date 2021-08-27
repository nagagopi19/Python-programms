# Accept strings from keyboard and sort them
# List comprehensions
lst = [i for i in input('Enter strings: ').split(",")]
lst1 =[]
for i in lst:
    lst1.append(i.strip())
lst1.sort()
#print(lst)
for i in lst1: print(i)

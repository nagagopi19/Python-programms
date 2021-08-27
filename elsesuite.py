# else suite program whether the no is available or not in list
lst = [10,20,30,-40,40,55]

x = int(input('Enter a number: '))
for i in lst:
    if i == x:
        print('Element is found')
        break
else:
    print('Element is not found')
        


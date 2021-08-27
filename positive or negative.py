#if demo
# Accept a number and test if it is positive or negative

num = int(input('Enter a number:'))
if num == 0:
    print('It is Zero')
elif num>0:
    print(num, 'is positive')
elif num < 0:
    print(num, 'is negative')

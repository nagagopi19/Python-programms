#if demo
# accept a number and find if it is even or odd
n = int(input('Enter a number: '))
if n==0:
    print('It is Zero')
elif n % 2 == 0:
    print(n, 'is even')
    print('yes')
else:
    print(n, 'is odd')
    print('no')
print("End")

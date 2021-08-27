"""
To display day of the week by accepting a number.
Author: K Naga Gopi
Version: v1.0
Company: Google Inc
Project: abc1234
Code:34_45
"""

n = int(input('Enter a number(1-7): '))
if n==1:
    print('Sunday')
elif n==2:
    print('Monday')
elif n==3:
    print('Tuesday')
elif n==4:
    print('Wednesday')
elif n==5:
    print('Thrusday')
elif n==6:
    print('Friday')
elif n==7:
    print('Saturday')
else:
    print("Not a valid Number")

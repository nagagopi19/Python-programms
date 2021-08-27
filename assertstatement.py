# assert Statements

# User should enter a number  between 100 and 200

'''num = int(input('Enter a number(100-200):'))
assert num>=100 and num<=200,"Invalid input entered"
print("You entered:", num)'''

try:
    num = int(input('Enter a number(100-200):'))
    assert num>=100 and num<=200,"Invalid input entered"
    print("You entered:", num)
except AssertionError as ae:
    print(ae)

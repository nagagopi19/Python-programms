# using the functions of modules ===> use.py
#type-1
'''import mypack.arith
mypack.arith.add(10,20.5)
result = mypack.arith.sub(10,20.5)
print('Result of sub is=', result)'''

#type-2
'''import mypack.arith as ar # ar means alias name or another name
ar.add(10,20.5)
result = ar.sub(10,20.5)
print('Result of sub is=', result)'''

# Type-3
'''from mypack.arith import *
add(10,20.5)
result = sub(10,20.5)
print('Result = ', result)'''

# Type-4
from mypack.arith import add,sub
add(10,20.5)
result = sub(10,20.5)
print('Result = ', result)





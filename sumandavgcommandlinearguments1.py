# To accept a group of nos and find their sum and avg

'''argv[0] ----> prog name (not considaration )
argv[1] to argv[n-1] (It is considaration)'''

from sys import *
n = len(argv) #n---> 4
total = 0
for i in range(1,n): #0,1,2,3
    #argv[1]+argv[2]+argv[3]
    #total = total+ int(argv[i])
    total = total+ float(argv[i])
print("Sum= ", total)
avg = total/(n-1)
print("Average= %.3f" %avg)
    



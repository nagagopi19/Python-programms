'''# to disply nos from 1 to 10
#obj = range(1,11)
#for i in obj:
for i in range(1,11):
    #print(i)
    print(i, end='\t')
    #print(i,end=' ')'''

# to display even nos for 10 to 20
'''for i in range(10,21,2):
   # if i % 2=0

    print(i, end='\t')'''

'''# To retrive even from a given list of nos
mylst=[10,11,12,-12,23,0,20]
print(mylst)
for i in mylst:
    if i%2==0:
        print(i)
        #print("Even numbers in given list is:",i)'''

'''# To retrive even from a given list of nos
mylst=[10,11,12,-12,23,0,20]
print(mylst)
for i in mylst:
    if i%2==0:
        print(i)
        #print("Even numbers in given list is:",i)'''

'''# To retrive even from a given list of nos
mylst=[10,11,12,-12,23,0,20]
print(mylst)
list=[]
for i in mylst:
    if i % 2 ==0 and i!=0:
        list.append(i)
    #if i%2==0 and i!=0:   list.append(i)
print(list)
        #print("Even numbers in given list is:",i)'''

'''# To find sum of list of numbers
mylst=[10,11,12,-12,23,0,20]
res = sum(mylst)
print('Sum is:', res)'''


'''# To find sum of list of numbers

mylst=[10,11,12,-12,23,0,20]

sum1=0
for x in mylst:
    sum1=sum1+x
print("Our original list is:", mylst)
print("Our sum is:", sum1)'''

# To display the starting letter of the string

'''words = ['Hyderbad','Guntur','Pune','Bangaluru', ' Kerala']

for word in words:
    print(word)'''

#words = ['Hyderbad','Guntur','Pune','Bangaluru', ' Kerala']
words=[i for i in input('Enter strings:').split(',')]
print(words)
for word in words:
    word=word.strip()
    print(word[0])






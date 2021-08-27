num=input()
Esum=int(0)
Osum=int(0)
for i in range(0,len(num)):
    if(i%2==0):
        Esum+=int(num[i])
    else:
        Osum+=int(num[i])
print(int(abs(Esum-Osum)))
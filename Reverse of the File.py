file_name=input("enter file name:")
f=open(file_name,'r')
for line in f:
 print(line[::-1])

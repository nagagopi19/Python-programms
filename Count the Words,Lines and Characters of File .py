line_count=0
word_count=0
char_count=0
file_name=input("Enter file name:")
f=open(file_name,'r')
for line in f:
 line_count+=1
 word_count+=len(line.split(' '))
 print(line)
 for l in line:
     if(l!=' ' and l!='\n'):
         char_count+=1
print("line count:",line_count)
print("word count:",word_count)
print("character count:",char_count)
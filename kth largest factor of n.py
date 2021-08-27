N, k = [int(x) for x in input().split(' ')]
count = 0
for i in range(N, 0, -1):
    if((N % i) == 0):
        count += 1
    if(count == k):
        print(i)
        break
        
if count < k:
    print("1")
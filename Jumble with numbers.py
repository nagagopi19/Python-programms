def Jumble_with_numbers(n):
    l1,l2=[],[]
    for i in range(1,n+1):
        l1.append(i*((2*i)-1))
        l2.append(i*(i+1)//2)
    if set(l1)&set(l2):
        n_list=sorted(set(l1)&set(l2))
        return n_list
if __name__ == '__main__':
    n1,n2,m= input().split()
    n1,n2,m = int(n1),int(n2),int(m)
    out = []
    for i in Jumble_with_numbers(1000):
        if n1<= i <=n2:
            out.append(i)
    print(out[m-1])
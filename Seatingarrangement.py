for i in range(int(input())):
    table,people=map(int,input().split())
    if table>=people:
        print(1)
    else:
        PA=people//table
        PB=PA+1
        TB=people%table
        TA=table-TB
        
        fact=[1,1]
        for i in range(2,people+2):
            x=i*fact[i-1]
            fact.append(x)
        
        #To find no.of.possible ways to divide people among groups    
        divide=fact[people]//((fact[PA]**TA)*(fact[PB]**TB)*fact[TA]*fact[TB])
        
        #To find no.of.arrangements in a circular table
        if PB>=4:
            arrange=int(divide*(fact[PA-1]/2)**TA*(fact[PB-1]/2)**TB)
        else:
            arrange=divide
        print(arrange)
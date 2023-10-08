n=int(input("enter the value"))
i=1
k=5
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print(p,end="")
        p-=1
        
    k-=1      
    print()
    
n=int(input("enter the value"))
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print(p,end="")
        p+=1
    
    for j in range(i+1):
        print(p,end="")
        p=p+1
    print()        
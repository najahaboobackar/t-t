n=int(input("enter the input"))

for i in range(n):
    p=1
    for j in range(1+i):
        print(" ",end="")
    for j in range(i,n):
        print(p,end="")
        p+=1
    print()        


   
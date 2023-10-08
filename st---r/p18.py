n=int(input("enter the value"))
i=1
for i in range(n):
    p=5
    for j in range(i+1):
        print(p,end="")
        p-=1
    print()
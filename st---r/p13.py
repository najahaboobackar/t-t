n=int(input("enter the input"))
p=2
print(0)

for i in range(2,n):
    for j in range(i):
        print(p,end="")
    p+= 2  
    print()    
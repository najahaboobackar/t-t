n=int(input("enter the limit"))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end="")
    p=p+ 1   
    print()    
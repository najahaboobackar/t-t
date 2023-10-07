n=int(input("enter the input"))


for i in range(n+1):
    for j in range(i+1):
        if i%2==0:
            print(1,end="")
        else:
            print(2,end="")    
    print()    
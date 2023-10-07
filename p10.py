n=int(input("enter the range"))
for i in range(n):
    for j  in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()    
for i in range(n):
    for j  in range(i):
        print(" ",end="")
    for j in range(i,n+1):
        print("*",end="")
    i=1    
    for j in range(i,n+1):
        print("*",end="")
    print()             
      
         
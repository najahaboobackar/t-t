n = int(input("Enter the limit: "))
s=[]

n0, n1 = 0, 1
s.append(n0)
s.append(n1)

print(n0, n1, end=" ")

for i in range(n-2):  # subtracting 2 because we've already printed the first two numbers
    fib = n0 + n1
    print(fib, end=" ")
    n0 = n1
    n1 = fib
    s.append(fib)
s=list(s) 
 

a=int(input("enter the pos"))    

if a<n:
    b=s[a]
    print(b)
        
    



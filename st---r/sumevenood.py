n=int(input("enter the value"))

sum=0
odd=0
for i in range(n+1):
    if i%2==0:
        sum=sum+i
    else:
        odd=odd+i
print(sum)        
print(odd)
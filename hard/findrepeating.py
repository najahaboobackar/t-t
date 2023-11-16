arr=[2,1,3,5,3,5,5,5,5,6,6,6,3]
nums=[]
count=0
b=[]
c=[]
n=len(arr)
arr.sort()
for i in range(n-1):
    if arr[i]+1!=arr[i+1] :
        c.append(arr[i]+1)
            
    if arr[i]==arr[i+1]:
        count+=2
        if count>1:
            b.append(arr[i])
    else:
        count=0 

print(set(b))
c=list(set(c))
c.remove(c[-1])
print(c)

 

         
               
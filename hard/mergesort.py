arr=[1,3,4]
n1=len(arr)
ar2=[2,5,6,7]
n2=len(ar2)
l=[0]*n1
r=[0]*n2
n=n1+n2
merge=[]
i=0
for i in range(n-1):
    b=arr[i]+1
    if arr[i]<ar2[i] and b==ar2[i]:
        l.append(arr[i])
        l.append(ar2[i])
        l.remove(0)
    else:
        r.append(arr[i]) 
        r.append(ar2[i])   
merge=[l,r] 
print(l)  
print(r)     
    
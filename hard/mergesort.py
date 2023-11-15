arr=[1,3,8]
n1=len(arr)+1
ar2=[4,5,6,7]
n2=len(ar2)+1
l=[]*n1
r=[]*n2
n=len(max(arr,ar2))
merge=[]*n
i=0
for i in range(n-1):
    c=ar2[i]+1 
    b=arr[i]+1
    if arr[i]<ar2[i] and i<=n1 :
        l.append(arr[i])
        l.append(ar2[i])
            
    elif ar2[i]<arr[i] and i<=n2:
        l.append(ar2[i])
        l.append(arr[i])    
    else:
        r.append(arr[i]) 
        r.append(ar2[i])
        r.append(ar2[n-1]) 
       
        
         
l=list(set(l))
r=list(set(r))          
merge=[l,r] 

print(merge)
print(l)  
print(r)     
    
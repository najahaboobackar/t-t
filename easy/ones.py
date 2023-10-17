arr=[1,1,1,1,0,0,0,1,1,1,1,1,0,0,0]
max1=0
count=0
n=len(arr)
for i in range(n-1):
    if arr[i]==1:
        count+=1
        while count>max1:
            max1=count
    else:        
        count=0    
    
print(max1)        
       
   
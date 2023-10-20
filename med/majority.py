arr=[1,3,4,4,4,0,0,0,4,4,1,5,5,5,5,5,4,4,4,5,5,4,4,4]
n=len(arr)
max=0
count=0
for i in range(n-1):
    if arr[i]==arr[i+1]:
        count+=1
        while count>max:
            max=count
            b=arr[i]
           
    else:
        count=0 
              
print(b)     
    

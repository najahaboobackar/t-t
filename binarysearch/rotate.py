arr=[5,4,1,2,3]
n=len(arr)
low=0
l=0
k=4
ans=0
high=n-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==k:
        ans=mid
    elif arr[low]<=arr[mid]:
        if arr[low]<=k and k<=arr[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if k>=arr[mid]and k <=arr[high]:
            low=mid+1
        else:
            high=mid-1 
print(ans)            
                                                      
           
               
           
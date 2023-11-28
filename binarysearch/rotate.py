arr=[5,4,1,2,3]
n=len(arr)
low=0
l=0
k=4
high=n-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==k:
        print(mid)
    elif arr[low]>arr[mid]and arr[mid]>k:
        high=mid-1
    
           
               
           
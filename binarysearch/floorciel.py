def floorCeil(arr,x):
    low=0
    n=len(arr)
    ans=0
    ans2=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            ans=arr[mid]
            low=mid+1
        if arr[mid]>=x:
            ans2=arr[mid]
            high=mid-1  
    return ans ,ans2         
            
if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 5
    ind=[]
    ind = floorCeil(arr, x)
    print("The index is:", ind)
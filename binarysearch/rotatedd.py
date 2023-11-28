def bsrotate(arr,k,n):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==arr[low] and arr[mid]==arr[high]and arr[low]==arr[high]:
            low+=1
            high-=1
        if arr [mid]==k:
            return True
        elif arr[low]<=arr[mid]:  
            if arr[low]<=k and arr[mid]>=k:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[high] >=k and arr[mid]<=k:
                low=mid+1
            else:
                high=mid-1
    return False            
if __name__=="__main__": 
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    k = 3
    n=len(arr)
    ans=bsrotate(arr,k,n)
    if not ans:
        print("Target is not present.")
    else:
        print("Target is present in the array.")

                 
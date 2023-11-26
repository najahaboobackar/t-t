def searchInsert(arr,x):
    low=0
    n=len(arr)
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans            
if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 2
    ind = searchInsert(arr, x)
    print("The index is:", ind)
def peak(arr):
    n=len(arr)
    low=1
    high=n-1
    if n==1:
        return 0
    if arr[0]<arr[1]:
       return low
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
            return mid
        if arr[low]<=arr[mid]:
            low=mid+1
        else:
            high=mid-1 
if __name__=="__main__":
     arr = [1,2,3,4,5,6,7,8,5,1]
     ans=peak(arr)
     print("the peak element index is",ans)
                   
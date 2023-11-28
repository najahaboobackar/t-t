import sys
def minsw(arr,n):
    ans=sys.maxsize
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            ans=min(ans,arr[low])
            break
        if arr[low]<arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans =min(ans,arr[mid])
            high=mid-1  
    return ans
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    n=len(arr)
    ans = minsw(arr,n)
    print("The minimum element is:", ans)        
            
    
def findKRotation(arr):
    n=len(arr)
    low=0
    high=n-1
    ans= float('inf')
    while low<=high:
        mid =(low+high)//2
        if arr[low]<=arr[high]:
            index=low
            ans=arr[low]
            break
        if arr[low]<=arr[mid]:
            if arr[low]<ans:
                index=low
                ans=arr[low]
            low=mid+1
        else:
            if arr[mid]<=ans:
                index=mid
                ans=arr[mid]
            high=mid-1
    return index  
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findKRotation(arr)
    print("The array is rotated", ans, "times.")

                  
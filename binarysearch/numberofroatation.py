def numberofRotate(arr,n):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            index=low
        if arr[low]<=arr[mid]:
            index=low
            
            low=mid+1
        if arr[mid]<=arr[high]:
            index=mid
            high=mid-1    
        if arr[mid]>=arr[high] and arr[mid]>=arr[low]:
            index=mid  
    return index
if __name__=="__main__":
    arr = [3,4,5,1,2]
    n=len(arr)
    ans=numberofRotate(arr,n)
    print("The array is rotated", ans, "times.")
          
            
        
       
                    
def lastOccurence(arr,k):
    n=len(arr)
    low=0
    high=n-1
    res=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            res=mid
            low=mid+1 
        elif arr[mid]>k:
            high=mid-1
        else:
            low=mid+1  
    return res 

 
if __name__=="__main__":
    arr=[1,2,3,4,13,13,13,13,16]
    
    ans=lastOccurence(arr,13)
    print(ans)
            
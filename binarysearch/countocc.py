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
def firstOccurence(arr,k):
    n=len(arr)
    low=0
    high=n-1
    fs=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            fs=mid
            high=mid-1 
        elif arr[mid]>k:
            low=mid+1
        else:
            high=mid-1  
    return fs
def count(arr,k):
    last=lastOccurence(arr,k)
    first=firstOccurence(arr,k)
    if first==-1:
        return -1,-1
    elif first==1 :
        return 1
    else:
        return last-first+1
if __name__ == "__main__":
    arr =[2, 4, 6, 8, 8, 8, 11, 13]
    x = 2
    c=count(arr,x)
    print(c)    


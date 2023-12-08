def kmiss(arr,v):
    n=len(arr)
    j=0
    i=0
    for i in range(n-1):
        if j<v:
            if j in arr:
                j+=1
            else:
                j+=1
    return j    
def kthelement(arr,k):
    low=1
    high=max(arr)
    while low<=high:
        mid=(low+high)//2
        kth=kmiss(arr,k) 
        if kth<=k:
            high=mid-1
        else:
            low=mid+1
    return low
if __name__=="__main__":
    arr=[4,7,9,10] 
    k=1
    ans=kthelement(arr,k)
    print("the missing value is ",ans)           
                   
                    
            
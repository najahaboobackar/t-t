def missing(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        misssing1=arr[mid]-(mid+1)
        if misssing1<k:
            low=mid+1
        else:
            high=mid-1
    return (low+k)
if __name__=="__main__":
    a=[4,7,9,10]
    k=4
    ans=missing(a,k)
    print("the missing value",ans)            
                
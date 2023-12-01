def squareroot(k):
    arr=[1,2,3,4,5,6,7,8,9,10]
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        
        if arr[mid]*arr[mid]==k:
            return arr[mid]
        elif arr[mid]*arr[mid]>=k:
            high=mid-1
        else:
            low=mid+1     
if __name__=="__main__":
    k=36  
    s=squareroot(k)
    print("the square root is ",s)          
        
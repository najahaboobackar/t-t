def isfindvalue(arr,n,k,mid):
    
    pos=arr[0]
    el=1
    n=len(arr)
    for i in range(n-1):
        if arr[i]-pos>=mid:
            pos=arr[i]
            el+=1
        if el == k:
            return True
            
    return False
def minimisedis(arr,n,k):
    low=arr[0]
    n=len(arr)
    result=-1
    high=arr[n-1]
    while(low<high):
        mid=(low+high)//2
        if isfindvalue(arr,n,k,mid):
            result=float(max(result,mid))
            low=mid+1
        else:
            high=mid-1
    return result

if __name__=="__main__":
    
    arr = [1, 2, 3, 4, 5]
    n=len(arr)
    k = 4
    ans = minimisedis(arr,n, k)
    print("The answer is:", ans)           
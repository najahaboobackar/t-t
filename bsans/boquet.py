def possible(arr,day,m,k):
    n=len(arr)
    count1=0
    no_of_b=0
    for i in range(n-1):
        if arr[i]>=day:
            count1+=1
        else:
            no_of_b+=(count1)//k  
            count1=0
        no_of_b+=(count1)//k  
        return no_of_b>=m   
def roseGarden(arr,k,m):
    n=len(arr)
    min1=0
    max1=0
    val=m*k
    if val>n:
        return -1
   
    for i in range(n-1):
        min1=min(min1,arr[i])
        max1=max(max1,arr[i])
    low=min1
    high=max1
    while low<=high:
        mid=(low+high)//2
        if possible(arr,mid,m,k) :
            high=mid-1
        else:
            low=mid+1
    return low       

if __name__=="__main__" :
    arr = [7, 7, 7, 7, 13, 11, 12, 7]
    k = 3
    m = 2
    ans = roseGarden(arr, k, m)
    if ans == -1:
        print("We cannot make m bouquets.")
    else:
        print("We can make bouquets on day", ans)      
            
              
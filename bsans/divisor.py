from math import ceil


def devisor(arr,val,th):
    sum=0
    n=len(arr)
    for i in range(n-1):
        sum+=ceil(arr[i]/val)
   
def bsb(arr,th):
    n=len(arr)
    if n>th:
        return -1
    high=max(arr)
    low=min(arr) 
    ans=0
    while low<=high:
        mid=(low+high)//2
        if devisor(arr,mid,th)<=th:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
if __name__=="__main__":
    arr = [1,2,5,9]  
    l=10
    ans=bsb(arr,8)
    print("the smallest devisor",ans)         
           
      
        
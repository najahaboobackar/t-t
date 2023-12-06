from math import ceil


def devisor(arr,val,th):
    sum=0
    n=len(arr)
    for i in range(n-1):
        sum+=ceil(arr[i]/val)
    if sum<=th:
        return True  
def bsb(arr,th):
    n=len(arr)
    if n>th:
        return -1
    high=max(arr)
    low=min(arr) 
    while low<=high:
        mid=(low+high)//2
        if devisor(arr,mid,th):
            high=mid-1
        else:
            low=mid+1
    return low 
if __name__=="__main__":
    arr = [8,4,2,3]  
    l=10
    ans=bsb(arr,8)
    print("the smallest devisor",ans)         
           
      
        
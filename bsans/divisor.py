from math import ceil


def devisor(arr,val,th):
    sum=0
    n=len(arr)
    for i in range(n-1):
        sum+=ceil(arr[i]/val)
    if sum<=th:
        return True  
def bsb(arr,th):
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
    arr = [1, 2, 3, 4, 5]  
    l=8
    ans=bsb(arr,8)
    print("the smallest devisor",ans+1)         
           
      
        
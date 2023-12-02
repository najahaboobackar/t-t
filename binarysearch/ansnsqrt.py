def sqrt1(n):
    low=1
    high=n
    while low<=high:
        mid=(low+high)//2
        val=mid*mid
        if val<=n:
            low=mid+1
        else:
            high=mid-1
    return high 
           
if __name__=="__main__":
    n=100
    ans=sqrt1(n)
    print(ans)

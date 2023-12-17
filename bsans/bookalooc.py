def findpages(arr,pages):
    student=1
    studentspages=0
    n=len(arr)
    for i in range(n):
        if studentspages+arr[i]<=pages:
            studentspages+=arr[i]
        else:
            student+=1
            studentspages=arr[i]
    return student  
def bookallocation(arr,m,n):
    low=max(arr)
    high=sum(arr)
    if m>n:
        return -1
    while high>=low:
        mid=(low+high)//2
        no_of_stu=findpages(arr,mid)
        if no_of_stu>m:
            low=mid+1
        else:
            high=mid-1
    return low        

if __name__=="__main__":
    arr = [25, 46, 28, 49, 24]
    n = 5
    m = 4
    ans=bookallocation(arr,m,n)
    print("The answer is:", ans)

        
          
                
def findlarge(arr,large):
    student=1
    studentspage=0
    n=len(arr)
    for  i in range(n):
        if studentspage+arr[i]<=large:
            studentspage+=arr[i]
        else:
            student+=1
            studentspage=arr[i]
    return student
def largest(arr,k):
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(low+high)//2
        no_large=findlarge(arr,mid)
        if no_large>k:
            low=mid+1
        else:
            high=mid-1
    return low

if __name__=="__main__":
    a = [10, 20, 30, 40]
k = 2
ans = largest(a, k)
print("The answer is:", ans)

    
                        
    
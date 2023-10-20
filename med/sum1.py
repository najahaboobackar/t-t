def main():
    arr=[1,2,3,4,5,6,7]
    n=len(arr)
    y=int(input("enter the  two number"))
    ans=twosum(arr,n,y)
    if ans:
        print("yes",ans)
    else:
        print("no")    
def twosum(arr,n,y):
    left=0
    sum=0
    right=n-1
    while left < right:
        sum=arr[left]+arr[right]
        if sum==y:
            return sum
        elif sum<y:
            left+=1
        else:
            right-=1
main()            
                
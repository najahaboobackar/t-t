def bookalloc(arr,k):
    sum=0
    ba=1
    n=len(arr)
    for i in range(n-1):
        max1=arr[i]
        for j in range(n-1):
            max1=max(max1,arr[j]+arr[i])
    for i in range(n-1):
        sum+=arr[i]
        if max1<=sum:
            ba+=1  
    if ba>=k:
        return sum
    
    
if __name__== "__main__":
    
    arr = [25, 46, 28, 49, 24]
    ans=bookalloc(arr,2)
    print("The answer is:", ans)
  
                      
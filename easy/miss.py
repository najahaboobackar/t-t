def main():
    arr=[1,2,4,5]
    n=len(arr)
    s=miss(arr,n)
    print(s)
def miss(arr,n):
    
        k=arr[n-1]
        s=0
        k=(k*(k-1))/2
        for i in range(n-1):
            s=s+arr[i]
        w=k-s 
        return w  
main()     
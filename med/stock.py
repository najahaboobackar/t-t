def main():
    arr=[7,1,5,3,6,4]
    n=len(arr)
    p=stock(arr,n)
    print(p)
def stock(arr,n):
    max=0
    proMax=0
    for i in range(n):
        for j in range(i+1,n-1):
            if arr[j] >arr[i]:
                proMax=arr[j]-arr[i]  
            if max<proMax:
                max=proMax     
    return max    
main()
        
def main():
    arr=[4,7,1,0]
    n=len(arr)
    leader(arr,n)
def leader(arr,n):
    a=[]
    max=arr[n-1]
    a.append(arr[n-1])
    for i in range(n-2,-1,-1): 
        if arr[i]>max:
            a.append(arr[i])
            max=arr[i]
               
    print(a)      
main()      
    
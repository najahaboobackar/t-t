def main():
    arr=[3,2,4,5,1,6,8]
    n=len(arr)
    m=findlargest(arr,n)
    print(m)
    
def findlargest(arr,n):
    max=arr[0]
    for i in range(1,n):
        if max < arr[i]:
            max=arr[i]
    return max        
                
                
main()                
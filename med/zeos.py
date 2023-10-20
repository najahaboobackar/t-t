def main():
    arr=[0,1,2,1,0]
    n=len(arr)
    sort(arr,n)
def sort(arr,n):
    p=0
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    print(arr)            
                
            
         
             
    
main()                    
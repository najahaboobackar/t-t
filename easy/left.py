def main():
    arr=[3,4,1,2,6,7,0]
    n=len(arr)
    leftRotate(arr,n)
    
def leftRotate(arr,n):
    for i in  range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
        
    temp=[0]*n
    for i  in range(n):
         temp[i-1]=arr[i] 
         arr[i]=arr[0] 
    print(temp)     
main()    
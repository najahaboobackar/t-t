def main():
    arr=[1,2,3,4,5,6,7,8,9]
    n=len(arr)
    leftRotate(arr,n)
    
def leftRotate(arr,n):
    shift=int(input("enter the d"))
    for i in range(0,shift):
        temp=arr[0]
        for j in range(1,n) :
            arr[j-1]=arr[j] 
        arr[j]=temp 
    print(arr)         
main()        
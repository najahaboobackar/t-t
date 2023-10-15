def main():
    arr=[1,3,2,7,4,6,8]
    n=len(arr)
    k=int(input("enter the key to be searched"))
    linearsearch(arr , n, k)
def linearsearch(arr,n,k):
    f=0
    for i in range(0,n-1):
        if arr[i]==k:
            f=1
        else:
            p=0
    if f==1:
        print("found")    
    elif p==0:
        print("not found")
                    
           
  
main()                        
def main():
    arr=[4,4,2,3,6,7,8,9,0]
    n=len(arr)
    getelement(arr,n)
def getelement(arr,n):
    for i in range (n-1):
        for j in range(n-1-i):
            if  arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    min=arr[1]
    max=arr[n-2]
    print(max,min)  
main()                 
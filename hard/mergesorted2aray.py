def main():
    arr=[1, 4, 8, 10]
    arr2=[2, 3, 9]
    m=len(arr2)
    n=len(arr)
    merge(arr,arr2,n,m)
def merge(arr,arr2,n,m):
    left=n-1 
    right=0
    while   left>=0 and right<m:
        if arr[left]>arr2[right]:
            arr[left],arr2[right]=arr2[right],arr[left]
        left-=1
        right+=1
    arr2.sort()
    arr.sort()
    print(arr)
    print(arr2)
main()        
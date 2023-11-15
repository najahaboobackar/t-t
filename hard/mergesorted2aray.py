def main():
    arr=[1,2,3,8]
    arr2=[9,0,10]
    m=len(arr2)
    n=len(arr)
    merge(arr,arr2,n,m)
def merge(arr,arr2,n,m):
    left=n-1 
    right=0
    while arr[left]<arr2[right] and left>0 and right<m:
        arr[left],arr2[right]=arr2[right],arr[left]
        left-=1
        right+=1
    arr2.sort()
    arr.sort()
    print(arr)
    print(arr2)
main()        
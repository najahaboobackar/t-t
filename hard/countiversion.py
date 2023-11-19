import math
def main():
    arr=[5, 4, 3, 2, 1]
    n=len(arr)
    count=inversion(arr,n)
    print(count)
def merge(arr,low,mid,high):
    temp=[]
    count=0
    left=0
    right=mid+1
    while left<=mid and right<=high:
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        elif arr[right]<arr[left]:
            temp.append(arr[right])
            right+=1
            count=(mid-left+1)
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while (right <= high):
        temp.append(arr[right])
        right += 1   
    return count
def mergesort(arr, low, high):
    count = 0

    if low < high:
        mid = (low + high) // 2

        # Recursive calls
        count += mergesort(arr, low, mid)
        count += mergesort(arr, mid + 1, high)

        # Merge the sorted halves
        count += merge(arr, low, mid, high)

    return count

def inversion(arr,n):
    return mergesort(arr,0,n-1)
main()

    
              
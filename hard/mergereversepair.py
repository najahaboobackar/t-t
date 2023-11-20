def main():
    arr= [4, 1, 2, 3, 1]
    n=len(arr)
    
    r=team(arr,n-1)
    print(r)
    
    
def merge(arr,low ,high,mid):
    temp=[]
    left=0
    right=mid+1
    while left<=mid and right<=high :
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        if arr[right]<arr[left]:
            temp.append(arr[right]) 
            right+=1  
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]    
def countpair(arr,low,high,mid):
    count=0
    right=mid+1
    for i in range(low,mid+1):
        while right<=high and arr[i]>2*arr[right] :
            right+=1
            count+= right-(mid+1)
            
    return count  
def mergesort(arr, low, high):
    count = 0
    if low < high:
        mid = (low + high) // 2

        count += mergesort(arr, low, mid)
        count += mergesort(arr, mid + 1, high)
        count += countpair(arr, low, high, mid)
        merge(arr, low, high, mid)

    return count
def team(arr,n):
    return mergesort(arr,0,n-1)

main()                  
        
                
            
        
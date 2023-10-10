def main():
    arr = [2, 4, 1, 2, 6, 4, 7, 8]
    lb = 0
    ub = len(arr) - 1
    mergesort(arr, lb, ub)
    print(arr)

def mergesort(arr, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2 #this used for division
        mergesort(arr, lb, mid)
        mergesort(arr, mid+1, ub)
        merge(arr, lb, mid, ub)

def merge(arr, lb, mid, ub):
    b = [0] * len(arr) #to store the till  length
    i = lb
    j = mid + 1
    k = lb
    while i <= mid and j <= ub:#if i is less then mid and j is less then upper bound  if array of i is lesthen j then store the value of i into b[k]
        if arr[i] < arr[j]:
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]#store j value
            j += 1
        k += 1
    while i <= mid: #if there is remaining element in i then add the element in b[k]
        b[k] = arr[i]
        i += 1
        k += 1
    while j <= ub: #if there is remaining element i kj add the value sis in b[k]
        b[k] = arr[j]
        j += 1
        k += 1

    for i in range(lb, ub+1):
        arr[i] = b[i]

if __name__ == "__main__":
    main()
